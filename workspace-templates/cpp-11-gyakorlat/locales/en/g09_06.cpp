#include <iostream>
#include <string>
using namespace std;

class Device {
public:
    virtual string signal() const { return "BASE"; }
};
class Bell : public Device {
public:
    string signal() const override { return "DING"; }
};

int main() {
    int choice;
    cin >> choice;
    Device base;
    Bell bell;
    Device* pointer = &base;
    // TODO: call through the pointer
    if (choice == 1) pointer = &bell;
    // TODO: call through the pointer
    return 0;
}
