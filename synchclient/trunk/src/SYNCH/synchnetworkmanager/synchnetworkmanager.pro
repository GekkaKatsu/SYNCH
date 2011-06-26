TEMPLATE = lib
QMAKE_LFLAGS += -Wl,-rpath=\'\$\$ORIGIN\'
TARGET = synchnetworkmanager

CONFIG += qt
QT += network

MOC_DIR = ../../../tmp
RCC_DIR = ../../../tmp
OBJECTS_DIR = ../../../tmp
UI_DIR = ../../../tmp

DLLDESTDIR += ../../../bin/windows

DESTDIR += ../../../lib/windows

HEADERS += \
    synchnetworkmanager.h \
    SUploadThread.h \
    SFileUploadThread.h


SOURCES += \
    SUploadThread.cpp \
    SFileUploadThread.cpp
