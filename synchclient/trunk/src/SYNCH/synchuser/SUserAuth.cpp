/*
Посвещается моей любимой девушке Katsu Arsur
*/

#include "SUserAuth.h"
#include "ui_SUserAuth.h"

SUserAuth::SUserAuth(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::SUserAuth)
{
    ui->setupUi(this);
}

SUserAuth::~SUserAuth()
{
    delete ui;
}
