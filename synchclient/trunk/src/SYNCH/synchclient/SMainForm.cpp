/*
����������� ���� ������� ������� Katsu Arsur
*/

#include "SMainForm.h"
#include "ui_SMainForm.h"
#include "../synchcore/SCmdLog.h"
#include "../synchcore/FileUtils.h"

SMainForm::SMainForm(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::SMainForm)
    ,m_watcher( new SWatcher())
{
    ui->setupUi(this);
    connect(SCmdLog::instance(),SIGNAL(entryAdded( QString )),this->ui->m_cmdWindow,SLOT(append(QString)));
    connect(this->ui->addPathButton,SIGNAL(clicked()),this,SLOT(addPathsForWatch()));
}

SMainForm::~SMainForm()
{
    delete ui;
}

void SMainForm::addPathsForWatch()
{
    QStringList pathList = FileUtils::getDirectoryNames();
    foreach ( QString path, pathList )
    {
        m_watcher->addPathForWatching(path);
    }
}
