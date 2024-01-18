import java.util.stream.Stream;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        int c = Integer.parseInt(br.readLine());

        // a,b,c 받아서 곱해주고, 해당 결과를 숫자배열로 변환
        int num = a*b*c;
        int[] numArray = Stream.of(String.valueOf(num).split(""))
        .mapToInt(Integer::parseInt)
        .toArray();

        // 0~9까지 숫자 개수 카운트해줄 배열 생성
        int[] numCntArray = new int[10];
        
        // 0~9까지 a*b*c에 몇 개 있는지 numCntArray에 저장
        for (int i = 0; i < 10; i++) {
            for (int j=0; j<numArray.length; j++) {
                if (numArray[j] == i) {
                    numCntArray[i] += 1;
                }
            }
        }

        // 출력
        for (int i=0; i<numCntArray.length; i++) {
            System.out.println(numCntArray[i]);
        }
    }
}