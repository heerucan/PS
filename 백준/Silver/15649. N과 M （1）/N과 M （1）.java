import java.util.*;
import java.io.*;

/**
 * 순열 - 순서 상관 있는, n까지 수 중 m개 고르기
 */

public class Main {

	static int n;
	static int m;
	static int[] arr;
	static boolean[] visited;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		visited = new boolean[n];

		arr = new int[m];
		dfs(0);
		System.out.println(sb);
	}

	public static void dfs(int level) {
		// 노드 탐색 깊이가 m가 같아지면 -> 출력 -> 종료 -> 이전 실행문인 visited[i]=false로 돌아가
		if (level == m) {
			for (int i: arr) {
				sb.append(i).append(" ");
			}
			sb.append("\n");
			return;
		}
		// 길이가 m보다 작으면 for문 실행
		for (int i = 0; i<n; i++) {
			if (!visited[i]) {
				visited[i] = true;
				arr[level] = i+1; // 1부터시작인데 idx가 0이라 1추가 
				dfs(level+1); // 노드 탐색하는 레벨 깊이+1 
				visited[i] = false; // 다시 조합을 찾아야 하니까 방문처리 해제
			}
		}
	}
}
