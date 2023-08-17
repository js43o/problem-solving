import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] count = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		sc.close();
		String num = String.valueOf(a * b * c);
		for (int i = 0; i < num.length(); i++) {
			int index = num.charAt(i) - '0';
			count[index]++;
		}
		for (int i = 0; i < count.length; i++)
			System.out.println(count[i]);
	}
}