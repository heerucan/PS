import java.util.*;
import java.io.*;

public class Main {

	static int n;
	static int m;
	static int r;
	static int[][] graph;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken()); //x
		m = Integer.parseInt(st.nextToken()); //y
		r = Integer.parseInt(st.nextToken()); //회전수 

		graph = new int[n][m];

		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<m; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// 회전수만큼 회전시키
		for (int i=0; i<r; i++) {
			rotate();
		}

		// 출력 
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				System.out.print(graph[i][j] + " ");
			}
			System.out.println();
		}
	}

	// 회전메소드 
	static void rotate() {
		int squareNum = Math.min(n,m)/2; // 4행5열이면 -> 2
		for (int s=0; s<squareNum; s++) {
			// 왼쪽 꼭짓점 기억해두기
			int temp = graph[s][s];

			// 상 <-
			for (int i=s; i<m-1-s; i++) {
				graph[s][i] = graph[s][i+1];
			}

			// 우 (올리는거)
			for (int i=s; i<n-1-s; i++) {
				graph[i][m-1-s] = graph[i+1][m-1-s];
			}

			// 하 ->
			for (int i=m-s-1; i>s; i--) {
				graph[n-s-1][i] = graph[n-s-1][i-1];
			}

			// 좌 (내리는거)
			for (int i=n-1-s; i>s; i--) {
				graph[i][s] = graph[i-1][s];
			}

			graph[s+1][s] = temp; // 0,0 -> 1,0 담아주
		}
	}
}
