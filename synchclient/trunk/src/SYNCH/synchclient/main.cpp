/*
Посвещается моей любимой девушке Katsu Arsur
*/

#include <QApplication>
#include "SMainForm.h"

int main(int argc, char **argv)
{
    /*TODO add cheking gui and non-gui version*/
    QApplication app(argc, argv);
    SMainForm mainForm;
    mainForm.show();
    return app.exec();
}
