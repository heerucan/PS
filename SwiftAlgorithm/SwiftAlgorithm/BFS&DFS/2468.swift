//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/23.
//

import Foundation

let n = Int(readLine()!)!
var graph = Array(repeating: Array(repeating: Int(), count: n), count: n)
var visited = Array(repeating: Array(repeating: false, count: n), count: n)

var dx = [-1, 1, 0, 0]
var dy = [0, 0, -1, 1]

for i in 0..<n {
    graph[i] = readLine()!.split(separator: " ").map { Int($0)! }
}


//[[6, 8, 2, 6, 2], [3, 2, 3, 4, 6], [6, 7, 3, 3, 2], [7, 2, 5, 3, 6], [8, 9, 5, 2, 7]]
//장마철에 물에 잠기지 않는 안전한 영역의 최대 개수 반환

func dfs(x: Int, y: Int, _ height: Int) {
    visited[x][y] = true
    
    for i in 0..<4 {
        let xx = x + dx[i]
        let yy = y + dy[i]
        
        if 0 <= xx && xx < n && 0 <= yy && yy < n {
            if !visited[xx][yy] && graph[xx][yy] != height {
                dfs(x: xx, y: yy, height)
            }
        }
    }
}

// 좌표를 다 해당 높이로 바꾸는 함수 하나 만들기!

func changeHeightofGraph(_ height: Int) -> Int {
    var result = 0 // 지역변수여야만 height값이 바뀔 때마다 리셋시킬 수 있음
    var total = 0 // 이거는 -> 근까 그래프가 하나로 이어져있냐 아니냐 요소덩어리 체크하는 변수임
    
    for i in 0..<n {
        for j in 0..<n {
            if graph[i][j] <= height {
                graph[i][j] = height
            }
        }
    }

    for i in 0..<n {
        for j in 0..<n {
            if graph[i][j] != height && !visited[i][j] {
                total += 1
    //            result += 1 // 여기에 작성해주면 안된다! 그러면 dfs 진입 전에 계산해버림
                dfs(x: i, y: j, height)
                result += 1
            }
        }
    }
    // 아;; 이거 까먹지 말자. 갱신안해주면 다시 들어갈 때 방문체크가 다 true라서 못함
    visited = Array(repeating: Array(repeating: false, count: n), count: n)
    
    // dk.. 아 아무 지역도 물에 잠기지 않을 수도 있다. .. 쉬보레...ㅠ;
    if total == 0 { // 0이 나왔다는 것은 그래프가 끊겨있지 않고 하나로 연결됐다는 것이잖아!!!
        // 만약 하나의 그래프로 이어져있다면, 한 덩어리겠지 -> 1 즉, 최대영역 1
        return 1
    }
    return result
}

var arr = [Int]()

for i in graph.flatMap({ $0 }).min()!...graph.flatMap({ $0 }).max()! {
    arr.append(changeHeightofGraph(i))
}

print(arr.max()!)

