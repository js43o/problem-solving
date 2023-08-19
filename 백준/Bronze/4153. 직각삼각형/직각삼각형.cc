#include <iostream>
using namespace std;
int main() {
	int x, y, z, garo, sero, bit;
	while (true) {
		cin >> x >> y >> z;
		if (x == 0 || y == 0 || z == 0) break;

		if (x > y && x > z) {
			bit = x;
			garo = y;
			sero = z;
		}
		else if (y > x && y > z) {
			bit = y;
			garo = x;
			sero = z;
		}
		else {
			bit = z;
			garo = x;
			sero = y;
		}
		
		if (bit * bit == garo * garo + sero * sero) cout << "right" << endl;
		else cout << "wrong" << endl;
	}
}