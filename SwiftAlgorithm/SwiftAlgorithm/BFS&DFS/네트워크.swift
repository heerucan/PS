//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/23.
//

import Foundation

// 네트워크 프로그래머스 swift 다시 풀기

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var graph = Array(repeating: [Int](), count: n) // 3개까지만 만들었으니까, 0번째 배열을 고려해!
    var visited = Array(repeating: false, count: n)
    for i in 0..<n {
        for j in 0..<n {
            if computers[i][j] == 1 && i != j {
                graph[i].append(j)
            }
        }
    }
    print(graph)
    func dfs(_ x: Int) {
        visited[x] = true
        
        for i in graph[x] {
            if !visited[i] {
                dfs(i)
            }
        }
    }
    
    var result = 0 // 네트워크 개수
    
    for i in 0..<n {
        if !visited[i] {
            result += 1 // 왜냐면, if문을 빠져나와서 다시 for문을 도는 순간, 노드가 끊어진 것을 알 수 있음
            dfs(i)
        }
    }
    return result
}
