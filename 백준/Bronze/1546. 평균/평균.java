import java.util.Collections;
import java.util.Scanner;
import java.util.Vector;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Vector<Integer> v = new Vector<Integer>();
		int count = sc.nextInt();
		int max = 0;
		for (int i = 0; i < count; i++) {
			int score = sc.nextInt();
			v.add(score);
			if (score > max)
				max = score;
		}
		sc.close();
		double total = 0;
		for (int i = 0; i < v.size(); i++)
			total += (v.elementAt(i).doubleValue() / max) * 100;
		System.out.println(total / v.size());
	}
}