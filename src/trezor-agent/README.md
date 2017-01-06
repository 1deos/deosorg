# Using TREZOR as a hardware SSH/GPG agent

[![Build Status](https://travis-ci.org/romanz/trezor-agent.svg?branch=master)](https://travis-ci.org/romanz/trezor-agent)
[![Python Versions](https://img.shields.io/pypi/pyversions/trezor_agent.svg)](https://pypi.python.org/pypi/trezor_agent/)
[![Package Version](https://img.shields.io/pypi/v/trezor_agent.svg)](https://pypi.python.org/pypi/trezor_agent/)
[![Development Status](https://img.shields.io/pypi/status/trezor_agent.svg)](https://pypi.python.org/pypi/trezor_agent/)
[![Downloads](https://img.shields.io/pypi/dm/trezor_agent.svg)](https://pypi.python.org/pypi/trezor_agent/)

See SatoshiLabs' blog posts about this feature:

- [TREZOR Firmware 1.3.4 enables SSH login](https://medium.com/@satoshilabs/trezor-firmware-1-3-4-enables-ssh-login-86a622d7e609)
- [TREZOR Firmware 1.3.6 — GPG Signing, SSH Login Updates and Advanced Transaction Features for Segwit](https://medium.com/@satoshilabs/trezor-firmware-1-3-6-20a7df6e692)
- [TREZOR Firmware 1.4.0 — GPG decryption support](https://www.reddit.com/r/TREZOR/comments/50h8r9/new_trezor_firmware_fidou2f_and_initial_ethereum/d7420q7/)

## Installation

First, make sure that the latest [trezorlib](https://pypi.python.org/pypi/trezor) Python package
is installed correctly (at least v0.6.6):

  $ apt-get install python-dev libusb-1.0-0-dev libudev-dev
  $ pip install -U setuptools pip
  $ pip install Cython trezor

Make sure that your `udev` rules are configured [correctly](https://doc.satoshilabs.com/trezor-user/settingupchromeonlinux.html#manual-configuration-of-udev-rules).
Then, install the latest [trezor_agent](https://pypi.python.org/pypi/trezor_agent) package:

  $ pip install trezor_agent

Or, directly from the latest source code (if `pip` doesn't work for you):

  $ git clone https://github.com/romanz/trezor-agent && cd trezor-agent
  $ python setup.py build && python setup.py install

Finally, verify that you are running the latest [TREZOR firmware](https://wallet.mytrezor.com/data/firmware/releases.json) version (at least v1.4.0):

  $ trezorctl get_features | head
  vendor: "bitcointrezor.com"
  major_version: 1
  minor_version: 4
  patch_version: 0
  ...

If you have an error regarding `protobuf` imports (after installing it), please see [this issue](https://github.com/romanz/trezor-agent/issues/28).

## Usage

For SSH, see the [following instructions](README-SSH.md) (for Windows support,
see [trezor-ssh-agent](https://github.com/martin-lizner/trezor-ssh-agent) project (by Martin Lízner)).

For GPG, see the [following instructions](README-GPG.md).

See [here](https://github.com/romanz/python-trezor#pin-entering) for PIN entering instructions.

## Troubleshooting

If there is an import problem with the installed `protobuf` package,
see [this issue](https://github.com/romanz/trezor-agent/issues/28) for fixing it.

### Gitter

Questions, suggestions and discussions are welcome: [![Chat](https://badges.gitter.im/romanz/trezor-agent.svg)](https://gitter.im/romanz/trezor-agent)

---

# SSH - Screencast demo usage

## Simple usage (single SSH session)
[![Demo](https://asciinema.org/a/22959.png)](https://asciinema.org/a/22959)

## Advanced usage (multiple SSH sessions from a sub-shell)
[![Subshell](https://asciinema.org/a/33240.png)](https://asciinema.org/a/33240)

## Using for GitHub SSH authentication (via `trezor-git` utility)
[![GitHub](https://asciinema.org/a/38337.png)](https://asciinema.org/a/38337)

## Loading multiple SSH identities from configuration file
[![Config](https://asciinema.org/a/bdxxtgctk5syu56yfz8lcp7ny.png)](https://asciinema.org/a/bdxxtgctk5syu56yfz8lcp7ny)

# Public key generation

Run:

  /tmp $ trezor-agent user@ssh.hostname.com -v > hostname.pub
  2015-09-02 15:03:18,929 INFO         getting "ssh://user@ssh.hostname.com" public key from Trezor...
  2015-09-02 15:03:23,342 INFO         disconnected from Trezor
  /tmp $ cat hostname.pub
  ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBGSevcDwmT+QaZPUEWUUjTeZRBICChxMKuJ7dRpBSF8+qt+8S1GBK5Zj8Xicc8SHG/SE/EXKUL2UU3kcUzE7ADQ= ssh://user@ssh.hostname.com

Append `hostname.pub` contents to `/home/user/.ssh/authorized_keys`
configuration file at `ssh.hostname.com`, so the remote server
would allow you to login using the corresponding private key signature.

# Usage

Run:

  /tmp $ trezor-agent user@ssh.hostname.com -v -c
  2015-09-02 15:09:39,782 INFO         getting "ssh://user@ssh.hostname.com" public key from Trezor...
  2015-09-02 15:09:44,430 INFO         please confirm user "roman" login to "ssh://user@ssh.hostname.com" using Trezor...
  2015-09-02 15:09:46,152 INFO         signature status: OK
  Linux lmde 3.16.0-4-amd64 #1 SMP Debian 3.16.7-ckt11-1+deb8u3 (2015-08-04) x86_64

  The programs included with the Debian GNU/Linux system are free software;
  the exact distribution terms for each program are described in the
  individual files in /usr/share/doc/*/copyright.

  Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
  permitted by applicable law.
  Last login: Tue Sep  1 15:57:05 2015 from localhost
  ~ $

Make sure to confirm SSH signature on the Trezor device when requested.

## Accessing remote Git/Mercurial repositories

Use your SSH public key to access your remote repository (e.g. [GitHub](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)):

  $ trezor-agent -v -e ed25519 git@github.com | xclip

Use the following Bash alias for convinient Git operations:

  $ alias git_hub='trezor-agent -v -e ed25519 git@github.com -- git'

Replace `git` with `git_hub` for remote operations:

  $ git_hub push origin master

The same works for Mercurial (e.g. on [BitBucket](https://confluence.atlassian.com/bitbucket/set-up-ssh-for-mercurial-728138122.html)):

  $ trezor-agent -v -e ed25519 git@bitbucket.org -- hg push


# Troubleshooting

If SSH connection fails to work, please open an [issue](https://github.com/romanz/trezor-agent/issues)
with a verbose log attached (by running `trezor-agent -vv`) .

## Incompatible SSH options

Note that your local SSH configuration may ignore `trezor-agent`, if it has `IdentitiesOnly` option set to `yes`.

     IdentitiesOnly
             Specifies that ssh(1) should only use the authentication identity files configured in
             the ssh_config files, even if ssh-agent(1) or a PKCS11Provider offers more identities.
             The argument to this keyword must be “yes” or “no”.
             This option is intended for situations where ssh-agent offers many different identities.
             The default is “no”.

If you are failing to connect, try running:

    $ trezor-agent -vv user@host -- ssh -vv -oIdentitiesOnly=no user@host

---

Note: the GPG-related code is still under development, so please try the current implementation
and feel free to [report any issue](https://github.com/romanz/trezor-agent/issues) you have encountered.
Thanks!

# Installation

First, verify that you have GPG 2.1.11+ installed
([Debian](https://gist.github.com/vt0r/a2f8c0bcb1400131ff51),
[macOS](https://sourceforge.net/p/gpgosx/docu/Download/)):

```
$ gpg2 --version | head -n1
gpg (GnuPG) 2.1.15
```

This GPG version is included in [Ubuntu 16.04](https://launchpad.net/ubuntu/+source/gnupg2)
and [Linux Mint 18](https://community.linuxmint.com/software/view/gnupg2).

Update you TREZOR firmware to the latest version (at least v1.4.0).

Install latest `trezor-agent` package from GitHub:
```
$ pip install --user git+https://github.com/romanz/trezor-agent.git
```

# Quickstart

## Identity creation
[![asciicast](https://asciinema.org/a/c2yodst21h9obttkn9wgf3783.png)](https://asciinema.org/a/c2yodst21h9obttkn9wgf3783)

## Sample usage (signature and decryption)
[![asciicast](https://asciinema.org/a/7x0h9tyoyu5ar6jc8y9oih0ba.png)](https://asciinema.org/a/7x0h9tyoyu5ar6jc8y9oih0ba)

You can use GNU Privacy Assistant (GPA) in order to inspect the created keys
and perform signature and decryption operations using:

```
$ sudo apt install gpa
$ ./scripts/gpg-shell gpa
```
[![GPA](https://cloud.githubusercontent.com/assets/9900/20224804/053d7474-a849-11e6-87f3-ab07dc536158.png)](https://www.gnupg.org/related_software/swlist.html#gpa)

## Git commit & tag signatures:
Git can use GPG to sign and verify commits and tags (see [here](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work)):
```
$ git config --local gpg.program $(which gpg2)
$ git commit --gpg-sign                      # create GPG-signed commit
$ git log --show-signature -1                # verify commit signature
$ git tag v1.2.3 --sign                      # create GPG-signed tag
$ git tag v1.2.3 --verify                    # verify tag signature
```
