//
//  15666.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/20.
//

import Foundation

/*
 같은 수 여러번 골라도 되고,
 비내림차순!
 */

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
        // 이미 포함하고 있는 조합이면 조건문 충족X
        /* 현재추가하는 수 = num[i]
         즉, output[index]에 들어갈 수가 output[index-1]보다 더 커야 한다. 그게 비내림차순!
         */
        let outputIndex = index-1 >= 0 ? output[index-1] : output[0]
        if !used.contains(num[i]) && outputIndex <= num[i] {
            output[index] = num[i]
            used.insert(num[i])
            backtrack(index+1)
        }
    }
}

backtrack(0)
