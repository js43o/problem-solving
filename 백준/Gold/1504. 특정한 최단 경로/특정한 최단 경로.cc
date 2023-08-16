#include <iostream>
#include <vector>
#include <queue>
#define MAX	1e9
using namespace std;

int N, E, a, b, c, v1, v2;
vector<pair<int, int>> adj[801];
int dist[801];

void dijkstra(int start) {
	for (int i = 0; i < 801; i++) dist[i] = MAX;	// 거리 초기화

	priority_queue<pair<int, int>> pq;				// (-거리, 번호)
	pq.push({ 0, start });
	dist[start] = 0;

	while (!pq.empty()) {
		int cur = pq.top().second;
		int curDist = -pq.top().first;
		pq.pop();

		for (auto w : adj[cur]) {
			int next = w.first;
			int cost = curDist + w.second;

			if (cost < dist[next]) {
				dist[next] = cost;
				pq.push({ -cost, next });
			}
		}
	}
}

int main() {
	cin >> N >> E;

	for (int i = 0; i < E; i++) {
		cin >> a >> b >> c;
		adj[a].push_back({ b, c });
		adj[b].push_back({ a, c });
	}

	cin >> v1 >> v2;

	dijkstra(1);
	int S_V1 = dist[v1];
	int S_V2 = dist[v2];

	dijkstra(v1);
	int V1_V2 = dist[v2];
	int V1_N = dist[N];

	dijkstra(v2);
	int V2_N = dist[N];

	if (V1_V2 == MAX || S_V1 == MAX || S_V2 == MAX || V1_N == MAX || V2_N == MAX) cout << -1;
	else cout << min(S_V1 + V1_V2 + V2_N, S_V2 + V1_V2 + V1_N);
}