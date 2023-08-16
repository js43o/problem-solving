import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.close();
		int count = 0;
		for (int i = 1; i <= n; i++) {
			if (han(i))
				count++;
		}
		System.out.print(count);
	}

	public static boolean han(int n) {
		if (n < 100)
			return true;
		else if ((n < 1000) && (2 * ((n / 10) - 10 * (n / 100)) == (n / 100) + (n % 10)))
			return true;
		else
			return false;
	}
}
