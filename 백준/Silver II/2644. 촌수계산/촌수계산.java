import java.util.ArrayList;
import java.util.Scanner;

public class Main  {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int total = -1;
    static int n,a,b,m;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        a = scanner.nextInt();
        b = scanner.nextInt();
        m = scanner.nextInt();
        
        graph = new ArrayList[n + 1];
        visited = new boolean[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            graph[x].add(y);
            graph[y].add(x);
        }

        dfs(a, 0);
        System.out.println(total);
    }

    public static void dfs(int x, int depth) {
        visited[x] = true;

        if (x == b) {
            total = depth;
            return;
        }

        for (int i : graph[x]) {
            if (!visited[i]) {
                dfs(i, depth + 1);
            }
        }
    }
}
