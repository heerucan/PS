import java.io.*;
import java.util.*;

public class Main {
    static int N, M, K;
    static int[][] A;
    static int[][] rotateInfo;
    static boolean[] visited;
    static int[] order;
    static int ans = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        A = new int[N + 1][M + 1];
        rotateInfo = new int[K][3];
        visited = new boolean[K];
        order = new int[K];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= M; j++) {
                A[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            rotateInfo[i][0] = Integer.parseInt(st.nextToken());
            rotateInfo[i][1] = Integer.parseInt(st.nextToken());
            rotateInfo[i][2] = Integer.parseInt(st.nextToken());
        }

        permute(0);

        System.out.println(ans);
    }

    static void permute(int depth) {
        if (depth == K) {
            int[][] temp = copyArray(A);
            for (int i = 0; i < K; i++) {
                rotate(temp, rotateInfo[order[i]][0], rotateInfo[order[i]][1], rotateInfo[order[i]][2]);
            }
            ans = Math.min(ans, getMinValue(temp));
            return;
        }

        for (int i = 0; i < K; i++) {
            if (!visited[i]) {
                visited[i] = true;
                order[depth] = i;
                permute(depth + 1);
                visited[i] = false;
            }
        }
    }

    static int[][] copyArray(int[][] arr) {
        int[][] copy = new int[N + 1][M + 1];
        for (int i = 1; i <= N; i++) {
            System.arraycopy(arr[i], 0, copy[i], 0, M + 1);
        }
        return copy;
    }

    static void rotate(int[][] arr, int r, int c, int s) {
        for (int i = 1; i <= s; i++) {
            int startX = r - i;
            int startY = c - i;
            int endX = r + i;
            int endY = c + i;

            int temp = arr[startX][startY];

            for (int j = startX; j < endX; j++) {
                arr[j][startY] = arr[j + 1][startY];
            }
            for (int j = startY; j < endY; j++) {
                arr[endX][j] = arr[endX][j + 1];
            }
            for (int j = endX; j > startX; j--) {
                arr[j][endY] = arr[j - 1][endY];
            }
            for (int j = endY; j > startY + 1; j--) {
                arr[startX][j] = arr[startX][j - 1];
            }
            arr[startX][startY + 1] = temp;
        }
    }

    static int getMinValue(int[][] arr) {
        int min = Integer.MAX_VALUE;
        for (int i = 1; i <= N; i++) {
            int sum = 0;
            for (int j = 1; j <= M; j++) {
                sum += arr[i][j];
            }
            min = Math.min(min, sum);
        }
        return min;
    }
}
