//
//  9663.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/24.
//

import Foundation

/*
 NQueen : 무조건 한 행에 하나씩만 놓인다. -> 왜냐하면, 그게 조건임
 퀸이 놓인 곳의 같은 행/열에 놓이면 안되고, 대각선도 안된다.
 그래서 2차원 배열로 만들지 않고, 1차원 배열로 만들어도 된다.
 */

let n = Int(readLine()!)!
var cnt = 0
// 가로줄에 대한 변수
var horizon = Array(repeating: false, count: n)
// 서로 반대 방향의 대각선을 체크하기 위한 변수
// 대각선의 개수는 2n-1개로 동일하다. 각각
// 왼쪽상단에서 오른쪽하단 대각선은 x-y 차가 같다. 대신 대각선의 위치에 따라 값이 달라진다.
// -3, -2, -1, 0, 1, 2, 3으로 달라져서 0~6으로 값을 바꾸려면 n-1을 더해준다.
var leftToRight = Array(repeating: false, count: 2*n-1)
// 오른쪽상단에서 왼쪽하단 대각선은 x+y 합이 같다.
var rightToLeft = Array(repeating: false, count: 2*n-1)

// 한정조건 : 무조건 한 행/열에 하나씩, 서로 대각선에 붙어선 안된다.
// 재귀탈출 : 퀸 개수가 n인 경우 탈출!

// 시작하는 인덱스, 하나씩 증가해서 이전 것은 갖지 않고
// row가 커질수록 그 다음 단계 검사

func backtrack(_ row: Int) {
    if row == n { // 재귀탈출
        cnt += 1
        return
    }
    
    // column을 열이라고 생각 column = 0, row = 0 즉, (0,0)부터 퀸을 두면서 체크 시작
    // 1열의 각 행에 퀸을 넣고 재귀함수를 통해 나머지 퀸의 자리를 확인하는 것
    // backtrack(0) -> horizon[0], rightToLeft[0], leftToRight[3]
    for column in 0..<n {
        if !horizon[column] && !rightToLeft[column+row] && !leftToRight[column-row+(n-1)] {
            horizon[column] = true
            rightToLeft[column+row] = true
            leftToRight[column-row+(n-1)] = true
            backtrack(row+1)
            horizon[column] = false
            rightToLeft[column+row] = false
            leftToRight[column-row+(n-1)] = false
        }
    }
    
}

backtrack(0)
print(cnt)
