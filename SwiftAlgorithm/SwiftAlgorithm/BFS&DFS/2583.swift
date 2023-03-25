//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/25.
//

import Foundation

/**
 2583 https://www.acmicpc.net/problem/2583
 1. 그래프를 그리자!
 2. 각 좌표를 받아서 범위 내에 있는 아이들을 다 방문처리를 시켜버리쟈!
 - (0,2) (4,4) 인 경우, 범위는 -> 0 <= x < 4 / 2 <= y < 4
 3. 그리고 dfs를 돌려서 영역값과, 영역의 너비를 구하자
 */

let mnk = readLine()!.split(separator: " ").map { Int($0)! }
let m = mnk[0] // y좌표 5
let n = mnk[1] // x좌표 7
var k = mnk[2]

var graph = Array(repeating: Array(repeating: 0, count: m), count: n)
var visited = Array(repeating: Array(repeating: false, count: m), count: n)


while k != 0 {
    let abcd = readLine()!.split(separator: " ").map { Int($0)! }
    let x1 = abcd[0]
    let y1 = abcd[1]
    let x2 = abcd[2]
    let y2 = abcd[3]
    
    for i in x1..<x2 { // 0<=  <4
        for j in y1..<y2 { // 2 <= < 4
            graph[i][j] = 1
        }
    }
    k -= 1
}

var dx = [-1, 1, 0, 0]
var dy = [0, 0, -1, 1]


var width = 1 // 각 영역의 크기는 항상 1이 기본값으로 시작

func dfs(_ x: Int, _ y: Int) {
        
    visited[x][y] = true
            
    for i in 0..<4 {
        let xx = x + dx[i]
        let yy = y + dy[i]
        
        if 0 <= xx && xx < n && 0 <= yy && yy < m {
            if !visited[xx][yy] && graph[xx][yy] == 0 {
                dfs(xx, yy)
                width += 1
            }
        }
    }
}

var total = 0 // 영역의 개수
var arr: [Int] = [] // 각 영역의 너비를 추가하기 위한 배열

for i in 0..<n {
    for j in 0..<m {
        if !visited[i][j] && graph[i][j] == 0 {
            width = 1 // 각 영역의 크기는 항상 1이 기본값으로 시작
            dfs(i, j)
            total += 1 // dfs에서 빠져나오는 순간에 -> 그래프가 끊긴 것이니까 1 추가
            arr.append(width)
        }
    }
}

arr = arr.sorted(by: <) // 오름차순 정렬을 위함


print(total)
arr.flatMap { print($0, terminator: " ") }
