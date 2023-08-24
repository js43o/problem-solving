import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		String a = sc.nextLine();
		String b = sc.nextLine();
		sc.close();
		
		int three = (Integer.parseInt(a) * Integer.parseInt(b.charAt(2) + ""));
		int four = (Integer.parseInt(a) * Integer.parseInt(b.charAt(1) + ""));
		int five = (Integer.parseInt(a) * Integer.parseInt(b.charAt(0) + ""));
		int six = (Integer.parseInt(a) * Integer.parseInt(b));
		
		System.out.println(three);
		System.out.println(four);
		System.out.println(five);
		System.out.println(six);
	}
}