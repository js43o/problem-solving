import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int result = 0;
		if (n == 1 || n == 2 || n == 4 || n == 7)
			result = -1;
		else if (n == 3 || n == 5)
			result = 1;
		else if (n % 5 == 0)
			result = n / 5;
		else {
			int temp = n;	// n의 원본 값 저장.
			while (n > 0) {	// 3의 배수가 나올 때까지 5를 하나씩 뺀다.
				n -= 5;
				result++;
				if (n == 3 || n == 6 || n == 9 || n == 12) { // 더이상 5를 뺄 수 없는 경우.
					result += n / 3;
					break;
				}
			}
			if (n < 0)	// n이 3으로만 구성된 경우.
				result = temp / 3;
		}
		System.out.print(result);
	}
}