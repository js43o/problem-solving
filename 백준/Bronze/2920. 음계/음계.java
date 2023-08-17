import java.util.Scanner;
import java.util.Vector;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Vector<Integer> v = new Vector<Integer>();
		Vector<Integer> t = new Vector<Integer>();
		for (int i = 0; i < 8; i++)
			v.add(sc.nextInt());
		sc.close();
		
		for (int i = 0; i < v.size() - 1; i++)
			t.add(v.elementAt(i) - v.elementAt(i + 1));

		if (isAscending(t))
			System.out.print("ascending");	
		else if (isDescending(t))
			System.out.print("descending");
		else
			System.out.print("mixed");
	}
	
	public static boolean isAscending(Vector<Integer> t) {
		boolean result = true;
		for (int i = 0; i < t.size(); i++)
			if (t.elementAt(i) != -1)
				result = false;
		return result;
	}
	
	public static boolean isDescending(Vector<Integer> t) {
		boolean result = true;
		for (int i = 0; i < t.size(); i++)
			if (t.elementAt(i) != 1)
				result = false;
		return result;
	}
}