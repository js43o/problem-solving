import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = Integer.parseInt(sc.nextLine());
		String[] strings = new String[n];
		for (int i = 0; i < n; i++)
			strings[i] = sc.nextLine();
		sc.close();
		int count = 0;
		for (int i = 0; i < strings.length; i++) {
			Set<Character> set = new HashSet<Character>();
			for (int j = 0; j < strings[i].length(); j++)	// 포함된 문자 저장
				set.add(strings[i].charAt(j));
			Character[] arr = new Character[set.size()];	// set을 array로 변환
			arr = set.toArray(arr);
			boolean test = true;
			for (int j = 0; j < arr.length; j++) {
				int first = strings[i].indexOf(arr[j]);
				int last = strings[i].lastIndexOf(arr[j]);
				String str = strings[i].substring(first, last + 1);
				for (int k = 0; k < str.length(); k++)
					if (str.charAt(k) != arr[j])
						test = false;
			}
			if (test)
				count++;
		}
		System.out.print(count);
	}
}