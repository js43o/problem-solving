import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String n = sc.nextLine();
		sc.close();
		for (char i = 'a'; i <= 'z'; i++)
			System.out.print(n.indexOf(i) + " ");
	}
}