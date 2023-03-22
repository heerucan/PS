//
//  6118.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/21.
//

import Foundation

// https://www.acmicpc.net/problem/6118 숨바꼭질 실버1

// bfs로 풀어야 하는 이유 - 재서기가 1번부터 가장 멀리 떨어진 헛간에 숨어야 하는데 그럴려면 1번 기준 가장 먼 곳을 찾아야 한다. 그 말은 각 좌표 별 최단거리를 의미하고, dfs로 풀 경우 깊이 우선 탐색이기 때문에 1-3-4로 가는 최단방법이 있음에도 1-2-3-4로 가는 경우도 생긴다.

let nm = readLine()!.split(separator: " ").map { Int($0)! }
let n = nm[0]
let m = nm[1]

var graph = Array(repeating: [Int](), count: n+1)
var visited = Array(repeating: false, count: n+1)

for _ in 0..<m {
    let ab = readLine()!.split(separator: " ").map { Int($0)! }
    let a = ab[0]
    let b = ab[1]
    graph[a].append(b)
    graph[b].append(a)
}

//[[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]

var queue: [Int] = []
var distance = Array(repeating: 0, count: n+1)

func bfs(_ x: Int) {
    visited[x] = true
    queue.append(x)
    
    while !queue.isEmpty {
        let x = queue.removeFirst()
        
        for i in graph[x] {
            if !visited[i] {
                visited[i] = true
                queue.append(i)
                distance[i] = distance[x] + 1
            }
        }
    }
}

// 그래프가 항상 어떤 걸로든 연결되어 있고, 끊겨있지 않다고 했음
// 1번 헛간부터 시작한다고 했음
for i in 1..<graph.count {
    if !visited[i] { // 방문 안한 곳들만
        bfs(i)
    }
}


// 가장 먼 곳 => 즉, 1. 최대값을 가진 가장 작은 인덱스 / 2. 거리 / 3. 같은 거리의 개수
var sortedDistance = distance.sorted()
let totalDistance = sortedDistance[distance.count-1]

var value = 0
for i in distance {
    if i == totalDistance {
        value += 1
    }
}
print(distance.firstIndex(of: totalDistance)!, totalDistance, value)
