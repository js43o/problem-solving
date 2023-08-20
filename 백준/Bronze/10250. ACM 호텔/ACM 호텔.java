import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int caseNum = sc.nextInt();
		StringBuffer[] arr = new StringBuffer[caseNum];
		for (int i = 0; i < caseNum; i++) {
			int h = sc.nextInt();
			int w = sc.nextInt();
			int n = sc.nextInt();
			int ho = n / h + ((n % h == 0) ? 0 : 1);	// 1, 2, ... W
			int floor = n % h;	// 1, 2, 3 ... 0 (최상층)
			StringBuffer result = new StringBuffer();
			if (floor != 0)
				result.append(floor);
			else
				result.append(h);
			if (ho < 10)
				result.append("0" + ho);
			else
				result.append(ho);
			arr[i] = result;
		}
		for (int i = 0; i < arr.length; i++)
			System.out.println(arr[i]);
		sc.close();
	}
}