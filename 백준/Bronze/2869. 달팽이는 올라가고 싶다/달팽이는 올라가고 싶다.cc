#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int a;
	int b;
	int v;
	cin >> a >> b >> v;
	int c = ceil(static_cast<double>(v - b) / (a - b));
	cout << c;
}