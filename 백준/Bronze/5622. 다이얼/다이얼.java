import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		sc.close();
		int time = 0;
		for (int i = 0; i < str.length(); i++) {
			time += dia(str.charAt(i));
		}
		System.out.print(time);
	}

	public static int dia(char ch) {
		int result = 0;
		if (ch >= 'A' && ch <= 'C')
			result = 3;
		else if (ch >= 'D' && ch <= 'F')
			result = 4;
		else if (ch >= 'G' && ch <= 'I')
			result = 5;
		else if (ch >= 'J' && ch <= 'L')
			result = 6;
		else if (ch >= 'M' && ch <= 'O')
			result = 7;
		else if (ch >= 'P' && ch <= 'S')
			result = 8;
		else if (ch >= 'T' && ch <= 'V')
			result = 9;
		else
			result = 10;
		return result;
	}
}