#include <iostream>
#include <map>
#include <queue>
#define INF 1e9	// 10e9 쓰면 중간에 짤림! (10e9 == 10 * 10^9 == 10^10)
using namespace std;

map<int, int> adj[20001];	// (to, weight), 같은 정점끼리라면 가장 가중치가 작은 것만 저장.
priority_queue<pair<int, int>> pq;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int V, E, K, u, v, w;

	cin >> V >> E >> K;

	for (int i = 0; i < E; i++) {
		cin >> u >> v >> w;

		if (!adj[u][v]) {
			adj[u][v] = w;
			continue;
		}
		adj[u][v] = min(adj[u][v], w);
	}

	vector<int> dist(V + 1, INF);
	dist[K] = 0;
	pq.push({0, K});	// 정점의 현재 가중치에 대한 정보. 가중치의 절댓값이 작은 순으로 정렬됨. (-가중치, 정점)

	while (!pq.empty()) {
		int cost = -pq.top().first;	// 거꾸로 삽입된 부호를 양수로 복원함.
		int v = pq.top().second;
		pq.pop();

		if (dist[v] < cost) continue;	// 큐에서 꺼낸 거리 정보가 갱신되기 전의 옛날 자료면 버림.

		for (auto w : adj[v]) {
			int to = w.first;
			int weight = w.second;

			if (dist[v] + weight < dist[to]) {
				dist[to] = dist[v] + weight;
				pq.push({-dist[to], to});	// max-heap을 min-heap처럼 쓰기 위해 거리의 부호를 음수로 바꿔 삽입.
			}
		}
	}

	for (int i = 1; i <= V; i++) {
		if (dist[i] == INF) {
			cout << "INF" << '\n';
			continue;
		}
		cout << dist[i] << '\n';
	}
}