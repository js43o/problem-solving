import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		String[] input = sc.nextLine().split(" ");
		sc.close();
		
		int a = Integer.parseInt(input[0]);
		int b = Integer.parseInt(input[1]);
		
		if (a > b)
			System.out.print(">");
		else if (a < b)
			System.out.print("<");
		else
			System.out.print("==");
	}
}