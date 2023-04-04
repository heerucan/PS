//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/04.
//

import Foundation

let n = Int(readLine()!)!
var wine: [Int] = []
for _ in 0..<n {
    wine.append(Int(readLine()!)!)
}

var dp = Array(repeating: 0, count: 10001)

// dp[n] = n번까지 마셨을 때 최대양

dp[0] = wine[0] // n = 1

if n >= 2 { // n = 2
    dp[1] = wine[0]+wine[1]
}

if n >= 3 { // n이 2보다 작으면 아래 반복문에 들어갈 수 없음
    
    // n = 3
    dp[2] = max(wine[0]+wine[2], wine[0]+wine[1], wine[2], wine[1]+wine[2], wine[1], wine[0])
    
    // n >= 4
    for i in 3..<n {
        dp[i] = max(dp[i-3]+wine[i],
                    dp[i-2]+wine[i],
                    dp[i-1],
                    dp[i-3]+wine[i-1]+wine[i],
                    dp[i-3]+wine[i-1],
                    dp[i-2])
    }
}

print(dp[n-1])
