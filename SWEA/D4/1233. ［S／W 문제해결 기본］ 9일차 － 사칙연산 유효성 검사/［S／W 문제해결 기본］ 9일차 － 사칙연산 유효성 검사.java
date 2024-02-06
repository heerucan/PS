
import java.util.*;
import java.io.*;

/**
 * SW1233 D4
 * @author 김루희
 * 생각과정
 * 1. 자식노드 둘 중 하나는 무조건 숫자다
 * 2. 리프노드는 무조건 숫자여야 한다
 * 3. 정점이 연산자가 아닌데 -> 자식이 연산자인 경우 x
 * 4. 정점이 숫자노드는 자식노드 가지면 안됨
 */
public class Solution {

	public static void main(String[] args) throws IOException {
		
		List<String> operators = new ArrayList<String>();
		operators.add("+");
		operators.add("-");
		operators.add("/");
		operators.add("*");
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		for (int t=0; t<10; t++) {
			// 첫번째 케이스의 양만큼 입력받기
			int res = 1;
			int n = Integer.parseInt(br.readLine());
			for (int i=0; i<n; i++) {
				// 1 - 2 3 => 1번노드에 (-)연산자, 2번노드가 왼쪽자식, 3번노드가 오른쪽자식
				List<String> arr = new ArrayList<String>();
				arr.add(br.readLine());
				
				String[] input = arr.get(0).split(" ");
				int root = Integer.parseInt(input[0]); // 루트노드
				String operator = input[1]; // 연산자

				// 입력에서 지금 문제가 있음. 입력 단위를 잘 받아주면 될 것 
				// 리프노드는 무조건 숫자여야 함, 연산자면 안됨
				int leaf = n/2+1;
				
				if (root>=leaf) {
					if (operators.contains(operator)) {
						res = 0;
						continue;
					}
				}
			}
			System.out.printf("#%d %d", t+1, res);
			System.out.println();
		}
	}
}