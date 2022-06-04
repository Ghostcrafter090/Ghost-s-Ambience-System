#include "dialog.h"

#include <QApplication>

std::string apiKey;

int main(int argc, char *argv[])
{
    apiKey = argv[1];
    QApplication a(argc, argv);
    Dialog w;
    w.apiKey = apiKey;
    w.show();
    return a.exec();
}

#include "main.moc"
