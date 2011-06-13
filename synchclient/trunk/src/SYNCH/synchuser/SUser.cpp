/*
Посвещается моей любимой девушке Katsu Arsur
*/

#include "SUser.h"

SUser::SUser(QObject *parent) :
    QObject(parent)
{
}

SUser * SUser::sUser()
{
    if( !m_sUserInstanse )
        m_sUserInstanse = new SUser();
    return m_sUserInstanse;
}
