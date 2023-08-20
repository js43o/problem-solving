import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] str = sc.nextLine().split(" ");
		int n = Integer.parseInt(str[0]);
		int x = Integer.parseInt(str[1]);
		int[] array = new int[n];
		for (int i = 0; i < n; i++)
			array[i] = sc.nextInt();
		sc.close();
		for (int i = 0; i < n; i++)
			if (x > array[i])
				System.out.print(array[i] + " ");
	}
}