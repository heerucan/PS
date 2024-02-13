import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] input = new int[n];

		for (int i=0; i<n; i++) {
			input[i] = sc.nextInt(); //input에 입력 수를 저장
		}

		// 0. 오름차순 정렬
//		Arrays.sort(input);
		
		if (np(input)) {
			for (int i=0; i<n; i++) {
				System.out.print(input[i]+" ");
			}
		} else {
			System.out.println(-1);
		}	
	}

	// 순열의 뒷쪽부터 변화를 준다
	public static boolean np(int[] p) { // 현순열의 사전순 다음 순열 생성 (p:현재 순열의 상태) 
		final int n = p.length;
		// 1. 교환위치 찾기 (뒤쪽부터 꼭대기 찾으면 꼭대기 이전이 교환위치가 됨)
		int i = n-1; //맨뒤부터 탐색
		while(i>0 && p[i-1]>=p[i]) --i; // 나보다 앞 원소가 더 큰 경우 

		if (i==0) return false; // 현순열의 상태가 큰순열이므로 np 없다.

		// 2. 교환위치인 i-1에 넣을 값을 뒤쪽부터 찾기 (큰 값 중 최소값)

		int j = n-1;
		while (p[i-1]>=p[j]) --j; 

		// 3. 교환위치(i-1) 값과 찾은 위치(j)값 교환
		swap(p, i-1, j); // 배열의 참조를 보내줬기 때문에 swap이 유지

		// 4. 꼭대기(i)위치부터 맨뒤까지 오름차순 정렬
		int k = n-1;
		while (i<k) swap(p,i++,k--);

		return true;
	}

	public static void swap(int[] arr, int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
}
