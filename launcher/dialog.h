#ifndef DIALOG_H
#define DIALOG_H

#include "ui_dialog.h"
#include <QTimer>
#include <iostream>
#include <fstream>
#include <filesystem>

QT_BEGIN_NAMESPACE
namespace Ui { class Dialog; }
// class QLabel;
QT_END_NAMESPACE

class Dialog : public QDialog {
    Q_OBJECT

public:
    void autoUpdate() {
        QTimer *timer = new QTimer(this);

        QObject::connect(timer, SIGNAL(timeout()), this, SLOT(dynamics()));

        timer->start(1000);
    }

    Dialog(QWidget *parent = nullptr);
    ~Dialog();

public slots:
    void dynamics() {
        std::string display;
        std::string clockList;
        std::string fireplaceList;
        std::string windowList;
        std::string outsideList;
        std::getline(std::ifstream(".\\vars\\dispstring.cx"), display, '\0');
        std::getline(std::ifstream(".\\vars\\sounds\\clock.cxl"), clockList, '\0');
        std::getline(std::ifstream(".\\vars\\sounds\\fireplace.cxl"), fireplaceList, '\0');
        std::getline(std::ifstream(".\\vars\\sounds\\window.cxl"), windowList, '\0');
        std::getline(std::ifstream(".\\vars\\sounds\\outside.cxl"), outsideList, '\0');
        ui->conditions->setText(display.c_str());
        ui->clockSpeaker->setText(clockList.c_str());
        ui->fireplaceSpeaker->setText(fireplaceList.c_str());
        ui->windowSpeaker->setText(windowList.c_str());
        ui->outsideSpeaker->setText(outsideList.c_str());
        std::string path = "C:\\users\\joshp\\desktop\\ambience_py\\vars\\plugins";
        std::string pathw = "";
        std::string working = "";
        for (const auto & entry : std::filesystem::directory_iterator(path)) {
            pathw = entry.path().u8string();
            std::getline(std::ifstream(pathw), working, '\0');
            qDebug() << getSplit(getSplit(pathw, '-', 0), '\\', 7).c_str();
            qDebug() << getSplit(pathw, '-', 1).c_str();
        }
    }

    std::string getSplit(std::string const &str, const char delim, int n = 0) {
        size_t start;
        size_t end = 0;
        int i = 0;
        std::string out = "";
        while ((start = str.find_first_not_of(delim, end)) != std::string::npos) {
            end = str.find(delim, start);
            if (i == n) {
                out = str.substr(start, end - start);
            }
            i = i + 1;
        }
        return out;
    }

private slots:
    void on_onButton_clicked();

private:
    // QLabel *ui_consoleOutput;
    Ui::Dialog *ui;
};
#endif // DIALOG_H
