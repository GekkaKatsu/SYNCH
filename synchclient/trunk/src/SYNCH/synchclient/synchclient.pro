TEMPLATE = app
QMAKE_LFLAGS += -Wl,-rpath=\'\$\$ORIGIN\'
CONFIG += qt

MOC_DIR = ../../../tmp
RCC_DIR = ../../../tmp
OBJECTS_DIR = ../../../tmp
UI_DIR = ../../../tmp

HEADERS += \
    SMainForm.h \

SOURCES += \
    SMainForm.cpp \
    main.cpp \

FORMS += \
    SMainForm.ui

LIBS += -L../../../lib/windows -lsynchcore -lsynchwatcher  -lsynchuser -lsynchnetworkmanager

DESTDIR += ../../../lib/windows
