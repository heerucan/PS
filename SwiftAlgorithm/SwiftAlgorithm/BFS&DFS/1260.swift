//
//  1260.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/03.
//

import Foundation


//n, m, v = map(int, input().split())
//
//g = [[0] * (n + 1) for _ in range(n + 1)]
//visited= [False] * (n+1)
//
//for _ in range(m):
//    a, b = map(int, input().split())
//    g[a][b] = 1
//    g[b][a] = 1
//
//
//def dfs(v):
//    visited[v] = True
//    print(v, end = ' ')
//    for i in range(1, n+1):
//        if not visited[i] and g[v][i] == 1:
//            dfs(i)
//
//def bfs(v):
//    visited[v] = False
//    queue = [v]
//    while queue: # queue가 채워져있는 동안에만 해당 while문이 돌아감
//        v = queue.pop(0)
//        print(v, end = ' ')
//        for i in range(n+1):
//            if visited[i] and g[v][i] == 1:
//                queue.append(i)
//                visited[i] = False
        
        
let nmvInput = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = nmvInput[0]
let m = nmvInput[1]
let v = nmvInput[2]

var visited = Array(repeating: false, count: n+1)
var graph = Array(repeating: [Int](), count: n+1) // [[], [], [], [], []]

for _ in 0..<m {
    let ab = readLine()!.split(separator: " ").map { Int(String($0))! }
    let a = ab[0]
    let b = ab[1]
    graph[a].append(b)
    graph[b].append(a)
    // 이 부분은 해당 문제에서 정점 번호가 작은 것을 먼저 방문하기 때문에 정렬을 해주는 것이다.
    graph[a].sort()
    graph[b].sort()
}

// [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

func dfs(_ x: Int) {
    visited[x] = true
    print(x, terminator: " ")
    
    for i in graph[x] {
        if visited[i] == false {
            dfs(i)
        }
    }
}

var queue: [Int] = []

func bfs(_ x: Int) {
    
    visited[x] = true
    queue.append(x)
//    print(queue,"=========")
    while !queue.isEmpty {
        print(queue,"=========")
        let newX = queue.removeFirst()
        print(newX, terminator: " ")
        
        for i in graph[newX] {
            print(graph[newX],"##########")
            if visited[i] == false {
                print(i,"-!!!!!!!!!")
                queue.append(i)
                visited[i] = true
            }
        }
    }
}

//dfs(v)
print()
visited = Array(repeating: false, count: n+1)
bfs(v)
