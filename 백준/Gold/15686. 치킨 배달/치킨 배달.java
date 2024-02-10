
import java.util.*;
import java.io.*;

/**
 * 15686 치킨배달 
 * @author 김루희 
 * 메모리 : 16364KB
 * 시간 : 220ms
 * 생각과정
 * 1. n개 중 m개의 치킨집을 구하고, 그 조합들 중에서 치킨거리가 가장 작을 치킨집을 구하자!
 * 2. 즉, 조합! backtracking - 순열안됨 -> start, level 매개변수로 받자
 * 3. 
 */

public class Main {
	
	static int n;
	static int m;
	static int[][] graph;
	static boolean[] visited;
	static int[][] home;
	static int[][] chicken;	
	static int totalChickenDistance = Integer.MAX_VALUE; // 도시의 치킨거리 총합

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		int homeCnt = 0;
		int chickenCnt = 0;
		
		// 그래프 입력 받기 + 치킨집 개수, 집 개수 체크하기 - 배열 만들려고 
		graph = new int[n][n];
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<n; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				if (graph[i][j] == 1) { // 집 
					homeCnt++;
				} else if (graph[i][j] == 2) { // 치킨 
					chickenCnt++;
				}
			}
		}
		
		// 집과 치킨집의 좌표를 저장할 배열 
		home = new int[homeCnt][2];
		chicken = new int[chickenCnt][2];
		
		homeCnt = 0;
		chickenCnt = 0;
		
		// 집, 치킨집 좌표 저장 
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (graph[i][j] == 1) { // 집 
					home[homeCnt][0] = i;
					home[homeCnt][1] = j;
					homeCnt++;
				} else if (graph[i][j] == 2) { // 치킨 
					chicken[chickenCnt][0] = i;
					chicken[chickenCnt][1] = j;
					chickenCnt++;
				}
			}
		}
		visited = new boolean[chicken.length];
		
		backtracking(0,0);
		System.out.print(totalChickenDistance);
	}
	
	// 치킨집의 배열을 따로 만들어서 거기서 탐색하는 것 같
	public static void backtracking(int level, int start) {
		if (level==m) { // m개를 선택했으면 멈춰!			
			
			int total = 0;
			
			// 해당 m개의 치킨집 좌표를 기준으로 집과의 거리를 계산
			for (int i=0; i<home.length; i++) {
				int distance = 0; 
				int chickenDistance = Integer.MAX_VALUE;
				for (int j=0; j<chicken.length; j++) {
					if (visited[j]) { // 방문한 것은 = 선택한 치킨집 좌표 	
						// 집 - 치킨집 사이의 거리 
						distance = Math.abs(home[i][0]-chicken[j][0]) + Math.abs(home[i][1]-chicken[j][1]);
						// 치킨집 최소 거리 
						chickenDistance = Math.min(chickenDistance, distance);
					}
				}
				// 각각의 치킨집의 최소 거리를 합해줌 
				total += chickenDistance;
			}	
			// 모든 치킨집의 최소거리를 구하는데 최소여야 하니까 비교를 통해 더함 
			totalChickenDistance = Math.min(total, totalChickenDistance);
			return;
		}
		
		// 조합을 통해 치킨집 중에서 m개를 골라 
		for (int i=start; i<chicken.length; i++) {
			if (!visited[i]) {
				visited[i] = true;
				backtracking(level+1, i+1);
				visited[i] = false;
			}
		}
	}
}
