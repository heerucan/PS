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
//		for (int i=1; i<n+1; i++) {
//			System.out.println(" ".repeat(n-i)+"*".repeat(i));
//		}
		
		/** 별찍기3 */
//		for (int i=n; i>=1; i--) {
//			System.out.println("*".repeat(i));
//		}
		
		/** 별찍기4 */
//		for (int i=n; i>=1; i--) {
//			System.out.println(" ".repeat(n-i)+"*".repeat(i));
//		}
		
		/** 별찍기5 - 2442 */
//		for (int i=1; i<n+1; i++) {
//			System.out.println(" ".repeat(n-i)+"*".repeat(i)+"*".repeat(i-1));
//		}
		
		/** 별찍기6 - 2443 */
//		for (int i=n; i>=1; i--) {
//			System.out.println(" ".repeat(n-i)+"*".repeat(i)+"*".repeat(i-1));
//		}
		
		/** 별찍기7 - 2444 */
//		for (int i=1; i<n+1; i++) {
//			System.out.println(" ".repeat(n-i)+"*".repeat(i)+"*".repeat(i-1));
//		}
//		for (int i=n-1; i>=1; i--) {
//			System.out.println(" ".repeat(n-i)+"*".repeat(i)+"*".repeat(i-1));
//		}
		
		/** 별찍기8 - 2445 */
//		for (int i=1; i<n+1; i++) {
//			System.out.println("*".repeat(i)+" ".repeat(n-i)+" ".repeat(n-i)+"*".repeat(i));
//		}
//		for (int i=n-1; i>=1; i--) {
//			System.out.println("*".repeat(i)+" ".repeat(n-i)+" ".repeat(n-i)+"*".repeat(i));
//		}
		
		/** 별찍기9 - 2446 */
		for (int i=n; i>=1; i--) {
			System.out.println(" ".repeat(n-i)+"*".repeat(i)+"*".repeat(i-1));
		}
		for (int i=2; i<n+1; i++) {
			System.out.println(" ".repeat(n-i)+"*".repeat(i)+"*".repeat(i-1));
		}
	}
}
