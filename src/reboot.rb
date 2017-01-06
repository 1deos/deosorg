require 'vagrant'
module VagrantPlugins
  module ProviderVirtualBox
    module Action
      class RemountSyncedFolders < SyncedFolders
        def initialize(app, env)
          super(app, env)
        end
        def call(env)
          @env = env
          @app.call(env)
          folders = synced_folders(env[:machine])
          folders.each do |impl_name, fs|
            plugins[impl_name.to_sym][0].new.enable(
                env[:machine], fs, impl_opts(impl_name, env))
          end
        end
      end
      def self.action_remount_synced_folders
        Vagrant::Action::Builder.new.tap do |b|
          b.use RemountSyncedFolders
        end
      end
    end
  end
end
class RebootPlugin < Vagrant.plugin('2')
  name 'Reboot Plugin'
  provisioner 'unix_reboot' do
    class RebootProvisioner < Vagrant.plugin('2', :provisioner)
      def initialize(machine, config)
        super(machine, config)
      end
      def configure(root_config)
        super(root_config)
      end
      def provision
        command = 'shutdown -r now'
        @machine.ui.info("Issuing command: #{command}")
        @machine.communicate.sudo(command) do |type, data|
          if type == :stderr
            @machine.ui.error(data);
          end
        end
        begin
          sleep 5
        end until @machine.communicate.ready?
        @machine.ui.info("Launching remount_synced_folders action...")
        @machine.action('remount_synced_folders')
      end
      def cleanup
        super
      end
    end
    RebootProvisioner
  end
  provisioner 'windows_reboot' do
    class RebootProvisioner < Vagrant.plugin('2', :provisioner)
      def initialize(machine, config)
        super(machine, config)
      end
      def configure(root_config)
        super(root_config)
      end
      def provision
        command = 'shutdown -t 0 -r -f'
        @machine.ui.info("Issuing command: #{command}")
        @machine.communicate.execute(command) do |type, data|
          if type == :stderr
            @machine.ui.error(data);
          end
        end
        begin
          sleep 5
        end until @machine.communicate.ready?
        @machine.ui.info("Launching remount_synced_folders action...")
        @machine.action('remount_synced_folders')
      end
      def cleanup
        super
      end
    end
    RebootProvisioner
  end
end
