#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int T;
	cin >> T;
	while (T--) {
		int x1, y1, r1, x2, y2, r2;
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
	
		// 원의 중심 사이의 거리
		double pr = sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2));
		
		if (x1 == x2 && y1 == y2 && r1 == r2)	// 두 원이 일치
			cout << -1 << endl;
		else if (pr < r1 + r2 && pr > abs(r1 - r2))	// 두 점에서 겹침
			cout << 2 << endl;
		else if (pr == r1 + r2 || pr == abs(r1 - r2))	// 외접 or 내접
			cout << 1 << endl;
		else if (pr > r1 + r2 || pr < abs(r1 - r2))	// 멀리 떨어짐 or 한 원이 포함
			cout << 0 << endl;
	}
}