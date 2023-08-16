#include <iostream>
using namespace std;
int main() {
	int x, y, w, h;
	cin >> x >> y >> w >> h;
	int garo, sero;
	
	if (x <= w - x) garo = x;
	else garo = w - x;
	
	if (y <= h - y) sero = y;
	else sero = h - y;
	
	if (garo <= sero) cout << garo;
	else cout << sero;
}