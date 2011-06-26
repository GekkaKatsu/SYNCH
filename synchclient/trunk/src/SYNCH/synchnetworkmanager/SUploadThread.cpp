/*
Посвещается моей любимой девушке Katsu Arsur
*/

#include "SUploadThread.h"
#include <QtNetwork/QNetworkAccessManager>
#include <QtNetwork/QNetworkRequest>
#include <QtNetwork/QNetworkReply>
#include <QMutex>

#include <QDebug>

#include "../synchcore/SCmdLog.h"

static int ref = 0;

QMutex mutex;

void SUploadThread::run()
{    
    if( m_nwManager )
    {
        m_nwManager->deleteLater();
        m_nwManager = 0;
    }

    m_nwManager = new QNetworkAccessManager();
    m_nwManager->moveToThread(this);
    connect( m_nwManager,SIGNAL(finished(QNetworkReply*)),this,SLOT(replyFinished(QNetworkReply*)));

    mutex.lock();
    ref++;

    QNetworkRequest rqst;
    rqst.setUrl(QUrl("http://www.synch.su/client"));
    QByteArray data;
    QString dbgEntry = QString("query=acquireUploadUrl");
    qDebug() << dbgEntry;
    data.append(dbgEntry);
    m_nwManager->post(rqst,data);
    mutex.unlock();
    qDebug() << "From thread" << ref;
    exec();
}

void SUploadThread::replyFinished(QNetworkReply *reply)
{
    qDebug() << "rcvd reply";
    SCmdLog::instance()->addEntry( reply->readAll() );
}
