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
var graph = Array(repeating: 0, count: n)

// 한정조건 : 무조건 한 행/열에 하나씩, 서로 대각선에 붙어선 안된다.
// 재귀탈출 : 퀸 개수가 n인 경우 탈출!

// 시작하는 인덱스, 하나씩 증가해서 이전 것은 갖지 않고
// depth가 길어질수록

// 유망성 있는지 검사해주는 함수 -> 한정조건
func checkQueen(row: Int) -> Bool {
    for i in 0..<row {
        if graph[i] == graph[row] || abs(graph[row]-graph[i]) == abs(row-i) {
            return false
        }
    }
    return true
}


func backtrack(_ depth: Int) {
    if depth == n { // 재귀탈출
        cnt += 1
        return
    }
    
    for i in 0..<n {
        graph[depth] = i
        if checkQueen(row: depth) {
            backtrack(depth+1)
        }
    }
}

backtrack(0)
print(cnt)
