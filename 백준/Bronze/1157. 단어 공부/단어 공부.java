import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[26];
		StringBuffer str = new StringBuffer(sc.nextLine());
		sc.close();
		for (int i = 0; i < str.length(); i++) {
			int ch = str.charAt(i);
			if (ch >= 'a')
				ch -= 32;
			arr[ch - 'A']++;
		}
		int maxNum = 0;
		char maxChar = 0;
		for (int j = 0; j < arr.length; j++)
			if (arr[j] > maxNum) {
				maxNum = arr[j];
				maxChar = (char) (j + 'A');
			}
		for (int k = 0; k < arr.length; k++)
			if (maxNum == arr[k] && maxChar != k + 'A')
				maxChar = '?';
		System.out.println(maxChar);
	}
}