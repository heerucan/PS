import java.util.*;
import java.io.*;

/*
 * 최대 랜선 길이 구하기
 * N개의 같은 길이의 랜선으로 만들자!
 */
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int k = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[k];
		for (int i=0; i<k; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(arr);
		
		sb.append(binarySearch(arr, 1, arr[k-1], n));
		System.out.println(sb);
	}
	
	public static long binarySearch(int[] arr, long start, long end, int target) {
		long result = 0;
		while (start <= end) {
			long mid = (start+end)/2;
			long cnt = 0;
			for (int i: arr) {
				cnt += i/mid;
			}
			
			if (cnt >= target) {
				start = mid+1;
				result = mid;
			} else {
				end = mid-1;
			}
		}
		return result;
	}
}
