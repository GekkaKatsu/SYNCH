/*
Посвещается моей любимой девушке Katsu Arsur
*/

#ifndef SFILEUPLOADTHREAD_H
#define SFILEUPLOADTHREAD_H

#include <QThread>
#include <QFile>
#include "synchnetworkmanager.h"

class SFileUploadThread : public QThread
{
    Q_OBJECT
public:
    explicit SFileUploadThread(QObject *parent = 0);

signals:

public slots:

private:
    QFile m_file;
};

#endif // SFILEUPLOADTHREAD_H
