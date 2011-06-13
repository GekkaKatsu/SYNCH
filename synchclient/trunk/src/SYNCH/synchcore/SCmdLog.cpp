/*
Посвещается моей любимой девушке Katsu Arsur
*/

#include "SCmdLog.h"

SCmdLog * SCmdLog::m_cmdLog = 0;

SCmdLog::SCmdLog(QObject *parent) :
    QObject(parent)
{
}

SCmdLog * SCmdLog::instance()
{
    if( !m_cmdLog )
        m_cmdLog = new SCmdLog();
    return m_cmdLog;
}

void SCmdLog::addEntry( QString entry )
{
    emit entryAdded( entry );
}
