import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(br.readLine());

        int hour = a;
        int minute = b;

        minute = (b+c)%60;
        hour = (a+(b+c)/60)%24;

        bw.write(hour+" "+minute);
        bw.flush();
        bw.close();
    }
}