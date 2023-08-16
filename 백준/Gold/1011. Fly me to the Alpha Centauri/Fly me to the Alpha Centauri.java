import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int caseNum = sc.nextInt();
		int start = 0;
		int end = 0;
		int length = 0;
		for (int i = 0; i < caseNum; i++) {
			start = sc.nextInt();
			end = sc.nextInt();
			length = end - start;
			f(length);
		}
		sc.close();
	}
	
	public static void f(int length) {
		int jump = 1;
		int rem = length;
		int count = 0;
		while (rem > jump * 2) {
			rem -= 2 * jump;
			jump++;
			count += 2;
		}
		if (rem > jump)
			count += 2;
		else
			count++;
		System.out.println(count);
	}
}