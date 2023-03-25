//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/25.
//

import Foundation

/**
 7569 https://www.acmicpc.net/problem/7569
 - 익은놈들은 우선 큐에 넣고...
 - 익은 것들은 1, 안익은 것은 0, 없는 것은 -1
 - 다 못익으면 -1을 반환 / 이미 다 익엇으면 0 반환
 
 3중 for 문 -> o(n^^^3) 이 정도는 괜춘.. 100*100*100 이니까.
 */

let mnh = readLine()!.split(separator: " ").map { Int($0)! }
let m = mnh[0] // 가로칸 4
let n = mnh[1] // 세로칸 3
let h = mnh[2] // 쌓아올려지는 상자의 수 2 - z축임

var graph = Array(repeating: Array(repeating: Array(repeating: Int(), count: m), count: n), count: h)
var visited = Array(repeating: Array(repeating: Array(repeating: false, count: m), count: n), count: h)

// (h, n, m)
/*
 [
 [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], -> 0층 (첫 번째 박스)
 
 [[1, 1, 1, 1], [-1, -1, -1, -1], [1, 1, 1, -1]] -> 1층 (두 번째 박스)
 ]
 */


// 1. 이미 다 익엇어 -> 다 1이면 -> 0 반환 / 긍까, h*n*m 과 개수가 같아 -> 그러면 0반환
// 2. 1인 것의 좌표를 찾아서 큐에 미리 넣어!
// 3. 그래프를 돌면서 전체 그래프에서 토마토의 전체 개수를 구해서  --> 나중에 토마토 다 익었는지 비교해!

var answer = 0 // 최소일수 (답)
var queue: [(Int, Int, Int)] = [] // 큐


/// n개의 줄 반복을 h번 반복

for i in 0..<h {
    for j in 0..<n {
        graph[i][j] = readLine()!.split(separator: " ").map { Int($0)! }
        
        for k in 0..<m {
            if graph[i][j][k] == 1 { // 다 익은 것들의 좌표를 찾아서 queue에 먼저 넣자!
                queue.append((i, j, k))
            }
            
            if !graph[i][j].contains(0) { // 0을 아예 포함을 안해 -> 즉, 다 익은 토마토 뿐 -> 0 반환
                answer = 0
            }
        }
    }
}

// 큐를 돌려!!!
// 상 하 좌 우 앞(첫 번째 박스 기준) 뒤(첫 번째 박스 기준)
var dx = [-1, 1, 0, 0, 0, 0]
var dy = [0, 0, -1, 1, 0, 0]
var dz = [0, 0, 0, 0, -1, 1]

// 시간초과 때문에.. index가 queue의 개수보다 작을 때까지 while문 돌리는 것으로 해줘야 한다..
var index = 0
while index < queue.count {
    let newXYZ = queue[index]
    let x = newXYZ.0
    let y = newXYZ.1
    let z = newXYZ.2
    index += 1
    visited[x][y][z] = true
    
    for i in 0..<6 {
        let xx = x + dx[i]
        let yy = y + dy[i]
        let zz = z + dz[i]
        
        if 0 <= xx && xx < h && 0 <= yy && yy < n && 0 <= zz && zz < m {
            // 방문을 안했고, 익지 않은 토마토에 한해서!
            if !visited[xx][yy][zz] && graph[xx][yy][zz] == 0 {
                graph[xx][yy][zz] = graph[x][y][z] + 1
                queue.append((xx, yy, zz))
                answer = graph[xx][yy][zz] - 1 // 왜 1을 빼냐면,, 첫날 토마토가 있다는 표시의 1이 같이 계산됨
            }
        }
    }
}

// 시간이 지난 후 토마토가 다 익었나요?
graph.flatMap { $0.compactMap {
    if $0.contains(0) {
        // print("다 익지 않았어!")
        answer = -1
    }
}}

print(answer)
