import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
        // 행값은 고정이니까 5로 박고
        String[][] graph = new String[5][];

        for (int i = 0; i < graph.length; i++) {
            String line = br.readLine();
            graph[i] = new String[line.length()]; // 열 길이 

            // 열에 line 문자열의 j 인덱스 값을 받아서 문자열로 박아
            for (int j=0; j<line.length(); j++) {
                graph[i][j] = Character.toString(line.charAt(j));
            }
        }        

        // 어차피 열은 최대 15개니까
        for (int i = 0; i< 15; i++) {
            // 행만큼 돌아
            for (int j = 0; j< 5; j++) {
                // index error나면 for문 처음으로 이동
                try {
                    System.out.print(graph[j][i]);
                } catch(ArrayIndexOutOfBoundsException e) {
                    continue;
                }
            }
        }		
    }
}
