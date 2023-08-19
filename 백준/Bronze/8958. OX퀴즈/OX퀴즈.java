import java.util.Scanner;
import java.util.Vector;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Vector<String> v = new Vector<String>();
		int count = sc.nextInt();
		sc.nextLine();
		for (int i = 0; i < count; i++)
			v.add(sc.nextLine());
		sc.close();

		for (int i = 0; i < v.size(); i++) {
			String str = v.elementAt(i);
			int score = 0;
			int total = 0;
			for (int j = 0; j < str.length(); j++)
				if (str.charAt(j) == 'O')
					total += ++score;
				else
					score = 0;
			System.out.println(total);
		}
	}
}