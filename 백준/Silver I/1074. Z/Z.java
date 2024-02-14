import java.util.*;
import java.io.*;

/**
 * 1074 
 * @author 김루희
 * 메모리 : 14268KB
 * 시간 : 124ms
 * 생각과정은 주석으로...
 * 1. 배열이 아닌 길이로 접근한다.
 */

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());

		// 규칙? 반갈 시의 시작지점 - 0, 4**(n-1), 4**(n-1)*2, 4**(n-1)*3
		// 차례대로 0행 0열 - 0행 N/2열 - N/2행 0열 - N/2행 N/2열

		// 반갈죽해서 r,c가 어느 사분면에 위치해있는지 알고
		// 시작좌표를 체크 (해당 지점의 값까지) 

		// while문을 돌면서 가장 어느 사분면에 위치하는지 찾아야 하고, 계속 쪼개고 쪼개서 들어가기 위해
		// x,y를 두고 값을 갱신해준다. 계속 어느 분면에 위치하는지 체크
		// 언제까지? -> 더 이상 한 변을 쪼갤 수 없을때까지 - 즉, 변 길이가 1이 되면 STOP
		int side = (int) Math.pow(2, n); // 정사각형 한 변의 길이
		int halfSide = side; // 한 변의 절반 길이
		int x = 0;
		int y = 0;
		int len = 0; // 결과를 알기 위한 길이 - 시작지점
				
		while (halfSide > 1) {

			halfSide /= 2;

			// 어느 사분면에 위치하는지 코드 작성
			if (r<x+halfSide && c<y+halfSide) { //1분면
				len += 0;
			} else if (r<x+halfSide && c>=y+halfSide) { //2분면
				y += halfSide;
				len += halfSide*halfSide;
			} else if (r>=x+halfSide && c<y+halfSide) { //3분면
				x += halfSide;
				len += halfSide*halfSide*2;
			} else if (r>=x+halfSide&& c>=y+halfSide) { //4분면
				x += halfSide;
                y += halfSide;
				len += halfSide*halfSide*3;
			}

			if (r == x && c == y) { // 내가 찾는 r행c열일 경우 break
				break;
			}
		}    
		System.out.println(len);
	}
}

