/*
Посвещается моей любимой девушке Katsu Arsur
*/

#ifndef SUPLOADTHREAD_H
#define SUPLOADTHREAD_H

#include <QThread>
#include <QtNetwork/QNetworkAccessManager>
#include "synchnetworkmanager.h"

class QNetworkReply;

class SYNCHNETWORKMANAGER_EXPORT SUploadThread : public QThread
{
    Q_OBJECT
public:
    void run();

signals:

public slots:
    void replyFinished(QNetworkReply* reply);

private:
    QNetworkAccessManager * m_nwManager;
};

#endif // SUPLOADTHREAD_H
