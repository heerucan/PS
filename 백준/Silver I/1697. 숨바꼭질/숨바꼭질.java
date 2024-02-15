import java.util.*;
import java.io.*;

// bfs? 
// 이동 가능 범위 : +1, -1, +x

public class Main {
	
	static int n;
	static int k;
	static int seconds;
	static int[] graph;
	static boolean[] visited;
	static int[] dx;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());

		seconds = 1;
		graph = new int[100001];
		visited = new boolean[100001];
		dx = new int[3];
		bfs(); // n지점에서 시작!
		System.out.println(graph[k]);
	}

	public static void bfs() {
		Queue<Integer> queue = new LinkedList<>();
		queue.add(n);
		visited[n] = true;
		
		while (!queue.isEmpty()) {
			int node = queue.poll();
			dx = new int[]{node, 1, -1};

			for (int i=0; i<3; i++) {
				// xx가 항상 *2, +1, -1 순서로 가니까, 그 순서를 어떻게 바꿔주지?
				int xx = node + dx[i];
				
				if (xx < 0 || xx> 100000 || visited[xx]) {
					continue;
				}
				
				if (!visited[xx]) {
					queue.add(xx);
					graph[xx] = graph[node]+1;
					visited[xx] = true;
				}
			}
		}
	}
}
