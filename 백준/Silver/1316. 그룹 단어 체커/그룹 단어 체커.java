import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String n = br.readLine();
        int intN = Integer.parseInt(n);
        int res = intN; // 반환할 결과값 (그룹단어 개수)

        for (int i=0; i<intN; i++) {
            String sentence = br.readLine();
            // 문자열로 받아서, 쪼개서 문자열 배열로
            String[] sArray = sentence.split("");
            // 해당 문자가 그룹단어인지 체크하기 위한 flag
            boolean flag = true;

            for (int j=0; j<sArray.length-1; j++) {
                // 현재값이 == 다음값 -> 넘겨 (체크할 필요 없으)
                if (sArray[j].equals(sArray[j+1])) {
                    continue;
                }
                
                // 현재값 != 다음값이면 체크해야 함
                // sArray[j] in sArray[j+1:] - 만약 있따? -> flag 변경
                // 자바에서는 in 이 없어서 배열로 돌려서 하나씩 비교해야함
                for (int k=j+1; k<sArray.length; k++) {
                    if (sArray[j].equals(sArray[k])) {
                        flag = false;
                        break;
                    }
                }
                
                // 마지막에 flag false면 -> 그룹단어 아니란 소리
                if (!flag) {
                    res--;
                    break;
                }
            }
        }
        System.out.println(res);
    }
}