TEMPLATE = lib
QMAKE_LFLAGS += -Wl,-rpath=\'\$\$ORIGIN\'
TARGET = synchcore

CONFIG += core

MOC_DIR = ../../../tmp
RCC_DIR = ../../../tmp
OBJECTS_DIR = ../../../tmp
UI_DIR = ../../../tmp

DLLDESTDIR += ../../../bin/windows

DESTDIR += ../../../lib/windows

LIBS += -L../../../lib/windows

HEADERS += \
    SCmdLog.h \
    synchcore.h \
    FileUtils.h \
    SApplication.h

SOURCES += \
    SCmdLog.cpp \
    FileUtils.cpp \
    SApplication.cpp
