//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/11.
//

import Foundation

// LIS DP 공식
let n = Int(readLine()!)!
let aList = readLine()!.split(separator: " ").map { Int($0)! }

var dp = Array(repeating: 1, count: n)

for i in 1..<n {
    for j in 0..<i {
        if aList[i] > aList[j] {
            dp[i] = max(dp[i], dp[j]+1)
        }
    }
}

print(dp.max()!)
