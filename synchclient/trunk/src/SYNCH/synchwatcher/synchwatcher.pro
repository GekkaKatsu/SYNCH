TEMPLATE = lib
QMAKE_LFLAGS += -Wl,-rpath=\'\$\$ORIGIN\'
TARGET = synchwatcher

CONFIG += qt

MOC_DIR = ../../../tmp
RCC_DIR = ../../../tmp
OBJECTS_DIR = ../../../tmp
UI_DIR = ../../../tmp

DLLDESTDIR += ../../../bin/windows

DESTDIR += ../../../lib/windows

LIBS +=  -L../../../lib/windows -lsynchcore

HEADERS += \
    SWatcher.h \
    synchwatcher.h


SOURCES += \
    SWatcher.cpp
