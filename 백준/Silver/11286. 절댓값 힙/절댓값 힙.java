import java.util.*;
import java.io.*;

/**
 * 11286 절댓값 힙
 * 메모리 : 
 * 시간 : 
 * 생각과정
 * 1. 힙 구현
 * 2. 절댓값과 진짜값을 넣어
 */

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		// 절댓값힙
		PriorityQueue<int[]> absHeap = new PriorityQueue<int[]>(new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) { // 0이 절댓값, 1이 진짜값
				// 절댓값으로 비교해서 출력
				// 근데 절댓값이 같으면 -> 실제값이으로 비교해서 출력
				if (o1[0] == o2[0]) {
					return Integer.compare(o1[1], o2[1]);
				} else {
					return Integer.compare(o1[0], o2[0]);	
				}
			}
		});
		
		List<Integer> result = new ArrayList<Integer>();
		
		for (int i=0; i<n; i++) {
			int x = Integer.parseInt(br.readLine());
			if (x==0) {
				if (!absHeap.isEmpty()) {
					result.add(absHeap.poll()[1]);
					continue;
				}
				result.add(0);
			} else {
				int[] temp = new int[2];
				temp[0] = Math.abs(x);
				temp[1] = x;
				
				absHeap.add(temp);
			}
		}
		
		for (int i=0; i<result.size(); i++) {
			System.out.println(result.get(i));
		}
	}

}
