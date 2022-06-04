#include "logdisplay.h"
#include <QWidget>

#include <QHBoxLayout>
#include <QLabel>

logDisplay::logDisplay(QWidget *parent) {
    setStyleSheet( "QWidget{ background-color : rgba( 160, 160, 160, 255); border-radius : 7px;  }" );
    QLabel *label = new QLabel(this);
    QHBoxLayout *layout = new QHBoxLayout();
    label->setText("Random String");
    layout->addWidget(label);
    setLayout(layout);
}
