/*
Посвещается моей любимой девушке Katsu Arsur
*/

#ifndef SWATCHER_H
#define SWATCHER_H

#include <QObject>
#include <QFileSystemWatcher>
#include <QStringList>

class SWatcher : public QFileSystemWatcher
{
    Q_OBJECT
public:
    explicit SWatcher(QObject *parent = 0);

signals:

public slots:
    void addPathForWatching( QString );
    void stateOfDirectoryChanged( QString );
    void stateOfFileChanged( QString );
private:
    QStringList m_watchedPaths;
};

#endif // SWATCHER_H
