#ifndef DIALOG_H
#define DIALOG_H

#include "ui_dialog.h"
#include <QTimer>
#include <iostream>
#include <fstream>
#include <filesystem>
#include <QTableWidget>
#include <QHeaderView>
#include "logdisplay.cpp"

QT_BEGIN_NAMESPACE
namespace Ui { class Dialog; }
// class QLabel;
QT_END_NAMESPACE

class Dialog : public QDialog {

    Q_OBJECT

public:

    std::string apiKey = "";

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
        std::string pluginsList;
        std::getline(std::ifstream(".\\vars\\dispstring.cx"), display, '\0');
        std::getline(std::ifstream(".\\vars\\sounds\\clock.cxl"), clockList, '\0');
        std::getline(std::ifstream(".\\vars\\sounds\\fireplace.cxl"), fireplaceList, '\0');
        std::getline(std::ifstream(".\\vars\\sounds\\window.cxl"), windowList, '\0');
        std::getline(std::ifstream(".\\vars\\sounds\\outside.cxl"), outsideList, '\0');
        std::getline(std::ifstream(".\\vars\\pluginsList.pyn"), pluginsList, '\0');
        ui->conditions->setText(display.c_str());
        ui->clockSpeaker->setText(clockList.c_str());
        ui->fireplaceSpeaker->setText(fireplaceList.c_str());
        ui->windowSpeaker->setText(windowList.c_str());
        ui->outsideSpeaker->setText(outsideList.c_str());
        std::string path = ".\\vars\\pluginVars";
        std::string errorPath = ".\\vars\\plugins";
        std::string pathw = "";
        std::string working = "";
        ui->pluginVars->setRowCount(100);
        ui->pluginVars->setColumnCount(3);
        QHeaderView* header = ui->pluginVars->horizontalHeader();
        header->setSectionResizeMode(0, QHeaderView::ResizeToContents);
        header->setSectionResizeMode(1, QHeaderView::ResizeToContents);
        header->setSectionResizeMode(2, QHeaderView::ResizeToContents);
        ui->plugins->setRowCount(100);
        ui->plugins->setColumnCount(3);
        QHeaderView* headerf = ui->plugins->horizontalHeader();
        headerf->setSectionResizeMode(0, QHeaderView::ResizeToContents);
        headerf->setSectionResizeMode(1, QHeaderView::ResizeToContents);
        headerf->setSectionResizeMode(2, QHeaderView::ResizeToContents);
        int row = 0;
        int f = 0;
        int n = 0;
        for (const auto & entry : std::filesystem::directory_iterator(path)) {
            pathw = entry.path().u8string();
            std::getline(std::ifstream(pathw), working, '\0');
            qDebug() << getSplit(getSplit(pathw, '-', 0), '\\', 7).c_str();
            qDebug() << getSplit(pathw, '-', 1).c_str();
            std::string var = "";
            std::getline(std::ifstream(pathw), var, '\0');
            std::string compf = "[";
            std::string mainf = "";
            mainf = var.substr(0, 1);
            if (mainf == compf) {
                n = countChar(var, ",");
                f = 0;
                while (f < (n)) {
                    qDebug() << n;
                    qDebug() << getSplit(var, ',', n).c_str();
                    QTableWidgetItem *item_0 = ui->pluginVars->item(row, 0);
                    QTableWidgetItem *item_1 = ui->pluginVars->item(row, 1);
                    QTableWidgetItem *item_2 = ui->pluginVars->item(row, 2);
                    if(!item_0) {
                        item_0 = new QTableWidgetItem;
                        ui->pluginVars->setItem(row, 0, item_0);
                    }
                    if(!item_1) {
                        item_1 = new QTableWidgetItem;
                        ui->pluginVars->setItem(row, 1, item_1);
                    }
                    if(!item_2) {
                        item_2 = new QTableWidgetItem;
                        ui->pluginVars->setItem(row, 2, item_2);
                    }
                    item_0->setText(QString::fromStdString(getSplit(getSplit(pathw, '-', 0), '\\', 7)));
                    item_1->setText(QString::fromStdString(getSplit(getSplit(pathw, '.', 0), '-', 1) + "::" + std::to_string(f)));
                    item_2->setText(QString::fromStdString(getSplit(var, ',', f)));
                    f = f + 1;
                    row = row + 1;
                }
            } else {
                QTableWidgetItem *item_0 = ui->pluginVars->item(row, 0);
                QTableWidgetItem *item_1 = ui->pluginVars->item(row, 1);
                QTableWidgetItem *item_2 = ui->pluginVars->item(row, 2);
                if(!item_0) {
                    item_0 = new QTableWidgetItem;
                    ui->pluginVars->setItem(row, 0, item_0);
                }
                if(!item_1) {
                    item_1 = new QTableWidgetItem;
                    ui->pluginVars->setItem(row, 1, item_1);
                }
                if(!item_2) {
                    item_2 = new QTableWidgetItem;
                    ui->pluginVars->setItem(row, 2, item_2);
                }
                item_0->setText(QString::fromStdString(getSplit(getSplit(pathw, '-', 0), '\\', 7)));
                item_1->setText(QString::fromStdString(getSplit(getSplit(pathw, '.', 0), '-', 1)));
                item_2->setText(QString::fromStdString(var));
            }
            row = row + 1;
        }
        std::string pluginName = "";
        int r;
        int l;
        l = 0;
        r = countChar(pluginsList, ";");
        qDebug() << pluginsList.c_str();
        qDebug() << r;
        while (l < (r - 1)) {
            QTableWidgetItem *item_0 = ui->plugins->item(l, 0);
            QTableWidgetItem *item_1 = ui->plugins->item(l, 1);
            QTableWidgetItem *item_2 = ui->plugins->item(l, 2);
            if(!item_0) {
                item_0 = new QTableWidgetItem;
                ui->plugins->setItem(l, 0, item_0);
            }
            if(!item_1) {
                item_1 = new QTableWidgetItem;
                ui->plugins->setItem(l, 1, item_1);
            }
            if(!item_2) {
                item_2 = new QTableWidgetItem;
                ui->plugins->setItem(l, 2, item_2);
            }
            qDebug() << getSplit(pluginsList, ';', l).c_str();
            std::string varf = "";
            qDebug() << (".\\vars\\plugins\\" + getSplit(pluginsList, ';', l) + ".run()-error.cx").c_str();
            if (fileExists(".\\vars\\plugins\\" + getSplit(pluginsList, ';', l) + ".run()-error.cx")) {
                std::string loopStatus = "";
                std::getline(std::ifstream(".\\vars\\plugins\\" + getSplit(pluginsList, ';', l) + ".run()-error.cx"), varf, '\0');
                std::getline(std::ifstream(".\\vars\\plugins\\" + getSplit(pluginsList, ';', l) + ".run()-loopStatus.cx"), loopStatus, '\0');
                if (loopStatus == "True") {
                    QIcon icon(".\\launcher\\icons\\warning.gif");
                    item_0->setIcon(icon);
                } else {
                    QIcon icon(".\\launcher\\icons\\error.png");
                    item_0->setIcon(icon);
                }
            } else {
                QIcon icon(".\\launcher\\icons\\check.png");
                item_0->setIcon(icon);
            }
            item_1->setText(QString::fromStdString(getSplit(pluginsList, ';', l)));
            item_2->setText(QString::fromStdString(varf));
            l = l + 1;
        }
    }

    int countChar(std::string charf, std::string chara) {
        int count = 0;
        const char* stringf = charf.c_str();
        std::string comp;
        for(int i = 0; i < strlen(stringf); i++) {
            comp = stringf[i];
            if(comp == chara) {
                count = count + 1;
            }
        }
        return count;
    }

    void openSettingsWindow(){
        QWidget* textView = new QWidget();
        textView->show();
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

    inline bool fileExists (const std::string& name) {
        std::ifstream f(name.c_str());
        return f.good();
    }

private slots:
    void on_onButton_clicked();

private:
    // QLabel *ui_consoleOutput;
    Ui::Dialog *ui;
};
#endif // DIALOG_H
