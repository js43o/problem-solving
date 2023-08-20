import java.util.Scanner;
import java.util.Vector;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Vector<Integer> v = new Vector<Integer>();
		while (true) {
			String[] str = sc.nextLine().split(" ");
			if (str[0].equals("0") && str[1].equals("0"))
				break;
			else
				v.add(Integer.parseInt(str[0]) + Integer.parseInt(str[1]));
		}
		sc.close();
		for (int i = 0; i < v.size(); i++)
			System.out.println(v.elementAt(i));
	}
}