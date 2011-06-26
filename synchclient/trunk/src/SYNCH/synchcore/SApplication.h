/*
Посвещается моей любимой девушке Katsu Arsur
*/

#ifndef SAPPLICATION_H
#define SAPPLICATION_H

#include <QApplication>

#include "../synchuser/SUser.h"
#include "synchcore.h"

class SYNCHCORE_EXPORT SApplication : public QApplication
{
    Q_OBJECT
public:
    static SApplication* instance();
    SApplication(int & argc, char ** argv,QApplication::Type type = QApplication::GuiClient);
signals:

public slots:
  //  bool setUser( QString userName, QByteArray userHash );
private:

private:
//    SUser * m_user;
};

SYNCHCORE_H SApplication* sApp();

#endif // SAPPLICATION_H
