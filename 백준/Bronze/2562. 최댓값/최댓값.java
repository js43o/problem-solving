import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] array = new int[9];
		int max = 0;
		int index = 0;
		for (int i = 0; i < 9; i++) {
			array[i] = sc.nextInt();
			if (array[i] >= max) {
				max = array[i];
				index = i;
			}
		}
		sc.close();
		System.out.print(array[index] + "\n" + (index + 1));
	}
}