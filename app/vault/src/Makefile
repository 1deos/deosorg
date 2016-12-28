UI_GENERATED := \
    ui_mainwindow.py \
    ui_addgroup_dialog.py \
    ui_trezor_passphrase_dialog.py \
    ui_add_password_dialog.py \
    ui_initialize_dialog.py \
    ui_enter_pin_dialog.py \
    ui_trezor_chooser_dialog.py \
    #end of UI_GENERATED

all: $(UI_GENERATED)

ui_%.py: %.ui
	pyuic4 -o $@ $<


clean:
	rm -rf $(UI_GENERATED)
