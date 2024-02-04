
import java.io.*;
import java.math.BigInteger;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		// 조건 : 20 이하만 과정을 출
		if (n<=20) {
			// 이동횟수 규칙 = 2*n-1
			int cnt = (int) Math.pow(2, n)-1;
			System.out.println(cnt);
			hanoi(n,1,3,2);
		} else { // BigInteger - int, long 범위를 넘어가기 때문에 사용해야 함 
			BigInteger cnt = new BigInteger("2");
			System.out.println(cnt.pow(n).subtract(new BigInteger("1")));
		}
	}
	
	// circleNum개의 원반을 start에서 end로 옮겨 / other는 임시장판 
	// 1->2(n-1개의 원반이 이동) / 1->3(가장큰원반이 이동) / 2->3(마지막으로 n-1개의 원반들이 이동) 
	public static void hanoi(int circleNum, int start, int end, int other) {
		// 종료조건 : 원반이 1개면 항상 시작장대에서 마지막장대으로 
		if (circleNum==1) {
			System.out.println(start + " " + end);
			return;
		} else {
			// 1번에 있던 원반들 중 가장 아래 있는 원반을 제외하고 2번으로 이동 
			hanoi(circleNum-1, start, other, end);
			System.out.println(start + " " + end);
			// 2번에 있는 원반들을 3번으로 이동  
			hanoi(circleNum-1, other, end, start);
		}
	}
}
