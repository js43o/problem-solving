#include <iostream>
#define MAX 12
using namespace std;

int n;
bool isFirst = true;
int maxNum = 0;
int minNum = 0;
int nums[MAX];
int opers[4];
int used[4];

int operate(int n1, int n2, int oper) {
	switch (oper) {
	case 0:
		return n1 + n2;
	case 1:
		return n1 - n2;
	case 2:
		return n1 * n2;
	case 3:
		return n1 / n2;
	}
	return 0;
}

void calculate(int pre, int idx) {
	if (idx >= n - 1) {
		if (isFirst) {
			maxNum = pre;
			minNum = pre;
			isFirst = false;
		}
		else {
			if (pre >= maxNum) maxNum = pre;
			if (pre <= minNum) minNum = pre;
			return;
		}
	}
	
	for (int i = 0; i < 4; i++) {
		if (used[i] < opers[i]) {
			used[i]++;
			calculate(operate(pre, nums[idx + 1], i), idx + 1);
			used[i]--;
		}
	}
}

int main() {
	cin >> n;
	
	for (int i = 0; i < n; i++)
		cin >> nums[i];
	
	for (int i = 0; i < 4; i++)
		cin >> opers[i];
	
	calculate(nums[0], 0);
	
	cout << maxNum << endl << minNum << endl;
}