#include <iostream>
#include <queue>
#include <string>
using namespace std;

struct pos {
	int y;
	int x;
	bool couldBreak;
};

int maze[1001][1001];
int dist[1001][1001];
bool passByBreaker[1001][1001];
bool passByUnbreaker[1001][1001];
queue<pos> q;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	string str;

	cin >> N >> M;

	for (int i = 1; i <= N; i++) {
		cin >> str;
		for (int j = 1; j <= M; j++) {
			maze[i][j] = str[j - 1] == '0' ? 0 : 1;
		}
	}

	dist[1][1] = 1;
	q.push({ 1, 1, true });

	while (!q.empty()) {
		int y = q.front().y;
		int x = q.front().x;
		bool couldBreak = q.front().couldBreak;
		q.pop();

		// cout << "(" << y << ", " << x << "): " << maze[y][x] << " - " << couldBreak << endl;

		if (y == N && x == M) {
			break;
		}

		if (y - 1 > 0) {
			// 벽을 한 번도 부수지 않은 자
			if (couldBreak && !passByUnbreaker[y - 1][x]) {
				dist[y - 1][x] = dist[y][x] + 1;
				// 벽을 만나면 부수게 됨
				if (maze[y - 1][x] == 1) {
					passByBreaker[y - 1][x] = true;
					q.push({ y - 1, x, false });
				}
				// 안 부숨 유지
				else {
					passByUnbreaker[y - 1][x] = true;
					q.push({ y - 1, x, true });
				}
			}
			// 벽을 이미 부순 자
			if (!couldBreak && !passByBreaker[y - 1][x] && maze[y - 1][x] != 1) {
				dist[y - 1][x] = dist[y][x] + 1;
				passByBreaker[y - 1][x] = true;
				q.push({ y - 1, x, false });
			}
		}
		if (y + 1 <= N) {
			// 벽을 한 번도 부수지 않은 자
			if (couldBreak && !passByUnbreaker[y + 1][x]) {
				dist[y + 1][x] = dist[y][x] + 1;
				// 벽을 만나면 부수게 됨
				if (maze[y + 1][x] == 1) {
					passByBreaker[y + 1][x] = true;
					q.push({ y + 1, x, false });
				}
				// 안 부숨 유지
				else {
					passByUnbreaker[y + 1][x] = true;
					q.push({ y + 1, x, true });
				}
			}
			// 벽을 이미 부순 자
			if (!couldBreak && !passByBreaker[y + 1][x] && maze[y + 1][x] != 1) {
				dist[y + 1][x] = dist[y][x] + 1;
				passByBreaker[y + 1][x] = true;
				q.push({ y + 1, x, false });
			}
		}
		if (x - 1 > 0) {
			// 벽을 한 번도 부수지 않은 자
			if (couldBreak && !passByUnbreaker[y][x - 1]) {
				dist[y][x - 1] = dist[y][x] + 1;
				// 벽을 만나면 부수게 됨
				if (maze[y][x - 1] == 1) {
					passByBreaker[y][x - 1] = true;
					q.push({ y, x - 1, false });
				}
				// 안 부숨 유지
				else {
					passByUnbreaker[y][x - 1] = true;
					q.push({ y, x - 1, true });
				}
			}
			// 벽을 이미 부순 자
			if (!couldBreak && !passByBreaker[y][x - 1] && maze[y][x - 1] != 1) {
				dist[y][x - 1] = dist[y][x] + 1;
				passByBreaker[y][x - 1] = true;
				q.push({ y, x - 1, false });
			}
		}
		if (x + 1 <= M) {
			// 벽을 한 번도 부수지 않은 자
			if (couldBreak && !passByUnbreaker[y][x + 1]) {
				dist[y][x + 1] = dist[y][x] + 1;
				// 벽을 만나면 부수게 됨
				if (maze[y][x + 1] == 1) {
					passByBreaker[y][x + 1] = true;
					q.push({ y, x + 1, false });
				}
				// 안 부숨 유지
				else {
					passByUnbreaker[y][x + 1] = true;
					q.push({ y, x + 1, true });
				}
			}
			// 벽을 이미 부순 자
			if (!couldBreak && !passByBreaker[y][x + 1] && maze[y][x + 1] != 1) {
				dist[y][x + 1] = dist[y][x] + 1;
				passByBreaker[y][x + 1] = true;
				q.push({ y, x + 1, false });
			}
		}
	}

	if (dist[N][M] > 0) {
		cout << dist[N][M] << '\n';
	}
	else {
		cout << -1 << '\n';
	}
}