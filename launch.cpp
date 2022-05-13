#include <iostream>

int main(int argc, char *argv[]) {
    std::string comm = argv[1];
    std::string command = "start /wait /b \"\" " + comm;
    std::cout << system(command.c_str());
}