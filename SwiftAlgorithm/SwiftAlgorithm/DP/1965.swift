//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/11.
//

import Foundation

/**
 LIS : 최장 증가 부분 수열 유형
 LIS (Longest Increasing Subsequence)
 - 어떤 수열 안에서 가장 긴 증가하는 수열을 찾는 것
 - 증가하는 수들이 연속하지 않아도 됨
 
 
 */

let n = Int(readLine()!)! // 배열 길이
let boxList = readLine()!.split(separator: " ").map { (Int($0)!) }


func lis(length: Int, _ arr: [Int]) -> Int {
    var dp = [Int](repeating: 1, count: length)
    
    // i는 현재 위치, j는 이전 위치
    for i in 1..<length {
        for j in 0..<i { // i번째 이전의 모든 요소 j
            /// i = 1, j = 0 / i = 2, j = 0,1 / i = 3 , j = 0,1,2 / i = 4, j = 0,1,2,3 / i = 5, j = 0,1,2,3,4 / ....
            if arr[i] > arr[j] {
                dp[i] = max(dp[i], dp[j]+1) // 1을 dp[j]에 더하는 이유?
            }
        }
    }
    print(dp.max()!)
    return dp.max()!
}

lis(length: n, boxList)
