#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int N;
long long B;
int matrix[5][5][40];	// matrix^(2^k) (1 <= k < 40)
int result[5][5];

int main() {
	cin >> N >> B;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> matrix[i][j][0];	// 2^0승
			matrix[i][j][0] %= 1000;
		}
	}

	// 행렬의 (2^k)승 계산
	for (int k = 1; k < 40; k++) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				for (int t = 0; t < N; t++) {
					matrix[i][j][k] += (matrix[i][t][k - 1] * matrix[t][j][k - 1]);
					matrix[i][j][k] %= 1000;
				}
			}
		}
	}

	bool isFirst = true;

	while (B > 0) {
		int q = floor(log2(B));
		B -= pow(2, q);

		// 처음이면 그대로 복사
		if (isFirst) {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					result[i][j] = matrix[i][j][q];
				}
			}
			isFirst = false;
			continue;
		}

		// 처음이 아니면 행렬곱 수행
		// 매 차례 계산 결과가 다음 계산에 영향을 주지 않도록 임시 배열에 먼저 저장
		int temp[5][5];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int sums = 0;
				for (int t = 0; t < N; t++) {
					sums += (result[i][t] * matrix[t][j][q]);
				}
				temp[i][j] = sums % 1000;
			}
		}
		// 임시 배열을 결과 배열에 덮어씌움
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				result[i][j] = temp[i][j];
			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << result[i][j] << " ";
		}
		cout << '\n';
	}
}