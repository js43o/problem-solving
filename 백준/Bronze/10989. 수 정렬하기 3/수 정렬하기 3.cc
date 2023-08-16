#include <stdio.h>
using namespace std;

int main() {
	int n, input;
	int count[10001];
	
	for (int i = 0; i <= 10000; i++)
		count[i] = 0;
	
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		scanf("%d", &input);
		count[input]++;
	}
	
	for (int i = 1; i <= 10000; i++) {
		while (count[i]-- > 0) {
			printf("%d\n", i);
		}
	}
}