/*
����������� ���� ������� ������� Katsu Arsur
*/

#ifndef SMAINFORM_H
#define SMAINFORM_H

#include <QWidget>
#include "../synchwatcher/SWatcher.h"

namespace Ui {
    class SMainForm;
}

class SMainForm : public QWidget
{
    Q_OBJECT

public:
    explicit SMainForm(QWidget *parent = 0);
    ~SMainForm();
public slots:
    void addPathsForWatch();
    void sendDbgEntry();

private:
    Ui::SMainForm *ui;
    SWatcher * m_watcher;

};

#endif // SMAINFORM_H
