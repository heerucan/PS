package Algo;

import java.util.*;
import java.io.*;

/**
 * D3 5215
 * @author 김루희
 * 생각과정
 * 1. 정해진 칼로리 이하 조합 중 - 민기가 가장 선호하는 햄버거! 조합
 * 2. 조합 - 백트래킹 사용하자
 */

public class SW5215 {

    static int n; // 재료의 수
    static int l;  // 제한칼로리
    static int[][] ingredients; // 음식재료 담을 배열
    static int maxVal; // 점수 결과 담을 변수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        
        for (int t=0; t<T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            l = Integer.parseInt(st.nextToken());

            maxVal = 0;

            // [맛점수, 칼로리]를 담는 2차원 배열
            ingredients = new int[n][2];

            for (int i=0; i<n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j=0; j<2; j++) {
                    ingredients[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            // 조합 진행
            backtracking(0,0,0);
            System.out.printf("#%d %d \n", t+1, maxVal);
        }
    }

    public static void backtracking(int level, int calorie, int score) {
        // 종료조건 : 탐색횟수
        if (level == n) {
            // 제한 칼로리 합이 l 초과하면 스탑
            if (calorie > l) return;

            // calorie의 조건이 맞는 와중에 점수 조합이 가장 큰 경우를 추출
            maxVal = Math.max(maxVal, score);
            return;
        }
        
        backtracking(level+1, calorie+ingredients[level][1], score+ingredients[level][0]);
        backtracking(level+1, calorie, score);
    }    
}
