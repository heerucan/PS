import java.util.*;
import java.io.*;

public class Main {

	static int n;
	static int m;
	static int r;
	static int[][] graph;
	static int[][] newGraph;
	static int operator;
	static int max;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken()); //x
		m = Integer.parseInt(st.nextToken()); //y
		r = Integer.parseInt(st.nextToken()); //연산수 

		max = Math.max(n, m);
		graph = new int[n][m];
		newGraph = new int[m][n];

		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<m; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		List<Integer> input = new ArrayList<Integer>();
		st = new StringTokenizer(br.readLine());

		while (st.hasMoreTokens()) {
			input.add(Integer.parseInt(st.nextToken()));
		}

		// 연산횟수 및 연산방식에 따라 회전 
		for (int i=0; i<r; i++) {
			switch (input.get(i)) {
			case 1: one(); break;
			case 2: two(); break;
			case 3: three(); break;
			case 4: four(); break;
			case 5: five(); break;
			case 6: six(); break;
			}
		}
		
		// 마지막 연산방식에 따라서 출력 방식 변경 
		switch (input.get(r-1)) {
		case 1: printGraph(); break;
		case 2: printGraph(); break;
		case 3: printNewGraph(); break;
		case 4: printNewGraph(); break;
		case 5: printGraph(); break;
		case 6: printGraph(); break;
		}
	}

	public static void printGraph() {
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				System.out.print(graph[i][j] + " ");
			}
			System.out.println();
		}
	}

	public static void printNewGraph() {
		for (int i=0; i<newGraph.length; i++) {
			for (int j=0; j<newGraph[0].length; j++) {
				System.out.print(newGraph[i][j] + " ");
			}
			System.out.println();
		}
	}

	// 1번연산 - 상하 반전 
	public static void one() {
		for (int i=0; i<n/2; i++) {
			for (int j=0; j<m; j++) {
				int temp = graph[i][j];
				graph[i][j] = graph[n-1-i][j];
				graph[n-1-i][j] = temp;
			}
		}
	}

	// 2번연산 - 좌우 반전 
	public static void two() {
		for (int i=0; i<n; i++) {
			for (int j=0; j<m/2; j++) {
				int temp = graph[i][j];
				graph[i][j] = graph[i][m-1-j];
				graph[i][m-1-j] = temp;
			}
		}
	}

	// 3번연산 - 오른쪽으로 90도 회전 
	public static void three() {
		newGraph = new int[m][n];
		for (int i=0; i<m; i++) {
			for (int j=0; j<n; j++) {
				newGraph[i][j] = graph[n-1-j][i];
			}
		}
		graph = newGraph;
		int temp = n;
		n = m;
		m = temp;
	}

	// 4번연산 - 왼쪽으로 90도 회전
	public static void four() {
		newGraph = new int[m][n];
		for (int i=0; i<m; i++) { 
			for (int j=0; j<n; j++) {
				newGraph[i][j] = graph[j][m-1-i];
			}
		}
		graph = newGraph;
		int temp = n;
		n = m;
		m = temp;
	}

	//5번연산 
	public static void five() {
		// 2번그룹 저장 
		int[][] temp = new int[n/2][m/2];
		for (int i=0; i<n/2; i++) {
			for (int j=m/2; j<m; j++) {
				temp[i][j-m/2] = graph[i][j];
			}
		}

		//right 1->2
		for (int i=0; i<n/2; i++) {
			for (int j=0; j<m/2; j++) {
				graph[i][j+m/2] = graph[i][j];
			}
		}

		//up 4->1
		for (int i=n-1; i>=n/2; i--) {
			for (int j=0; j<m/2; j++) {
				graph[i-n/2][j] = graph[i][j];
			}
		}

		//left 3->4
		for (int i=n/2; i<n; i++) {
			for (int j=m-1; j>=m/2; j--) {
				graph[i][j-m/2] = graph[i][j];
			}
		}

		//temp에 저장해둔 2->3
		for (int i=n/2; i<n; i++) {
			for (int j=m/2; j<m; j++) {
				graph[i][j] = temp[i-n/2][j-m/2];
			}
		}
	}

	//6번연산 
	public static void six() {
		// 1번그룹 저장 
		int[][] temp = new int[n/2][m/2];
		for (int i=0; i<n/2; i++) {
			for (int j=0; j<m/2; j++) {
				temp[i][j] = graph[i][j];
			}
		}

		//left 2->1
		for (int i=0; i<n/2; i++) {
			for (int j=m/2; j<m; j++) {
				graph[i][j-m/2] = graph[i][j];
			}
		}

		//up 3->2
		for (int i=n-1; i>=n/2; i--) {
			for (int j=m-1; j>=m/2; j--) {
				graph[i-n/2][j] = graph[i][j];
			}
		}

		//right 4->3
		for (int i=n/2; i<n; i++) {
			for (int j=0; j<m/2; j++) {
				graph[i][j+m/2] = graph[i][j];
			}
		}

		//temp에 저장해둔 1->4
		for (int i=n/2; i<n; i++) {
			for (int j=0; j<m/2; j++) {
				graph[i][j] = temp[i-n/2][j];
			}
		}
	}
}
