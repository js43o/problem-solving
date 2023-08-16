import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int count = 1;
		String s = sc.nextLine();
		sc.close();
		s = s.trim();
		if (s.isEmpty()) {
			System.out.println(0);
			return;
		}
		for (int i = 0; i < s.length(); i++)
			if (s.charAt(i) == ' ')
				count++;
		System.out.println(count);
	}
}