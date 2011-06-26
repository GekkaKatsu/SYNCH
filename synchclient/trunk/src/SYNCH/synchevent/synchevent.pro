TEMPLATE = lib
QMAKE_LFLAGS += -Wl,-rpath=\'\$\$ORIGIN\'
TARGET = synchevent

CONFIG += qt

MOC_DIR = ../../../tmp
RCC_DIR = ../../../tmp
OBJECTS_DIR = ../../../tmp

DLLDESTDIR += ../../../bin/windows

DESTDIR += ../../../lib/windows

HEADERS += \


SOURCES += \

#Will implemented soon
