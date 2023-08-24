#include <iostream>
using namespace std;

int arr[100001][3];
int dpMax[3];
int dpMaxPrev[3];
int dpMin[3];
int dpMinPrev[3];

int main() {
	int N;

	cin >> N;

	for (int i = 1; i <= N; i++) {
		for (int k = 0; k < 3; k++) {
			cin >> arr[i][k];
		}
	}

	for (int i = 0; i < 3; i++) {
		dpMax[i] = arr[1][i];
		dpMin[i] = arr[1][i];
	}

	for (int i = 1; i <= N; i++) {
		dpMax[0] = arr[i][0] + max(dpMaxPrev[0], dpMaxPrev[1]);
		dpMax[1] = arr[i][1] + max(dpMaxPrev[0], max(dpMaxPrev[1], dpMaxPrev[2]));
		dpMax[2] = arr[i][2] + max(dpMaxPrev[1], dpMaxPrev[2]);

		dpMin[0] = arr[i][0] + min(dpMinPrev[0], dpMinPrev[1]);
		dpMin[1] = arr[i][1] + min(dpMinPrev[0], min(dpMinPrev[1], dpMinPrev[2]));
		dpMin[2] = arr[i][2] + min(dpMinPrev[1], dpMinPrev[2]);

		for (int k = 0; k < 3; k++) {
			dpMaxPrev[k] = dpMax[k];
			dpMinPrev[k] = dpMin[k];
		}
	}

	cout << max(dpMax[0], max(dpMax[1], dpMax[2])) << " " << min(dpMin[0], min(dpMin[1], dpMin[2])) << endl;
}