import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int caseNum = sc.nextInt();
		for (int i = 0; i < caseNum; i++) {
			int k = sc.nextInt();
			int n = sc.nextInt();
			System.out.println(summer(k, n));
		}
		sc.close();
	}
	
	public static int summer(int k, int n) {
		if (k == 0)
			return n;
		else {
			int sum = 0;
			for (int i = 1; i <= n; i++)
				sum += summer(k - 1, i);
			return sum;
		}
	}
}