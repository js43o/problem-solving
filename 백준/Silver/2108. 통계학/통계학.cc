#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int arr[500001];
	int sorted[500001];
	int count[8001];
	for (int i = 0; i < 8001; i++)
		count[i] = 0;
	int n, input;
	double sum;
	int max = 8001;
	int min = 8001;
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> input;
		input += 4000;	// 음수 보정
		arr[i] = input;
		count[input]++;
		sum += input - 4000;	// 합은 원래 수로 저장
		if (max == 8001 || max < input) max = input;
		if (min == 8001 || min > input) min = input;
	}
	bool flag = false;
	int modeNum = 0;
	int mode;
	// 최빈값 자체 훑기
	for (int i = 0; i < 8001; i++) {
		if (modeNum < count[i])
			modeNum = count[i];
	}
	// 두 번째로 작은 값 찾기
	for (int i = 0; i < 8001; i++) {
		if (modeNum == count[i]) {
			mode = i;
			if (!flag) flag = true;
			else break;
		}
	}
	// 누적합
	for (int i = 1; i <= 8000; i++)
		count[i] += count[i - 1];
	// 계수정렬
	for (int i = n - 1; i >= 0; i--) {
		if (count[arr[i]] > 0)
			sorted[--count[arr[i]]] = arr[i];
	}
	
	cout << int(round(sum / n)) << endl << sorted[(n - 1) / 2] - 4000 << endl
		<< mode - 4000 << endl << max - min << endl;
}