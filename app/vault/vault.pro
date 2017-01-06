QT       += core\
            gui
TARGET    = vault
TEMPLATE  = app
SOURCES  += main.cpp\
            mainwindow.cpp
HEADERS  += mainwindow.h
FORMS    += mainwindow.ui\
            addgroup_dialog.ui\
            trezor_passphrase_dialog.ui\
            add_password_dialog.ui\
            initialize_dialog.ui\
            enter_pin_dialog.ui\
            trezor_chooser_dialog.ui
