#include <iostream>
#include <set>
#include <queue>
#define INF 1e9
using namespace std;

int N, M, a, b, r;
priority_queue<pair<int, int>> pq;
vector<pair<int, int>> adj[1001];	// (번호, 거리)
int dist[1001];

int dijkstra(int start, int finish) {
	for (int i = 0; i < 1001; i++) {
		dist[i] = INF;
	}

	dist[start] = 0;
	pq.push({ 0, start });	// (거리, 번호)

	while (!pq.empty()) {
		auto v = pq.top();	pq.pop();
		int cur = v.second;
		int cost = -v.first;

		if (cur == finish) {
			return dist[cur];
		}

		for (auto w : adj[cur]) {
			int to = w.first;
			int weight = w.second;

			if (dist[cur] + weight < dist[to]) {
				dist[to] = dist[cur] + weight;
				pq.push({ -dist[to], to });
			}
		}
	}
}

int main() {
	cin >> N >> M;

	for (int i = 0; i < M; i++) {
		cin >> a >> b >> r;
		adj[a].push_back({ b, r });
	}

	cin >> a >> b;

	cout << dijkstra(a, b) << '\n';
}