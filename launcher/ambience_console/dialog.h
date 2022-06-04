#ifndef DIALOG_H
#define DIALOG_H

#include "ui_dialog.h"
#include <QTimer>
#include <iostream>
#include <fstream>
#include <filesystem>
#include <QTableWidget>
#include <QHeaderView>
#include <QHBoxLayout>

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

    QTableWidgetItem *pluginVarsf[100][3];

    QTableWidgetItem *pluginsf[100][3];

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
        ui->pluginVars->horizontalHeader()->setSectionResizeMode(0, QHeaderView::ResizeToContents);
        ui->pluginVars->horizontalHeader()->setSectionResizeMode(1, QHeaderView::ResizeToContents);
        ui->pluginVars->horizontalHeader()->setSectionResizeMode(2, QHeaderView::ResizeToContents);
        ui->plugins->setRowCount(100);
        ui->plugins->setColumnCount(3);
        ui->plugins->horizontalHeader()->setSectionResizeMode(0, QHeaderView::ResizeToContents);
        ui->plugins->horizontalHeader()->setSectionResizeMode(1, QHeaderView::ResizeToContents);
        ui->plugins->horizontalHeader()->setSectionResizeMode(2, QHeaderView::ResizeToContents);
        int row = 0;
        int f = 0;
        int n = 0;
        for (const auto & entry : std::filesystem::directory_iterator(path)) {
            pathw = entry.path().u8string();
            std::getline(std::ifstream(pathw), working, '\0');
            // qDebug() << getSplit(getSplit(pathw, '-', 0), '\\', 7).c_str();
            // qDebug() << getSplit(pathw, '-', 1).c_str();
            std::string var = "";
            std::getline(std::ifstream(pathw), var, '\0');
            std::string compf = "[";
            std::string mainf = "";
            mainf = var.substr(0, 1);
            if (mainf == compf) {
                n = countChar(var, ",");
                f = 0;
                while (f < (n)) {
                    // qDebug() << n;
                    // qDebug() << getSplit(var, ',', n).c_str();
                    pluginVarsf[row][0] = ui->pluginVars->item(row, 0);
                    pluginVarsf[row][1] = ui->pluginVars->item(row, 1);
                    pluginVarsf[row][2] = ui->pluginVars->item(row, 2);
                    if (!pluginVarsf[row][0]) {
                        pluginVarsf[row][0] = new QTableWidgetItem;
                        ui->pluginVars->setItem(row, 0, pluginVarsf[row][0]);
                    }
                    if (!pluginVarsf[row][1]) {
                        pluginVarsf[row][1] = new QTableWidgetItem;
                        ui->pluginVars->setItem(row, 1, pluginVarsf[row][1]);
                    }
                    if (!pluginVarsf[row][2]) {
                        pluginVarsf[row][2] = new QTableWidgetItem;
                        ui->pluginVars->setItem(row, 2, pluginVarsf[row][2]);
                    }
                    pluginVarsf[row][0]->setText(QString::fromStdString(getSplit(getSplit(pathw, "-", 0), "\\", 7)));
                    pluginVarsf[row][1]->setText(QString::fromStdString(getSplit(getSplit(pathw, ".", 0), "-", 1) + "::" + std::to_string(f)));
                    pluginVarsf[row][2]->setText(QString::fromStdString(getSplit(var, ",", f)));
                    f = f + 1;
                    row = row + 1;
                }
            } else {
                pluginVarsf[row][0] = ui->pluginVars->item(row, 0);
                pluginVarsf[row][1] = ui->pluginVars->item(row, 1);
                pluginVarsf[row][2] = ui->pluginVars->item(row, 2);
                if(!pluginVarsf[row][0]) {
                    pluginVarsf[row][0] = new QTableWidgetItem;
                    ui->pluginVars->setItem(row, 0, pluginVarsf[row][0]);
                }
                if(!pluginVarsf[row][1]) {
                    pluginVarsf[row][1] = new QTableWidgetItem;
                    ui->pluginVars->setItem(row, 1, pluginVarsf[row][1]);
                }
                if(!pluginVarsf[row][2]) {
                    pluginVarsf[row][2] = new QTableWidgetItem;
                    ui->pluginVars->setItem(row, 2, pluginVarsf[row][2]);
                }
                pluginVarsf[row][0]->setText(QString::fromStdString(getSplit(getSplit(pathw, "-", 0), "\\", 7)));
                pluginVarsf[row][1]->setText(QString::fromStdString(getSplit(getSplit(pathw, ".", 0), "-", 1)));
                pluginVarsf[row][2]->setText(QString::fromStdString(var));
            }
            row = row + 1;
        }
        std::string pluginName = "";
        int r;
        int l;
        l = 0;
        r = countChar(pluginsList, ";");
        // qDebug() << pluginsList.c_str();
        // qDebug() << r;
        while (l < (r - 1)) {
            pluginsf[l][0] = ui->plugins->item(l, 0);
            pluginsf[l][1] = ui->plugins->item(l, 1);
            pluginsf[l][2] = ui->plugins->item(l, 2);
            if(!pluginsf[l][0]) {
                pluginsf[l][0] = new QTableWidgetItem;
                ui->plugins->setItem(l, 0, pluginsf[l][0]);
            }
            if(!pluginsf[l][1]) {
                pluginsf[l][1] = new QTableWidgetItem;
                ui->plugins->setItem(l, 1, pluginsf[l][1]);
            }
            if(!pluginsf[l][2]) {
                pluginsf[l][2] = new QTableWidgetItem;
                ui->plugins->setItem(l, 2, pluginsf[l][2]);
            }
            // qDebug() << getSplit(pluginsList, ";", l).c_str();
            std::string varf = "";
            // qDebug() << (".\\vars\\plugins\\" + getSplit(pluginsList, ";", l) + ".run()-error.cx").c_str();
            if (fileExists(".\\vars\\plugins\\" + getSplit(pluginsList, ";", l) + ".run()-error.cx")) {
                std::string loopStatus = "";
                std::getline(std::ifstream(".\\vars\\plugins\\" + getSplit(pluginsList, ";", l) + ".run()-error.cx"), varf, '\0');
                std::getline(std::ifstream(".\\vars\\plugins\\" + getSplit(pluginsList, ";", l) + ".run()-loopStatus.cx"), loopStatus, '\0');
                if (loopStatus == "True") {
                    QIcon icon(".\\launcher\\icons\\warning.gif");
                    pluginsf[l][0]->setIcon(icon);
                } else {
                    QIcon icon(".\\launcher\\icons\\error.png");
                    pluginsf[l][0]->setIcon(icon);
                }
            } else {
                QIcon icon(".\\launcher\\icons\\check.png");
                pluginsf[l][0]->setIcon(icon);
            }
            pluginsf[l][1]->setText(QString::fromStdString(getSplit(pluginsList, ";", l)));
            pluginsf[l][2]->setText(QString::fromStdString(varf));
            l = l + 1;
        }
    }

    int countChar(std::string charf, std::string chara) {
        int count = 0;
        std::string comp;
        for(int i = 0; i < strlen(charf.c_str()); i++) {
            comp = charf.c_str()[i];
            if(comp == chara) {
                count = count + 1;
            }
        }
        return count;
    }

    void openWindow(){

    }

    std::string getSplit(std::string const &str, std::string delim, int n = 0) {
        size_t start;
        size_t end = 0;
        int i = 0;
        std::string out = "";
        while ((start = str.find_first_not_of(delim.c_str(), end)) != std::string::npos) {
            end = str.find(delim.c_str(), start);
            if (i == n) {
                out = str.substr(start, end - start);
            }
            i = i + 1;
        }
        return out;
    }

    inline bool fileExists (std::string name) {
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
