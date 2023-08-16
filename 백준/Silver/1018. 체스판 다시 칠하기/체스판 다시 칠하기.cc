#include <iostream>
#include <string>
using namespace std;

int main() {
	char array[51][51];
	
	int n, m;
	string str;
	cin >> n >> m;
	
	for (int i = 0; i < n; i++) {
		cin >> str;
		for (int j = 0; j < m; j++) {
			array[i][j] = str.at(j);
		}
	}
	
	char target = 'B';
	int min = 10000;
	int count = 0;
	
	// start from B
	for (int k = 0; k < 2; k++) {
		
		for (int i = 0; i < n - 7; i++) {
			for (int j = 0; j < m - 7; j++) {
			
				for (int x = 0; x < 8; x++) {
					for (int y = 0; y < 8; y++) {
						if (array[i + x][j + y] != target) count++;
						
						if (y == 7) continue;
						// switch target
						if (target == 'B') target = 'W';
						else target = 'B';
					}
				}
				if (count < min) min = count;
				count = 0;
			}
		}
		// start from W
		target = 'W';
	}
	
	cout << min << endl;
}