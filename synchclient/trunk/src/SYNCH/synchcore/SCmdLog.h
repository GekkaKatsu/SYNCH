/*
Посвещается моей любимой девушке Katsu Arsur
*/

#ifndef SCMDLOG_H
#define SCMDLOG_H

#include <QObject>
#include <QStringList>

#include "synchcore.h"

class SYNCHCORE_EXPORT SCmdLog : public QObject
{
    Q_OBJECT

    enum LogEntryTypes
    {
        Folder,
        User,
        Other
    };

public:
    static SCmdLog * instance();

public slots:
    void addEntry( QString );
signals:
    void entryAdded( QString );

private:
    SCmdLog(QObject *parent = 0);
private:
    static SCmdLog * m_cmdLog;
    QStringList m_loggingEntries;
};

SYNCHCORE_EXPORT SCmdLog* sLog();

#endif // SCMDLOG_H
