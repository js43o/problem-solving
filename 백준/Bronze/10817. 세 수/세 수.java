import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] str = sc.nextLine().split(" ");
		sc.close();

		int a = Integer.parseInt(str[0]);
		int b = Integer.parseInt(str[1]);
		int c = Integer.parseInt(str[2]);
		int mid = 0;

		if (a >= b) {
			if (b >= c)
				mid = b;
			else {
				if (a >= c)
					mid = c;
				else
					mid = a;
			}
		}
		else {
			if (a >= c)
				mid = a;
			else {
				if (c >= b)
					mid = b;
				else
					mid = c;
			}
		}
		System.out.print(mid);
	}
}