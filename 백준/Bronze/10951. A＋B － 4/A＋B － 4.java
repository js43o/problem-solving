import java.util.Scanner;
import java.util.Vector;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Vector<Integer> v = new Vector<Integer>();
		try {
			while (true) {
				String s = sc.nextLine();
				if (s.length() < 2)
					break;
				String[] str = s.split(" ");
				v.add(Integer.parseInt(str[0]) + Integer.parseInt(str[1]));
			}
		}
		catch (Exception e) {
			
		}
		sc.close();
		for (int i = 0; i < v.size(); i++)
			System.out.println(v.elementAt(i));
	}
}