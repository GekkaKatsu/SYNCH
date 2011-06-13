/*
Посвещается моей любимой девушке Katsu Arsur
*/

#include "FileUtils.h"

QStringList FileUtils::getDirectoryNames()
{
    QFileDialog fileDialog;
    fileDialog.setFileMode(QFileDialog::Directory);
    QStringList fileNames;
    if (fileDialog.exec())
        fileNames = fileDialog.selectedFiles();
    return fileNames;
}
