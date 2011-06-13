/*
Посвещается моей любимой девушке Katsu Arsur
*/

#include "SWatcher.h"
#include "../synchcore/SCmdLog.h"

SWatcher::SWatcher(QObject *parent) :
    QFileSystemWatcher(parent)
    ,m_watchedPaths(QStringList())
{
    connect( this, SIGNAL(directoryChanged(QString)),this,SLOT(stateOfDirectoryChanged(QString)));
    connect( this, SIGNAL(fileChanged(QString)),this,SLOT(stateOfFileChanged(QString)));
}

void SWatcher::addPathForWatching( QString value )
{
    SCmdLog::instance()->addEntry( value );
    addPath( value );
}

void SWatcher::stateOfDirectoryChanged(QString path)
{
    QString logString = QString("State of directort %1 changed. Current state: %2").arg(path);
    SCmdLog::instance()->addEntry(logString);
}

void SWatcher::stateOfFileChanged(QString path)
{
    QString logString = QString("State of file %1 changed. Current state: %2").arg(path);
    SCmdLog::instance()->addEntry(logString);
}
