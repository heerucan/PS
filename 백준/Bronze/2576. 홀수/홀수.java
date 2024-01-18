import java.io.*;
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
				
		int sum = -1;
		int minValue = 100;
		
		try {
			for(int i=0; i<7; i++) {
				int n = Integer.parseInt(br.readLine());
				if (n%2!=0) {
					sum += n;
					if (minValue >= n) {
						minValue = n;
					}
				}
			}
			
			if (sum!=-1) {
				sum += 1;
				bw.write(sum +"\n"); //아스키코드로 넘어가서 문자열 처리를 해줘야 함
				bw.write(minValue+"");
			} else if (sum==-1) {
				bw.write(sum +"\n");
			}
			
			bw.flush();
			bw.close();
			
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
