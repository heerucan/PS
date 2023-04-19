//
//  15663.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/19.
//

import Foundation

let nm = readLine()!.split(separator: " ").map { Int($0)! }
let n = nm[0], m = nm[1]

let nums = readLine()!.split(separator: " ").map { Int($0)! }.sorted()
var visited = Array(repeating: false, count: n)
var output = Array(repeating: 0, count: m)

func backtrack(_ index: Int) {
    if index == m {
        print(output.map { String($0) }.joined(separator: " "))
        return
    }
    
    var used = Set<Int>()
    print("??- ",used)

    for i in 0..<n {
        // 선택되지 않은 수와 중복되지 않은 수를 차례로 선택
        if !visited[i] && !used.contains(nums[i]) {
            visited[i] = true
            output[index] = nums[i]
            used.insert(nums[i])
            backtrack(index + 1)
            visited[i] = false
        }
    }
}

backtrack(0)
