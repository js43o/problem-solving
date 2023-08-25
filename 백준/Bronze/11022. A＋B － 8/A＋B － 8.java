import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int count = sc.nextInt();
		String[] result = new String[count];
		sc.nextLine();
		for (int i = 0; i < count; i++) {
			String[] str = sc.nextLine().split(" ");
			result[i] = String.format("%s + %s = %d", str[0], str[1],
					Integer.parseInt(str[0]) + Integer.parseInt(str[1]));
		}
		sc.close();
		for (int i = 0; i < count; i++)
			System.out.println("Case #" + (i + 1) + ": " + result[i]);
	}
}