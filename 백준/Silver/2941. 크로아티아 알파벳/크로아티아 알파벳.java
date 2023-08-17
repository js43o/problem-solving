import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		sc.close();
		int count = 0;
		for (int i = 0; i < str.length(); i++) {
			switch (str.charAt(i)) {
			case 'c':
				if (i < str.length() - 1 && (str.charAt(i + 1) == '=' || str.charAt(i + 1) == '-')) {
					count++;
					i++;
				}
				else
					count++;
				break;
			case 'd':
				if (i < str.length() - 1 && (str.charAt(i + 1) == '-')) {
					count++;
					i++;
				}
				else if (i < str.length() - 2 && (str.charAt(i + 1) == 'z' && str.charAt(i + 2) == '=')) {
						count++;
						i += 2;
					}
				else
					count++;
				break;
			case 'l':
				if (i < str.length() - 1 && (str.charAt(i + 1) == 'j')) {
					count++;
					i++;
				}
				else
					count++;
				break;
			case 'n':
				if (i < str.length() - 1 && (str.charAt(i + 1) == 'j')) {
					count++;
					i++;
				}
				else
					count++;
				break;
			case 's':
				if (i < str.length() - 1 && (str.charAt(i + 1) == '=')) {
					count++;
					i++;
				}
				else
					count++;
				break;
			case 'z':
				if (i < str.length() - 1 && (str.charAt(i + 1) == '=')) {
					count++;
					i++;
				}
				else
					count++;
				break;
			default:
				count++;
				break;
			}
		}
		System.out.print(count);
	}
}