public class Main {
	public static void main(String[] args) {
		for (int i = 1; i < 10000; i++) {
			boolean test = true;
			for (int j = 1; j <= i; j++)
				if (i == d(j))
					test = false;
			if (test)
				System.out.println(i);
			test = true;
		}
	}

	public static int d(int n) {
		int result = 0;
		if (n < 10) {
			result = n + n;
		}
		else if (n < 100) {
			result = n + (n / 10) + (n % 10);
		}
		else if (n < 1000) {
			result = n + (n / 100) + ((n / 10) - 10 * (n / 100)) + (n % 10);
		}
		else if (n < 10000) {
			result = n + (n / 1000) + ((n / 100) - 10 * (n / 1000)) + ((n / 10) - 10 * (n / 100)) + (n % 10);
		}
		return result;
	}
}