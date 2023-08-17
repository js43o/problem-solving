#include <iostream>
#include <queue>
using namespace std;

int N, M;
int map[101][101];
bool visited[101][101];
int cheese;
int result;

int dy[4] = { -1, 1, 0, 0 };
int dx[4] = { 0, 0, -1, 1 };

void spreadAir() {
	queue <pair<int, int>> q;

	// visited 초기화
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			visited[i][j] = false;
		}
	}

	q.push({ 0, 0 });
	visited[0][0] = true;

	while (!q.empty()) {
		int y = q.front().first;
		int x = q.front().second;
		q.pop();

		for (int k = 0; k < 4; k++) {
			if (y + dy[k] < 0 || y + dy[k] >= N || x + dx[k] < 0 || x + dx[k] >= M) continue;
			if (!visited[y + dy[k]][x + dx[k]] && map[y + dy[k]][x + dx[k]] != 1) {
				visited[y + dy[k]][x + dx[k]] = true;
				q.push({ y + dy[k], x + dx[k] });
			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (visited[i][j]) {
				map[i][j] = 2;
			}
		}
	}
}

void meltCheese() {
	queue<pair<int, int>> melting;

	// 치즈가 2면 이상 노출되었는지 체크
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (map[i][j] != 1) continue;

			int adj = 0;
			for (int k = 0; k < 4; k++) {
				if (i + dy[k] < 0 || i + dy[k] >= N || j + dx[k] < 0 || j + dx[k] >= M) continue;
				if (map[i + dy[k]][j + dx[k]] == 2) adj++;
			}

			if (adj >= 2) {
				melting.push({ i, j });
				cheese--;
			}
		}
	}

	// 모아두었다가 한꺼번에 없애기
	while (!melting.empty()) {
		int y = melting.front().first;
		int x = melting.front().second;
		melting.pop();

		map[y][x] = 2;
	}
}



int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> map[i][j];
			if (map[i][j] == 1) cheese++;
		}
	}

	while (cheese > 0) {
		spreadAir();
		meltCheese();
		result++;
	}

	cout << result << '\n';
}