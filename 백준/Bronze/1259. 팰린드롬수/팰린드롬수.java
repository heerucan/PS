import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// 0 나오기 전까지 체크
		while (true) {
			String nums = br.readLine();

			if (nums.equals("0")) {
				break;
			}

			char[] check = new char[nums.length()];
			char[] reverseCheck = new char[nums.length()];
			nums.toCharArray(); 

			String res = "yes";
			
			// 순방향 
			for (int i=0; i<nums.length(); i++) {
				check[i] = nums.charAt(i);
			}

			// 역방향
			for (int i = nums.length()-1; i >= 0; i--) {
				reverseCheck[nums.length()-1-i] = nums.charAt(i);
			}

			// 두개 비교
			for (int i = 0; i < nums.length(); i++) {
				if (!Character.toString(check[i]).equals(Character.toString(reverseCheck[i]))) {
					res = "no";
					break;
				}
			}

			System.out.println(res);
		}
	}
}
