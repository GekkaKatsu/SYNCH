/*
Посвещается моей любимой девушке Katsu Arsur
*/

#include "SApplication.h"

SApplication::SApplication(int & argc, char ** argv,QApplication::Type type):
            QApplication(argc, argv,type)
            //,m_user(new SUser())
{

}

SApplication * SApplication::instance()
{
    SApplication* app = qobject_cast<SApplication*>(qApp);
    return app;
}

SApplication* sApp()
{
    return SApplication::instance();
}
