#include <iostream>
#include <cmath>
#define MAX 21
using namespace std;

int n;
int board[MAX][MAX];
int arr[MAX];
bool selected[MAX];
int dif = -1;

void calculate() {
	int start = 0;
	int link = 0;
	
	for (int i = 1; i <= n / 2; i++)
		for (int j = 1; j <= n / 2; j++)
			start += board[arr[i]][arr[j]];
	
	for (int i = n / 2 + 1; i <= n; i++)
		for (int j = n / 2 + 1; j <= n; j++)
			link += board[arr[i]][arr[j]];
	
	if (dif == -1 || dif >= abs(start - link))
		dif = abs(start - link);
}


void select(int count) {
	if (count > n / 2) {
		// 남은 것들 link로 쑤셔넣기
		for (int i = 1; i <= n; i++)
			if (!selected[i])
				arr[count++] = i;
		
		calculate();
		return;
	}
	
	for (int i = 1; i <= n; i++) {
		if (!selected[i] && count > 0 && arr[count - 1] < i) {
			selected[i] = true;
			arr[count] = i;
			select(count + 1);
			selected[i] = false;
		}
	}
}

int main() {
	cin >> n;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> board[i][j];
		}
	}
	
	select(1);
	
	cout << dif << endl;
	
	// 1. n개에서 n/2를 정한다. (조합)
	// -> 먼저 start n/2개 고르고 그 뒤에 남은 거 다 link로.
	// 2. 6개 중 3개 -> 1, 3, 6이면 1-3, 3-1, 1-6, 6-1, 3-6, 6-3. 3개 중 2개 (순열)
	// 3. 스타트/링크 각각 한 번씩 더하고 비교해서 다시 1번으로.
}