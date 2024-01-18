import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String line = br.readLine();
        if (line.equals(" ")) {
            System.out.println(0);
        } else {
            String[] words = line.trim().split(" ");
            System.out.println(words.length);
        }
    }
}