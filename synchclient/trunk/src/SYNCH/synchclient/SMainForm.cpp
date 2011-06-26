/*
����������� ���� ������� ������� Katsu Arsur
*/

#include "SMainForm.h"
#include "ui_SMainForm.h"
#include "../synchcore/SCmdLog.h"
#include "../synchcore/FileUtils.h"
#include "../synchnetworkmanager/SUploadThread.h"

SMainForm::SMainForm(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::SMainForm)
    ,m_watcher( new SWatcher())
{
    ui->setupUi(this);
    connect(SCmdLog::instance(),SIGNAL(entryAdded( QString )),this->ui->m_cmdWindow,SLOT(append(QString)),Qt::QueuedConnection);
    connect(ui->addPathButton,SIGNAL(clicked()),this,SLOT(addPathsForWatch()));
    connect(ui->m_createDbgEntryButton,SIGNAL(clicked()),this,SLOT(sendDbgEntry()));
}

SMainForm::~SMainForm()
{
    delete ui;
}

/*
Todo: move to application
*/
void SMainForm::addPathsForWatch()
{
    QStringList pathList = FileUtils::getDirectoryNames();
    foreach ( QString path, pathList )
    {
        m_watcher->addPathForWatching(path);
    }
}

void SMainForm::sendDbgEntry()
{
    QList<SUploadThread*> m_list;
    for( int i = 0; i < 2; i++ )
    {
        SUploadThread * uploadThread = new SUploadThread();
        connect(uploadThread, SIGNAL(finished()), uploadThread, SLOT(deleteLater()),Qt::QueuedConnection);
        m_list.append(uploadThread);
    }
    foreach( SUploadThread* thread, m_list )
    {
        thread->start();
    }
}


