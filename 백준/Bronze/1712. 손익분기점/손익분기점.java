import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long a = sc.nextInt();
		long b = sc.nextInt();
		long c = sc.nextInt();
		sc.close();

		long ob = b;
		long oc = c;
		long count = 1;
		
		if (b >= c)
			System.out.print(-1);
		else {
			while (c <= a + b) {
				count++;
				b += ob;
				c += oc;
			}
			System.out.print(count);
		}
	}
}