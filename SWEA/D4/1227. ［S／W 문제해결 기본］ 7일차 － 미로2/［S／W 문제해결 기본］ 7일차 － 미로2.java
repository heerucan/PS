import java.util.*;
import java.io.*;

public class Solution {

	static int[][] graph;
	static boolean[][] visited;
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	static int[] start = new int[2];
	static int[] end = new int[2];
	static int result;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for (int t=0; t<10; t++) {
			int T = Integer.parseInt(br.readLine());
			// 그래프 생성
			result = 0;
			visited = new boolean[100][100];
			graph = new int[100][100];
			for (int i=0; i<100; i++) {
				String line = br.readLine();
				for (int j=0; j<line.length(); j++) {
					graph[i][j] = line.charAt(j)-'0';
					if (graph[i][j] == 2) {
						start[0] = i;
						start[1] = j;
					} else if (graph[i][j] == 3) {
						end[0] = i;
						end[1] = j;
					}
				} 
			}

			// 2인 곳부터 시작
			bfs(start);
			
			if (visited[end[0]][end[1]]) { // end좌표를 방문했다면 -> 1
				result = 1;
			} else {
				result = 0;
			}
			System.out.printf("#%d %d\n", T, result);
		}
	}

	public static void bfs(int[] start) {
		Queue<int[]> queue = new LinkedList<>();
		queue.offer(start);
		visited[start[0]][start[1]] = true;
		
		while (!queue.isEmpty()) {
			int[] current = queue.poll();
			int x = current[0];
			int y = current[1];
			 
			for (int i=0; i<4; i++) {
				int xx = dx[i]+x;
				int yy = dy[i]+y;
				
				if (xx < 0 || xx >= 100 || yy <0 || y>= 100) {
					continue;
				}
				
				if (visited[xx][yy] || graph[xx][yy] == 1) {
					continue;
				}
				
				if (0<=xx && xx<100 && 0<=yy && yy<100) {
					if (!visited[xx][yy] && graph[xx][yy] != 1) {
						visited[xx][yy] = true;
						int[] temp = new int[2];
						temp[0] = xx;
						temp[1] = yy;
						queue.offer(temp);
					}
				}
			}
		}
	}
}
