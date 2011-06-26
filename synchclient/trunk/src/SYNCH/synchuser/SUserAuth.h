/*
Посвещается моей любимой девушке Katsu Arsur
*/

#ifndef SUSERAUTH_H
#define SUSERAUTH_H

#include <QWidget>

namespace Ui {
    class SUserAuth;
}

class SUserAuth : public QWidget
{
    Q_OBJECT

public:
    explicit SUserAuth(QWidget *parent = 0);
    ~SUserAuth();

private:
    Ui::SUserAuth *ui;
};

#endif // SUSERAUTH_H
