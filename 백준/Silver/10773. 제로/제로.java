import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String input = br.readLine();
        int k = Integer.parseInt(input);

        // 수를 담을 스택
        ArrayList<Integer> stackArray = new ArrayList<>();

        for (int i=0; i<k; i++) {
            StringTokenizer x = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(x.nextToken());

            if (num==0) { // 0이면 stack.pop
                stackArray.remove(stackArray.size()-1);
            } else { // 그외 append
                stackArray.add(num);
            }
        }

        // 총합
        int res = 0;
        for (int x: stackArray) {
            res += x;
        }
        System.out.println(res);
     }   
}