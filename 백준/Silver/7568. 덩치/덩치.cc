#include <iostream>
#include <vector>
using namespace std;

struct Man {
	int h, w, r;
	Man() : h(0), w(0), r(1) {}
	Man(int h_, int w_) : h(h_), w(w_), r(1) {}
};

int main() {
	int n, h, w;
	cin >> n;
	vector<Man> mans;
	for (int i = 0; i < n; i++) {
		cin >> h >> w;
		mans.push_back(Man(h, w));
	}
	for (int j = 0; j < mans.size(); j++) {
		for (int k = 0; k < mans.size(); k++) {
			if (j == k) continue;
			if (mans[j].h < mans[k].h && mans[j].w < mans[k].w)
				mans[j].r++;
		}
	}
	for (int m = 0; m < mans.size(); m++) {
		cout << mans[m].r << " ";
	}
	cout << endl;
}