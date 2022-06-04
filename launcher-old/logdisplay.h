#ifndef LOGDISPLAY_H
#define LOGDISPLAY_H

#include <QWidget>

class logDisplay : public QWidget {
    Q_OBJECT
    public:
        logDisplay(QWidget *parent = nullptr);
        ~logDisplay();

};

#endif // LOGDISPLAY_H
