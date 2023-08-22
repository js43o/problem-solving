#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

int N, M;
int town[51][51];
vector<pair<int, int>> house;
vector<pair<int, int>> chicken;

int dy[4] = { 0, 0, -1, 1 };
int dx[4] = { -1, 1, 0, 0 };
bool visited[51][51];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	vector<bool> ind;

	cin >> N >> M;

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> town[i][j];
			if (town[i][j] == 1) house.push_back({ i, j });
			if (town[i][j] == 2) chicken.push_back({ i, j });
		}
	}

	for (int i = 0; i < M; i++) {
		ind.push_back(true);
	}

	for (int i = M; i < chicken.size(); i++) {
		ind.push_back(false);
	}

	sort(ind.begin(), ind.end());

	int result = 1e9;

	do {
		int chickenDist[101];
		for (int i = 0; i < 101; i++) chickenDist[i] = 1e8;
		// 모든 치킨집 조합에 대하여
		for (int i = 0; i < ind.size(); i++) {
			if (!ind[i]) continue;
			// 각 집마다 가장 가까운 치킨 거리를 구함
			for (int k = 0; k < house.size(); k++) {
				int y = house[k].first;
				int x = house[k].second;

				chickenDist[k] = min(chickenDist[k], abs(y - chicken[i].first) + abs(x - chicken[i].second));
			}
		}
		// 치킨 거리의 합이 최소면 결과에 덮어씌움
		int acc = 0;
		for (int i = 0; i < 101; i++) {
			if (chickenDist[i] < 1e8) acc += chickenDist[i];
		}
		result = min(result, acc);

	} while (next_permutation(ind.begin(), ind.end()));

	cout << result << '\n';
}