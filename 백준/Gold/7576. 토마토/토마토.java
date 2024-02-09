import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 7576
 * @author 김루희
 * 메모리 : 120816KB
 * 시간 : 728ms
 * 생각과정 
 * 1. 최소 날짜를 출력 = 최단 거리 구하듯이 날짜 체크 -> bfs
 * 2. 큐에 익은 토마토 위치부터 넣어주자 - 이걸 기준으로 탐색시작할 것임
 * 3. 사방탐색 진행 시에 0인 경우만 탐색하고 +1
 * 4. 기존 토마토 개수 == 익은 토마토 개수 체크하고 값 반환 
 * 
 * ++ 정적변수 선언해줬는데 새롭게 선언하고 있는지 확인하기
 * ++ 큐에 int[]로 제네릭타입 주면 됨 
 */

public class Main {

	static int m; // 가로 
	static int n; // 세로 
	static int[][] graph;
	static boolean[][] visited;
	static Queue<int[]> queue = new LinkedList<>();

	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};

	static int days; // 최소 날짜 
	static int total; // 처음 토마토 개수 총
	static int tomatos; // 토마토의 총합 

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		m = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());

		graph = new int[n][m];
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<m; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		visited = new boolean[n][m];
		
		// 전체 토마토 개수 - 1,0 | 익은 토마토 개수 - 1
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				if (graph[i][j] == 1) {
					tomatos++;
					total++;
					// 큐에 초기 익은 토마토의 좌표 추가하기 -> 이걸로 그래프 탐색할 것임 
					queue.add(new int[]{i,j});
				} else if (graph[i][j] == 0) {
					total++;
				}
			}
		}
		
		// 처음부터 토마토가 모두 이미 익은 상태면 -> 0 출력		
		if (tomatos == total) {
			System.out.println(0);
			return;
		} else {
			bfs();
			
			// 탐색 후 익은 토마토 개수 = 방문처리된 것의 개수
			tomatos = 0;
			for (int i=0; i<n; i++) {
				for (int j=0; j<m; j++) {
					if (visited[i][j]) {
						tomatos++;
					}
				}
			}
				
//			System.out.println("전체토마토개수 "+total + "| 익은 토마토개수 "+tomatos);
			
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
			visited[x][y] = true;
			
			for (int i=0; i<4; i++) {
				int xx = dx[i] + x;
				int yy = dy[i] + y;

				if (0>xx || xx>=n || 0>yy || yy>=m || visited[xx][yy]) {
					continue;
				}
				
				if (0<=xx && xx<n && 0<=yy && yy<m && !visited[xx][yy]) {
					if (graph[xx][yy] == 0) {
						queue.add(new int[]{xx,yy});
						visited[xx][yy] = true;
						graph[xx][yy] = graph[x][y] + 1;
						days = graph[xx][yy];
					}					
				}
			}
		}
	}
}
