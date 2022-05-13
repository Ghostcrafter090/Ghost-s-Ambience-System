#include "dialog.h"
#include "./ui_dialog.h"

#include <iostream>

bool systemState = false;

Dialog::Dialog(QWidget *parent) : QDialog(parent), ui(new Ui::Dialog) {
    ui->setupUi(this);
}

Dialog::~Dialog() {
    delete ui;
}

void killSound() {
    system("start /min "" taskkill /f /im clock.exe");
    system("start /min "" taskkill /f /im fireplace.exe");
    system("start /min "" taskkill /f /im window.exe");
    system("start /min "" taskkill /f /im windown.exe");
    system("start /min "" taskkill /f /im outside.exe");
    system("start /min "" taskkill /f /im light.exe");
}

void Dialog::on_onButton_clicked() {
    if (systemState) {
        systemState = false;
        system("taskkill /t /f /im ambience.exe");
        killSound();
        ui->onButton->setText("Switch Online");
    } else {
        systemState = true;
        autoUpdate();
        system("pushd %USERPROFILE%\\Desktop\\ambience_py && start /min "" ambience \"py main.py\"");
        ui->onButton->setText("Switch Offline");
    }
}

#include "dialog.moc"
