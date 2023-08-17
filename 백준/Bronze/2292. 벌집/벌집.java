import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.close();
		int count = 1;
		while (n > honey(count))
			count++;
		System.out.print(count);
	}

	public static int honey(int n) {
		if (n == 1)
			return 1;
		else
			return honey(n - 1) + 6 * (n - 1);
	}
}