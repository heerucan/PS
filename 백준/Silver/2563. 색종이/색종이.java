import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int cnt = 0;
        // graph : false로 채워진 100*100 만들기
        boolean[][] graph = new boolean[100][100];
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                graph[i][j] = false;
            }
        }

        // 가로세로 크기가 10인 정사각형 붙이기

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int aa = a+10;
            int bb = b+10;

            for (int x = 0; x < 100; x++) {
                for (int y = 0; y < 100; y++) {
                    // 이미 붙인 영역은 pass
                    if (graph[x][y]) {
                        continue;
                    }
                    // 색종이 영역 체크 및 카운팅
                    if ((a <= x && x < aa) && (b <= y && y < bb)) {
                        graph[x][y] = true;
                        cnt += 1;
                    }
                }
            }
        }
        System.out.println(cnt);
    }
}
