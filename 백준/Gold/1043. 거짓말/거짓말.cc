#include <iostream>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

int N, M, K, input, result;
vector<int> knower;
vector<int> party[51];
int parent[51];

int find_root(int x) {
	if (x == parent[x]) return x;
	return parent[x] = find_root(parent[x]);
}

void union_root(int x, int y) {
	int u = find_root(x);
	int v = find_root(y);
	parent[v] = u;
}

int main() {
	cin >> N >> M >> K;

	// 인지자 따로 받아두기
	for (int i = 1; i <= K; i++) {
		cin >> input;
		knower.push_back(input);
	}

	for (int i = 1; i <= M; i++) {
		cin >> K;
		for (int j = 1; j <= K; j++) {
			cin >> input;
			party[i].push_back(input);
		}
	}

	// 초기 parent 값은 자기 자신
	for (int i = 1; i <= N; i++) parent[i] = i;
	
	// 각 파티마다 다 묶어줌
	for (int i = 1; i <= M; i++) {
		int leader = party[i][0];
		for (int j = 0; j < party[i].size(); j++) {
			union_root(leader, party[i][j]);
		}
	}

    // 모든 파티 인원에 대해
	for (int i = 1; i <= M; i++) {
		bool flag = true;
		int leader = party[i][0];
        // 인지자와 1명이라도 겹치는지 확인
		for (int k : knower) {
			if (find_root(k) == find_root(leader)) {
				flag = false;
				break;
			}
		}
		if (flag) result++;
	}

	cout << result << '\n';
}