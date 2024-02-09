import java.io.*;

public class Main {
    static int n;
    static char[][] graph;
    static boolean[][] visited;
    static int[] dx;
    static int[] dy;
    static int redGreen; // 적록색약인 사람의 구역수
    static int normal; // 아닌 사람의 구역수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        
        graph = new char[n][n];
        for (int i=0; i<n; i++) {
        	String letter = br.readLine();
            for (int j=0; j<n; j++) {
                graph[i][j] = letter.charAt(j);
            }
        }
        
        visited = new boolean[n][n];
        dx = new int[]{-1,1,0,0};
        dy = new int[]{0,0,1,-1};
        
        // 아닌 사람의 구역수
        normal = countRange(normal);
        
        // Red -> Green으로 변경해
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (graph[i][j] == 'R') {
                    graph[i][j] = 'G';
                }
            }
        } 
        
        // 방문배열 다시 원상태로 복구
        visited = new boolean[n+1][n+1];
        
        // 적록색약인 사람의 구역수
        redGreen = countRange(redGreen);  
        
        System.out.print(normal + " " + redGreen);
    }
    
    // 탐색하기 위한 메소드
    public static void dfs(int x, int y, char letter) {
        visited[x][y] = true;
        
        for (int i=0; i<4; i++) {
        	int xx = dx[i]+x;
        	int yy = dy[i]+y;
        	
        	if (0>xx || xx>=n || 0>yy || yy>=n || visited[xx][yy]) {
        		continue;
        	}
        	
        	if (0<=xx && xx<n && 0<=yy && yy<n && !visited[xx][yy]) {
        		if (graph[xx][yy] == letter) {
        			dfs(xx,yy,letter);
        		}
        	}
        }
    }
    
    // 구역 횟수 세는 함수 
    public static int countRange(int cnt) {
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (!visited[i][j]) {
                    dfs(i,j,graph[i][j]);
                    cnt += 1;
                }
            }
        }
        return cnt;
    }
}


