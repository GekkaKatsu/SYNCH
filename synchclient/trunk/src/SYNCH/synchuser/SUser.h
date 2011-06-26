/*
Посвещается моей любимой девушке Katsu Arsur
*/

#ifndef SUSER_H
#define SUSER_H

#include <QObject>
#include "synchuser.h"

class SYNCHUSER_EXPORT SUser : public QObject
{
    Q_OBJECT
public:
    SUser(QObject *parent = 0);
signals:

public slots:
    QByteArray userSignature();

private:
    SUser * m_sUserInstanse;
};

#endif // SUSER_H
