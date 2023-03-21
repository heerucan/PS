//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/20.
//

import Foundation

// 17086번
// 아기상어랑 제일 멀리 떨어져 있는 칸이 있을 때 그 칸의 안전 거리를 구해라

// BFS.. 왜... 최단거리라서? 응..

let nm = Array(readLine()!.split(separator: " ").map { Int(String($0))! })
let n = nm[0]
let m = nm[1]

var graph = Array(repeating: Array(repeating: Int(), count: m), count: n)
var visited = Array(repeating: Array(repeating: false, count: m), count: n)
for i in 0..<n {
    graph[i] = readLine()!.split(separator: " ").map { Int(String($0))! }
}

var dx = [1, -1, 0, 0, -1, -1, 1, 1]
var dy = [0, 0, 1, -1, -1, 1, -1, 1]

var queue: [(Int, Int)] = []

for i in 0..<n {
    for j in 0..<m {
        // 아기상어 좌표를 먼저 큐에 넣는다.
        // 왜 넣냐면,, 그러게 왜 넣지..
        // 안전거리(최단거리) 긍까, 최단거리를 구하려면,, 결국에는 아기상어 기준으로 시작해야 한다..
        // 우선 먼저 그래프에다가 아기상어 기준으로 모든 좌표에 안전거리가 얼마나 나오는지 써보면 안다...
        if graph[i][j] == 1 {
            graph[i][j] = 0 // 왜 0으로 바꿧냐면,, 0으로 안바꾸면 아래에서 1 기준으로 최단거리 카운팅 시작함
            visited[i][j] = true
            queue.append((i, j))
        }
    }
}

while !queue.isEmpty {
    let (x, y) = queue.removeFirst()
    
    for i in 0..<8 {
        let xx = x + dx[i]
        let yy = y + dy[i]

        if 0 <= xx && n > xx && 0 <= yy && m > yy {
            if !visited[xx][yy] && graph[xx][yy] != 1 {
                visited[xx][yy] = true
                graph[xx][yy] = graph[x][y] + 1
                queue.append((xx, yy))
            }
        }
    }
}

// 안전거리 최댓값 구하기
func getMaxSafeDistance(_ graph: [[Int]]) {
    var arr = [Int]()

    graph.compactMap {
        $0.compactMap {
            arr.append($0)
        }
    }

    arr = arr.sorted(by: >)
    print(arr[0])
}

getMaxSafeDistance(graph)
