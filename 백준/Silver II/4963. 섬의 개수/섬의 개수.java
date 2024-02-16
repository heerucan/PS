import java.util.*;
import java.io.*;

/**
 * 생각과정
 * 1. 팔방탐색
 */

public class Main {
	
	static int w;
	static int h;
	static int[] dx = new int[] {-1,1,0,0,-1,-1,1,1};
	static int[] dy = new int[] {0,0,-1,1,-1,1,1,-1};
	static boolean[][] visited;
	static int[][] graph;
	static int result;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			w = Integer.parseInt(st.nextToken()); // 너비 y
			h = Integer.parseInt(st.nextToken()); // 높이 x
					
			if (w==0 && h==0) {
				break;
			}
			
			visited = new boolean[h][w];
			graph = new int[h][w];
			for (int i=0; i<h; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j=0; j<w; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
				}
			}
						
			result = 0;
			for (int i=0; i<h; i++) {
				for (int j=0; j<w; j++) {
					if (!visited[i][j] && graph[i][j] == 1) {
						bfs(i,j);
						result += 1;
					}
				}
			}
			System.out.println(result);
		}
	}
	
	public static void bfs(int x, int y) {
		Queue<int[]> queue = new ArrayDeque<>();
		int[] start = new int[] {x,y};
		queue.offer(start);
		visited[x][y] = true;
		
		while (!queue.isEmpty()) {
			int[] current = queue.poll();
			
			for (int i=0; i<8; i++) {
				int xx = dx[i]+current[0];
				int yy = dy[i]+current[1];
				
				if (xx<0 || xx>=h || yy<0 || yy>=w || visited[xx][yy] || graph[xx][yy] == 0) {
					continue;
				}
				
				if (!visited[xx][yy] && graph[xx][yy] == 1) {
					visited[xx][yy] = true;
					int[] temp = new int[] {xx,yy};
					queue.offer(temp);
				}
			}
		}
	}
}
