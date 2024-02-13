import java.util.*;
import java.io.*;

/**
 * 과일 하나 먹으면 길이++
 * 과일 높이 h
 * 자신보다 작거나 같은 높이에 있는 과일을 먹을 수 있음
 * 처음 길이가 l일 때 - 과일들을 먹어 늘릴 수 있는 최대 길이??
 */

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken()); //과일의 개수
		int l = Integer.parseInt(st.nextToken()); //스네이크버드의 초기 길이
		
		int[] h = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<n; i++) {
			h[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(h);
		
		// 1 2 3 4 5 6 7 8 9
		for (int i=0; i<n; i++) {
			// 과일을 먹을 수 있으면 -> 먹고 길이 증가
			if (l >= h[i]) {
				l += 1;
			} else {
				break;
			}
		}
		System.out.println(l);
	}
}
