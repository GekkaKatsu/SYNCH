TEMPLATE = lib
QMAKE_LFLAGS += -Wl,-rpath=\'\$\$ORIGIN\'
TARGET = synchuser

QT += core gui

MOC_DIR = ../../../tmp
RCC_DIR = ../../../tmp
OBJECTS_DIR = ../../../tmp
UI_DIR = ../../../tmp

DLLDESTDIR += ../../../bin/windows

DESTDIR += ../../../lib/windows

HEADERS += \
    SUser.h \
    SUserAuth.h \
    synchuser.h

SOURCES += \
    SUser.cpp \
    SUserAuth.cpp

FORMS += \
    SUserAuth.ui
