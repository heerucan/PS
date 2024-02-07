import java.util.*;
import java.io.*;

public class Solution {
	
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	static int[][] graph;
	static boolean[][] visited;
	static int maxVal;
	static int minIdx;
	static int result;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());		
		
		for (int t=1; t<=T; t++) {
			int n = Integer.parseInt(br.readLine());
			graph = new int[n][n];
			visited = new boolean[n][n];
			
			// 그래프 값 받기
			for (int x=0; x<n; x++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int y=0; y<n; y++) {
					graph[x][y] = Integer.parseInt(st.nextToken());
				}
			}
			
			// 구현
			// 이동하려는 방에 적힌 숫자가 현재 방숫자보다 정확히 1 더 커야 이동가능
			// Max 만들어서 체크
			minIdx = Integer.MAX_VALUE;
			maxVal = Integer.MIN_VALUE;
			List<Integer> temp = new ArrayList<Integer>();
			for (int x=0; x<n; x++) {
				int cnt = 0; // 방개수
				for (int y=0; y<n; y++) {
					int[] start = {x,y};
					if (!visited[x][y]) {
						cnt = bfs(start,n);
						// 더 큰 방문개수를 기록한다
						maxVal = Math.max(maxVal, cnt); 
					}
				}
			}
			
			// maxVal와 같은 방의 개수를 가진 좌표를 배열에 담아서
			for (int x=0; x<n; x++) {
				int cnt = 0; // 방개수
				for (int y=0; y<n; y++) {
					int[] start = {x,y};
					if (visited[x][y]) {
						cnt = bfs(start,n);
						if (maxVal == cnt) {
							temp.add(graph[x][y]);
						}
					}
				}
			}
			
			// 이 배열에서 가장 적은 값을 minIdx에 담는다.
			for (int i: temp) {
				minIdx = Math.min(minIdx, i);
			}
			
			// 출력 - 처음출발방번호 최대몇개방이동 가능한지
			System.out.printf("#%d %d %d \n", t, minIdx, maxVal);
		}
	}
	
	// 그래프를 탐색하고 방개수 카운트할 용도
	// 시작좌표, 그래프크기
	public static int bfs(int[] start, int n) {
		// 방문가능 방의 개수
		int cnt = 1;
		
		// 큐에 시작 루트노드 좌표 추가
		Queue<int[]> queue = new LinkedList<>();
		queue.offer(start);
			
		// 방문처리
		visited[start[0]][start[1]] = true;
		
		// 큐가 빌 때까지 도는데
		// 해당 노드 기준 사방탐색을 한 번 해주고 -> 카운트 끝 -> 새로운 좌표 탐색
		while (!queue.isEmpty()) {
			// 큐에서 값을 빼서 그 아이 기준으로 탐색해
			int[] node = queue.poll();
			
			for (int i=0; i<4; i++) {
				int xx = dx[i] + node[0];
				int yy = dy[i] + node[1];
				
				// 탐색할 것의 조건
				// 1. 방문 안한 것
				// 2. 내것보다 +1 큰 것
				// 3. 범위 내의 것
				if (0<=xx && xx<n && 0<=yy && yy<n) {
					if (graph[xx][yy] == graph[node[0]][node[1]] + 1) {
						// 개수 +1
						cnt += 1;
						// 큐에 넣어줘야 함
						int[] newStart = {xx,yy};
						queue.add(newStart);
						visited[xx][yy] = true;
					}
				}
			}
		}
		// 한 번 탐색 시 방문 가능한 방개수를 반환
		return cnt;
	}
}
