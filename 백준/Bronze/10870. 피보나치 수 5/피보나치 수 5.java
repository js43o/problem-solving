import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.close();
		System.out.print(fibo(n));
	}

	public static int fibo(int n) {
		if (n == 0 || n == 1)
			return n;
		else
			return fibo(n - 2) + fibo(n - 1);
	}
}
