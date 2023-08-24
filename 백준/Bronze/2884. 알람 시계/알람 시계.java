import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] str = sc.nextLine().split(" ");
		sc.close();
		
		int hour = Integer.parseInt(str[0]);
		int minute = Integer.parseInt(str[1]);
		minute -= 45;
		if (minute < 0) {
			hour -= 1;
			minute += 60;
			if (hour < 0) {
				hour += 24;
			}
		}
		System.out.print(hour + " " + minute);
	}
}