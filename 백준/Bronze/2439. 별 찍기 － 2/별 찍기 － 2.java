import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		/** 별찍기1 */
//		for (int i=1; i<n+1; i++) {
//			String star = "*";
//			for (int k=0; k<i; k++) {
//				System.out.print(star);
//			}
//			System.out.println();
//		}
		
		/** repeat 사용 */
//		for (int i=1; i<n+1; i++) {
//			System.out.println("*".repeat(i));
//		}
		
		/** 별찍기2 */
		for (int i=1; i<n+1; i++) {
			System.out.println(" ".repeat(n-i)+"*".repeat(i));
		}
	}
}
