TEMPLATE = app

CONFIG += qt

HEADERS += \
    SMainForm.h

SOURCES += \
    SMainForm.cpp \
    main.cpp

FORMS += \
    SMainForm.ui

LIBS += -L../../../lib/windows -lsynchcore -lsynchwatcher
