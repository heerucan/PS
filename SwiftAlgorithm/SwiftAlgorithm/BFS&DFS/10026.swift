//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/06.
//

import Foundation

let n = Int(readLine()!)!
var graph = Array(repeating: [String](), count: n)
for i in 0..<n {
    graph[i] = Array(readLine()!.map { String($0) })
}

var visited = Array(repeating: Array(repeating: false, count: n), count: n)

// dfs 사용해서 풀기
// 상하좌우 돌면서 나랑 같은 글자인 경우에만 방문
// 적록색약인 사람 -> 빨강을 다 초록으로 바꿔버리고 dfs
// 아닌 사람 -> 그냥 dfs

let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]

func dfs(_ x: Int, _ y: Int) {
    visited[x][y] = true
    
    for i in 0..<4 {
        let xx = x + dx[i]
        let yy = y + dy[i]
        
        if 0..<n ~= xx && 0..<n ~= yy {
            if graph[xx][yy] == graph[x][y] && !visited[xx][yy] {
                dfs(xx, yy)
            }
        }
    }
}


// 적록색약이 아닌 사람
var normal = 0
for i in 0..<n {
    for j in 0..<n {
        if !visited[i][j] {
            dfs(i, j)
            normal += 1
        }
    }
}

for i in 0..<n {
    for j in 0..<n {
        if graph[i][j] == "R" {
            graph[i][j] = "G"
        }
    }
}

// 재준이
var jaejun = 0
visited = Array(repeating: Array(repeating: false, count: n), count: n)

for i in 0..<n {
    for j in 0..<n {
        if !visited[i][j] {
            dfs(i, j)
            jaejun += 1
        }
    }
}

print(normal, jaejun)

//5
//RRRBB
//GGBBB
//BBBRR
//BBRRR
//RRRRR
