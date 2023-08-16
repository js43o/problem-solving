import java.util.Scanner;
import java.util.Vector;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int input = sc.nextInt();
		if (input < 10)
			input *= 10;
		int sum = 0;
		int newNum = 0;
		int count = 0;
		int save = input;
		while (true) {
			int a = input / 10;
			int b = input - a * 10;
			sum = a + b;
			if (sum < 10)
				newNum = b * 10 + sum;
			else {
				int c = sum / 10;
				int d = sum - c * 10;
				newNum = b * 10 + d;
			}
			count++;
			if (newNum == save)
				break;
			input = newNum;
		}
		sc.close();
		System.out.print(count);
	}
}