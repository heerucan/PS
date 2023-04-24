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

// 배열을 순회하면서 각각의 인덱스를 비교해서 어떤 기준값보다 큰 값이 있으면 기준값을 수정해주는 과정
for i in 1..<n {
    for j in 0..<i {
        // 1-0
        // 2-0, 2-1
        // 3-0, 3-1, 3-2
        // 4-0, 4-1, 4-2, 4-3
        // 5-0, 5-1, 5-2, 5-3, 5-4
        // i=4인 경우를 계산 시에, dp[0]~dp[3]까지 모두 정해져있는 상황이다.
        // 따라서, index 4가 index 2보다 크면 dp[4]는 최소 dp[2]+1이라서 1을 더하는 것임
        if aList[i] > aList[j] {
            dp[i] = max(dp[i], dp[j]+1)
        }
    }
}

print(dp.max()!)
