#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct edge {
	int s, e, t;
};

int N, M, W, S, E, T;
int dist[501];
vector<edge> edges;

bool bellman_ford() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < edges.size(); j++) {
			int cur = edges[j].s;
			int to = edges[j].e;
			int cost = edges[j].t;

			if (dist[to] > dist[cur] + cost) {
				dist[to] = dist[cur] + cost;

				if (i == N - 1) return true;
			}
		}
	}

	return false;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int TC;
	cin >> TC;

	while (TC--) {
		// 초기화
		for (int i = 0; i < 501; i++) {
			dist[i] = 0;
		}
		edges.clear();

		cin >> N >> M >> W;

		for (int i = 0; i < M; i++) {
			cin >> S >> E >> T;
			edges.push_back({ S, E, T });
			edges.push_back({ E, S, T });
		}

		for (int i = 0; i < W; i++) {
			cin >> S >> E >> T;
			edges.push_back({ S, E, -T });
		}

		cout << (bellman_ford() ? "YES" : "NO") << '\n';
	}
}