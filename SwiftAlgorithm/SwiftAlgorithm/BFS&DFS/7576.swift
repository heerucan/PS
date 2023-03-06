//
//  7576.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/05.
//

import Foundation

let mn = readLine()!.split(separator: " ").map { Int(String($0))! }
let m = mn[0]
let n = mn[1]
// 그래프 다시 그려줘야 돼
var graph = [[Int]]()
var visited = Array(repeating: Array(repeating: false, count: m), count: n)

for _ in 0..<n {
    graph.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]

var answer = 0
var tomato = 0

var queue: [(Int, Int)] = []

for i in 0..<n {
    for j in 0..<m {
        // 그래프에 0이 없으면(안익은 토마토가 없으면) -> 0 출력
        if !graph[i].contains(0) {
            answer = 1 // 원래는 0을 출력하면 되는데 날짜개념상 첫 하루도 1일로 카운트되어서 1을 쳐줌
        } else { // 토마토 전체 개수를 구해~
            if graph[i][j] == 0 || graph[i][j] == 1 {
                tomato += 1
            }
            if graph[i][j] == 1 { // 좌표값이 1인 아이들의 x, y를 큐에 미리 넣어두기
                queue.append((i, j))
            }
        }
    }
}

var index = 0
// index가 queue.count보다 작을 때까지 돌려준다.
while index < queue.count {
    let newXY = queue[index]
    let x = newXY.0
    let y = newXY.1
    index += 1
    visited[x][y] = true

    for i in 0..<4 {
        let xx = x + dx[i]
        let yy = y + dy[i]
        
        if 0..<n ~= xx && 0..<m ~= yy {
            if !visited[xx][yy] && graph[xx][yy] == 0 {
                visited[xx][yy] = true
                graph[xx][yy] = graph[x][y] + 1
                queue.append((xx, yy))
                answer = graph[xx][yy]
            }
        }
    }
}

//# 모든 그래프 좌표 다 방문을 하면 False -> True로 방문처리가 될 것임
//# 그러면 그 뜻은 True인 것은 익은 토마토들이고, True 개수와 방문 전 1,0인 토마토 개수가 일치하는지 체크해줘야 함
//# 일치하면 다 방문했고, == 토마토가 다 익은 것임 // 일치하지 않으면 토마토가 익지 않은 게 있다는 뜻
var trueCount = 0
for i in 0..<n {
    for j in 0..<m {
        if visited[i][j] == true {
            trueCount += 1
        }
    }
}

if trueCount != tomato {
    print(-1)
} else {
    print(answer-1)
}
