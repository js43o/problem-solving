#include <iostream>
using namespace std;

int arr[1000000];

void mergeSort(int start, int mid, int end) {
	if (start < end) {	// 쪼갤 수 있을 때
		mergeSort(start, (start + mid) / 2, mid);
		mergeSort(mid + 1, (mid + 1 + end) / 2, end);
	}
	else return;
	
	int left[500000];
	int right[500000];
	int lcount = 0;
	int rcount = 0;
	// 두 개로 분할
	for (int i = start; i <= mid; i++)
		left[lcount++] = arr[i];
	for (int i = mid + 1; i <= end; i++)
		right[rcount++] = arr[i];
	
	int idx = start;
	int leftIdx = 0;
	int rightIdx = 0;
	// 양쪽 비교하며 차례로 병합
	while (leftIdx < lcount && rightIdx < rcount) {
		if (left[leftIdx] < right[rightIdx])
			arr[idx++] = left[leftIdx++];
		else 
			arr[idx++] = right[rightIdx++];
	}
	// 남은 것 쑤셔넣기
	if (leftIdx >= lcount) {	// rightIdx < rcount
		for (int i = rightIdx; i < rcount; i++)
			arr[idx++] = right[i];
	}
	else if (rightIdx >= rcount) {	// leftIdx < lcount
		for (int i = leftIdx; i < lcount; i++)
			arr[idx++] = left[i];
	}
}

int main() {
	int n, input;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> input;
		arr[i] = input;
	}
	mergeSort(0, (n - 1) / 2, n - 1);
	
	for (int i = 0; i < n; i++) {
		cout << arr[i] << '\n';
	}
}