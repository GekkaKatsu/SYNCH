/*
Посвещается моей любимой девушке Katsu Arsur
*/

#ifndef SUSER_H
#define SUSER_H

#include <QObject>

class SUser : public QObject
{
    Q_OBJECT
public:
    SUser* sUser();
signals:

public slots:

private:
    explicit SUser(QObject *parent = 0);
private:
    SUser * m_sUserInstanse;
};

#endif // SUSER_H
