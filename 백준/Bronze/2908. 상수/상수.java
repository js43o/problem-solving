import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] str = sc.nextLine().split(" ");
		sc.close();
		int a = (str[0].charAt(2) - '0') * 100 + (str[0].charAt(1) - '0') * 10 + (str[0].charAt(0) - '0');
		int b = (str[1].charAt(2) - '0') * 100 + (str[1].charAt(1) - '0') * 10 + (str[1].charAt(0) - '0');
		if (a > b)
			System.out.print(a);
		else
			System.out.print(b);
	}
}