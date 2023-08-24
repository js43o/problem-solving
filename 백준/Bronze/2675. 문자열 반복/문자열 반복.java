import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for (int i = 0; i < n; i++) {
			int iter = sc.nextInt();
			String str = sc.nextLine();
			str = str.substring(1, str.length());
			StringBuffer nStr = new StringBuffer();
			for (int j = 0; j < str.length(); j++)
				for (int k = 0; k < iter; k++)
					nStr.append(str.charAt(j));
			System.out.println(nStr);
		}
		sc.close();
	}
}