
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 7569 토마토
 * @author 김루희
 * 메모리 : KB
 * 시간 : ms
 * 생각과정
 * 1. 위, 아래, 왼, 오, 앞, 뒤 6방향 
 * 2. 7576과 로직은 비슷한데, 그래프 만들 때만 주의하자 
 */

public class Main {

	static int m; // 가로 
	static int n; // 세로 
	static int h; // 높
	static int[][][] graph;
	static boolean[][][] visited;
	static Queue<int[]> queue = new LinkedList<>();

	static int[] dx = {-1,1,0,0,0,0};
	static int[] dy = {0,0,-1,1,0,0};
	static int[] dz = {0,0,0,0,1,-1}; //높이만 추가된  

	static int days; // 최소 날짜 
	static int total; // 처음 토마토 개수 총
	static int tomatos; // 토마토의 총합 

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		m = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		h = Integer.parseInt(st.nextToken());

		graph = new int[h][n][m];
		for (int i=0; i<h; i++) {
			
			for (int j=0; j<n; j++) {
				st = new StringTokenizer(br.readLine());
				for (int k=0; k<m; k++) {
					graph[i][j][k] = Integer.parseInt(st.nextToken());
					if (graph[i][j][k] == 0) {
						total++;
					} else if (graph[i][j][k] == 1) {
						total++;
						tomatos++;
						// 큐에 초기 익은 토마토의 좌표 추가하기 -> 이걸로 그래프 탐색할 것임 
						queue.add(new int[]{i,j,k});
					}
				}
			}
		}
		visited = new boolean[h][n][m];
		
		// 처음부터 다 익은 것 
		if (total == tomatos) {
			System.out.println(0);
		} else {
			bfs();

			// 탐색 후 익은 토마토 개수 = 방문처리된 것의 개수
			tomatos = 0;
			for (int i=0; i<h; i++) {
				for (int j=0; j<n; j++) {
					for (int k=0; k<m; k++) {
						if (visited[i][j][k]) {
							tomatos++;
						}
					}
				}
			}

			// 토마토가 모두 익었는지 체크하고 -> 영원히 못 익으면 -1 출력 		
			if (tomatos != total) {
				System.out.println(-1);
				return;
			} else {
				System.out.println(days-1);
				return;
			}
		}
	}

	public static void bfs() {
		while (!queue.isEmpty()) {

			int[] current = queue.poll();
			int x = current[0];
			int y = current[1];
			int z = current[2];
			visited[x][y][z] = true;

			for (int i=0; i<6; i++) {
				int xx = dx[i] + x;
				int yy = dy[i] + y;
				int zz = dz[i] + z;

				if (0>xx || xx>=h || 0>yy || yy>=n || 0>zz || zz>=m || visited[xx][yy][zz]) {
					continue;
				}

				if (0<=xx && xx<h && 0<=yy && yy<n && 0<=zz && zz<m && !visited[xx][yy][zz]) {
					if (graph[xx][yy][zz] == 0) {
						queue.add(new int[]{xx,yy,zz});
						visited[xx][yy][zz] = true;
						graph[xx][yy][zz] = graph[x][y][z] + 1;
						days = graph[xx][yy][zz];
					}					
				}
			}
		}
	}
}