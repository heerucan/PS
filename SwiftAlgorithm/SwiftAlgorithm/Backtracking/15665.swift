//
//  15665.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/20.
//

import Foundation

// n과m - 11
let nm = readLine()!.split(separator: " ").map { Int($0)! }
let n = nm[0]
let m = nm[1]
let num = readLine()!.split(separator: " ").map { Int($0)! }.sorted()
var output = Array(repeating: 0, count: m)

func backtrack(_ index: Int) {
    if index == m {
        print(output.map { String($0) }.joined(separator: " "))
        return
    }
    
    var used = Set<Int>() // 똑같은 조합을 체크하기 위한 집합
    
    for i in 0..<n {
        // 같은 수 여러번 골라도 되니까 방문처리는 안해도 됨
        if !used.contains(num[i]) { // 이미 포함하고 있는 조합이면 조건문 충족X
            output[index] = num[i]
            used.insert(num[i])
            backtrack(index+1)
        }
    }
}

backtrack(0)
