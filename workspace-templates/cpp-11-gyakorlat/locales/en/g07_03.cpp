#include <iostream>
using namespace std;

struct Device { int id; bool active; };
void deactivate(Device* p) {
    // TODO: handle valid and null pointers
}

int main() {
    int id, active;
    cin >> id >> active;
    Device item{id, active != 0};
    deactivate(&item);
    deactivate(nullptr);
    cout << item.id << " " << item.active << "\n";
    return 0;
}
