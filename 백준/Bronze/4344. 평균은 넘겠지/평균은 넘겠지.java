import java.util.Scanner;
import java.util.Vector;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Vector<Double> vectorOfCase = new Vector<Double>();
		int numberOfCase = sc.nextInt();
		for (int i = 0; i < numberOfCase; i++) {
			Vector<Integer> vectorOfStudent = new Vector<Integer>();
			double average = 0;
			int numberOfStudent = sc.nextInt();
			for (int j = 0; j < numberOfStudent; j++) {
				int score = sc.nextInt();
				average += score;
				vectorOfStudent.add(score);
			}
			average /= numberOfStudent;
			double OK = 0;
			for (int j = 0; j < numberOfStudent; j++)
				if (vectorOfStudent.elementAt(j) > average)
					OK++;
			OK = (OK / numberOfStudent) * 100;
			vectorOfCase.add(OK);
		}
		sc.close();
		for (int i = 0; i < numberOfCase; i++)
			System.out.printf("%.3f%%%n", vectorOfCase.elementAt(i));
	}
}