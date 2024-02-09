import java.util.*;
import java.io.*;

// [[], [], [] ... ] 그래프의 각 인덱스에 연결된 노드 번호를 추가 
// 1번째 인덱스에는 1번과 연결된 노드의 번호 추가!!
// [[], [2,3,4], [1,4], [1,4], [1,2,3]] 

public class Main {
	
	static ArrayList<ArrayList<Integer>> graph;
	static boolean[] visited;
	static Queue<Integer> queue;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int v = Integer.parseInt(st.nextToken());
		
		graph = new ArrayList<>(n+1); // 0번 인덱스는 사용X
		for (int i=0; i<=n; i++) {
			graph.add(new ArrayList<>());
		}
		visited = new boolean[n+1];
		queue = new LinkedList<>();
		
		for (int i=0; i<m; i++) {			
			st = new StringTokenizer(br.readLine());
			int node1 = Integer.parseInt(st.nextToken());
			int node2 = Integer.parseInt(st.nextToken());
			
			graph.get(node1).add(node2);
			graph.get(node2).add(node1);
		}
		
		for (ArrayList<Integer> nodes: graph) {
			Collections.sort(nodes);
		}
		
		dfs(v);
		System.out.println();
		bfs(v);
	}
	
	public static void dfs(int x) {
		visited[x] = true;
		System.out.print(x + " ");
		
		for (int i: graph.get(x)) {
			if (!visited[i]) {
				dfs(i);
			}
		}
	}
	
	public static void bfs(int x) {
		queue.offer(x);
		visited[x] = false;
		
		while (!queue.isEmpty()) {
			x = queue.poll();
			System.out.print(x + " ");
			
			for (int i: graph.get(x)) {
				if (visited[i]) {
					queue.offer(i);
					visited[i] = false;
				}
			}
		}
	}
}
