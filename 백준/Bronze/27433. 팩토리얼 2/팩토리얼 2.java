import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
        int n = Integer.parseInt(input);
        long res = 1; // int 범위 넘어가!!

        for (int i=1; i<n+1; i++) {
            res *= i;
        }
        System.out.println(res);
    }
}