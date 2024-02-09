package Algo;

import java.util.*;
import java.io.*;

/**
 * 모의 역량테스트 4012
 * @author 김루희
 * 메모리 : 22,880 kb
 * 시간 : 257 ms
 * 생각과정
 * 1. 조합으로 풀고! 종료조건은 탐색횟수가 n/2 됐을때!
 * 2. 방문탐색 배열로도 충분히 선택한 값을 체크할 수 있다!
 * 3. 순열 -> 시간초과
 * 4. 조합 -> start값의 변경이 필요하다!!!
 */

public class Algo4012 {

	static int n; // 식재료수
	static int[][] ingredients; // 식재료 담은 배열
	static boolean[] visited; // 방문처리 배열
	static int minVal; // a와b 음식 차이 값

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("src/Algo/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int t=0; t<T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());

			ingredients = new int[n][n];
			visited = new boolean[n]; 
			minVal = Integer.MAX_VALUE;

			for (int i=0; i<n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j=0; j<n; j++) {
					ingredients[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			// 조합 진행
			backtracking(0,0);
			System.out.printf("#%d %d", t+1, minVal);
			System.out.println();
		}
	}

	// 순열로 하면 시간초과 뜬다 - 조합으로 해야!!!!! 
	// 근데 조합일 경우 어떻게 하냐? -> start를 통해서 +1해주면서 이전 값 탐색안하게 하면 된다.
	public static void backtracking(int level, int start) {
		if (level == n/2) {
			// 2개 뽑은 거 -> visited로 체크
			int a = 0; // a총합
			int b = 0; // b총합

			// 2차원 배열 돌면서 방문처리 = A 라고 생각하고 음식값 추가해주기
			for (int i=0; i<n; i++) {
				for (int j=0; j<n; j++) {
					// A음식
					if (visited[i] && visited[j]) {
						a += (ingredients[i][j]);
					} else if (!visited[i] && !visited[j]) { // B음식
						b += (ingredients[i][j]);
					}
				}
			}	
			minVal = Math.min(minVal, Math.abs(a-b));
			return;
		}
		// 숫자 4개중에 2개를 뽑아!!!!
		for (int i=start; i<n; i++) {
			// 순열 말고 조합으로 풀고 있는지!!
			if (!visited[i]) {
				visited[i] = true;
				backtracking(level+1,i+1);
				visited[i] = false;
			}
		}

	}
}
