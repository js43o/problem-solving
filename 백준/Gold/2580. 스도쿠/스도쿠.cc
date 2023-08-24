#include <iostream>
using namespace std;

int board[10][10];
bool each[10][10];
int z = 0;
struct pos {
	int x;
	int y;
	int sqr;
	pos()
		: x(0), y(0), sqr(0) {}
	pos(int x_, int y_, int sqr_)
		: x(x_), y(y_), sqr(sqr_) {}
};
pos list[81];
bool finish = false;

int findSqr(int i, int j) {
	if (i > 0 && i <= 3) {
		if (j > 0 && j <= 3) return 1;
		else if (j > 3 && j <= 6) return 2;
		else return 3;
	}
	else if (i > 3 && i <= 6) {
		if (j > 0 && j <= 3) return 4;
		else if (j > 3 && j <= 6) return 5;
		else return 6;
	}
	else {
		if (j > 0 && j <= 3) return 7;
		else if (j > 3 && j <= 6) return 8;
		else return 9;
	}
}

void sudoku(int count) {
	if (count == z) {
		for (int i = 1; i <= 9; i++) {
			for (int j = 1; j <= 9; j++) {
				cout << board[i][j] << " ";
			}
			cout << "\n";
		}
		finish = true;
		return;
	}
	
	int i = list[count].x;
	int j = list[count].y;
	int sqr = list[count].sqr;
	
	for (int n = 1; n <= 9; n++) {
		if (each[sqr][n] == false) {
			bool flag = true;
			// 십자 검사
			for (int r = 1; r <= 9; r++) {
				if (board[i][r] == n || board[r][j] == n) {
					flag = false;
					break;
				}
			}
			if (flag) {
				board[i][j] = n;
				each[sqr][n] = true;
				
				sudoku(count + 1);
				if (finish) return;
				
				each[sqr][n] = false;
				board[i][j] = 0;
			}
		}
	}
}

int main() {
	int input;
	for (int i = 1; i <= 9; i++) {
		for (int j = 1; j <= 9; j++) {
			cin >> input;
			board[i][j] = input;
			each[findSqr(i, j)][input] = true;
			
			if (input == 0) {
				list[z] = pos(i, j, findSqr(i, j));
				z++;
			}
		}
	}
	
	sudoku(0);
}