import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Set<Integer> set = new HashSet<Integer>();
		for (int i = 0; i < 10; i++)
			set.add(sc.nextInt() % 42); 
		sc.close();
		System.out.print(set.size());
	}
}