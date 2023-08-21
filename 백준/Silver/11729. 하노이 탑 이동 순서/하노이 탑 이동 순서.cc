#include<iostream>

using namespace std;


void hanoi(int T,int from,int mid,int to)
{
	if (T == 1)
	{
		cout << from << " " << to << "\n";
	}
	else
	{
		hanoi(T - 1, from, to, mid);
		cout << from << " " << to << "\n";
		hanoi(T - 1, mid, from, to);
	}

}

int main()
{
	int T;
	

	cin >> T;

	int result = 1;

	for (int i = 0; i < T; i++)
	{
		result *= 2;
	}
	
	cout << result - 1 << "\n";

	hanoi(T, 1, 2, 3);

}