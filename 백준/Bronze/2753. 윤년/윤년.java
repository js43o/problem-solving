import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int day = sc.nextInt();
		sc.close();
		
		if ((day % 4 == 0 && day % 100 != 0) || (day % 400 == 0))
			System.out.print(1);
		else
			System.out.print(0);
	}
}