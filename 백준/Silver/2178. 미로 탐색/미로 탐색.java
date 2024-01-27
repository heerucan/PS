import java.util.*;
import java.io.*;

public class Main {

    static int[] dx = { -1, 1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };
    static int n;
    static int m;
    static int[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken()); // 행 x좌표
        m = Integer.parseInt(st.nextToken()); // 열 y좌표
        graph = new int[n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                graph[i][j] = line.charAt(j) - '0';
            }
        }

        // 0,0좌표부터 bfs의 큐에 삽입
        bfs(0, 0);
        System.out.println(graph[n - 1][m - 1]); // 가장 마지막 - 우하단 좌표가 곧, 최종적인 거리
    }

    // 최단경로 -> BFS를 통해 탐색!
    public static void bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] { x, y });

        while (!queue.isEmpty()) {
            // 큐에서 탐색할 것을 pop해줌
            int[] current = queue.poll();
            x = current[0];
            y = current[1];

            for (int i = 0; i < 4; i++) {
                int xx = dx[i] + x;
                int yy = dy[i] + y;

                if (0 > xx || n <= xx || 0 > yy || m <= yy) {
                    continue;
                }

                if (graph[xx][yy] == 0) {
                    continue;
                }

                // 그래프 이동할 수 있는 공간이면서, 이동 칸인 1일 때
                if (0 <= xx && xx < n && 0 <= yy && yy < m && graph[xx][yy] == 1) {
                    // 큐에 넣고
                    queue.add(new int[] { xx, yy });
                    // 이동횟수 추가
                    graph[xx][yy] = graph[x][y] + 1;
                }
            }
        }
    }
}
