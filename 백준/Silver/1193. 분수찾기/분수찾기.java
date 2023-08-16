import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.close();
		int count = 1;
		while (n >= floor(count))	// n번째 수의 분자와 분모의 합 = count
			count++;
		int pre = floor(count - 1);	// count가 같은 첫 번째 수
		int denom = 0;
		int numer = 0;
		if (count % 2 == 0) {
			denom = n - pre + 1;
			numer = count - denom;
		}
		else {
			numer = n - pre + 1;
			denom = count - numer;
		}
		System.out.print(numer + "/" + denom);
	}
	
	public static int floor(int n) {
		if (n == 1)
			return 1;
		else
			return floor(n - 1) + (n - 1);
	}
}