TEMPLATE = lib

TARGET = synchwatcher

CONFIG += qt

DLLDESTDIR += ../../../bin/windows

DESTDIR += ../../../lib/windows

LIBS +=  -L../../../lib/windows -lsynchcore

HEADERS += \
    SWatcher.h \
    synchwatcher.h


SOURCES += \
    SWatcher.cpp
