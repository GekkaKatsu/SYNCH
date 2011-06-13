TEMPLATE = lib

TARGET = synchcore

CONFIG += core


DLLDESTDIR += ../../../bin/windows

DESTDIR += ../../../lib/windows



HEADERS += \
    SCmdLog.h \
    synchcore.h \
    FileUtils.h

SOURCES += \
    SCmdLog.cpp \
    FileUtils.cpp
