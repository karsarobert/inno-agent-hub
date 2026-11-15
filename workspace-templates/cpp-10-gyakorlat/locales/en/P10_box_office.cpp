// Existing classes are provided; you write the new file-I/O methods.
#include <iostream>
using namespace std;

const int CAPACITY = 4;
class Ticket {
private:
    int row;
    int seat;
public:
    Ticket() : row(0), seat(0) {}
    Ticket(int newRow, int newSeat) : row(0), seat(0) {
        if (newRow >= 1 && newRow <= 3 && newSeat >= 1 && newSeat <= 4) {
            row = newRow; seat = newSeat;
        }
    }
    int getRow() const { return row; }
    int getSeat() const { return seat; }
    bool isValid() const { return row >= 1 && row <= 3 && seat >= 1 && seat <= 4; }
    int price() const { return !isValid() ? 0 : row == 1 ? 4000 : 3000; }
};
class BoxOffice {
private:
    Ticket tickets[CAPACITY];
    int count;
public:
    BoxOffice() : count(0) {}
    int getCount() const { return count; }
    bool isBooked(int row, int seat) const {
        for (int i = 0; i < count; ++i)
            if (tickets[i].getRow() == row && tickets[i].getSeat() == seat) return true;
        return false;
    }
    bool add(int row, int seat) {
        Ticket item(row, seat);
        if (!item.isValid() || count >= CAPACITY || isBooked(row, seat)) return false;
        tickets[count] = item;
        ++count;
        return true;
    }
    int revenue() const {
        int sum = 0;
        for (int i = 0; i < count; ++i) sum += tickets[i].price();
        return sum;
    }
    void list() const {
        for (int i = 0; i < count; ++i)
            cout << tickets[i].getRow() << ' ' << tickets[i].getSeat() << '\n';
    }
// TODO: P2-P5
};
int main() {
    BoxOffice office;
    cout << office.add(1,2) << ' ' << office.add(2,3) << ' '
         << office.add(1,2) << '\n';
    cout << office.getCount() << ' ' << office.revenue() << '\n';
}
