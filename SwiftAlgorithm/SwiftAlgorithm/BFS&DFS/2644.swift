//
//  2644.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/03.
//

//# 전체 사람 수 n
//# 둘째 줄 : 촌수 계산해야 하는 서로 다른 두 사람 번호
//# 셋째 줄 : 부모 자식 간의 관계의 개수 m
//# 넷째 줄 : 부모 자식 간의 관계를 나타내는 두 번호 x, y (x-부모, y-자식)
//# 촌수 계산할 필요없으면 -1 반환
//# DFS

        
import Foundation

let n = Int(readLine()!)!
let abInput = readLine()!.split(separator: " ").map { Int(String($0))! }
let a = abInput[0]
let b = abInput[1]
let m = Int(readLine()!)!

var graph = Array(repeating: [Int](), count: n+1)
var visited = Array(repeating: false, count: n+1)

for _ in 0..<m {
    let xyInput = readLine()!.split(separator: " ").map { Int(String($0))! }
    let x = xyInput[0]
    let y = xyInput[1]
    graph[x].append(y)
    graph[y].append(x)
}

var total = -1
func dfs(x: Int, depth: Int) {
    visited[x] = true
    
    // a랑 b가 같은 노드 연결 요소에 속해서 b가 x랑 같으면 결국 연결되어 있는 것임
    if x == b {
        total = depth
    }
    
    for i in graph[x] {
        if !visited[i] {
            dfs(x: i, depth: depth+1)
        }
    }
}

dfs(x: a, depth: 0)
print(total)
