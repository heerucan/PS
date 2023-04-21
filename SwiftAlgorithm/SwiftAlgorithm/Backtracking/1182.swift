//
//  1182.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/21.
//

import Foundation


/*
 N개의 정수들 중에서 부분수열을 뽑아서 그걸 합한 값이 S가 되는 경우의 수
 */
let ns = readLine()!.split(separator: " ").map { Int($0)! }
let n = ns[0]
let s = ns[1]
let num = readLine()!.split(separator: " ").map { Int($0)! }

var sum = 0
var count = 0 // 경우의 수

// 조합이고, 경우의 수를 구하는 거고,
// 재귀탈출 = 결과배열의 합이 s랑 같을 때 탈출
// 한정조건 = 이미 갖고 있는 것은 포함하면 X && 비내림차순이어야 해

// 방문처리 배열을 사용해서 이미 선택한 원소를 다시 선택하지 않도록 처리하는 것보다는
// startIndex 파라미터를 사용해서 이전에 선택한 원소 이후부터 탐색하도록 구현하는 것이 더 간단하고 효율적
// depth는 현재까지 선택된 원소의 개수를 나타내는 변수, 재귀호출이 진행될수록 원소의 개수가 증가하고, 이게 부분수열의 길이를 나타냄
// depth > 0 즉, 최소 하나 이상의 원소를 선택 시에만 경우의 수가 증가
func backtrack(_ startIndex: Int, _ depth: Int) {
    if sum == s && depth > 0 {
        count += 1
    }
    
    // sumArray를 사용해서 현재 선택된 부분수열을 저장하는 것보다는
    // sum 변수를 통해서 현재까지의 부분수열의 합을 저장하는 것이더 간단하고 효율적
    
    for i in startIndex..<n {
        sum += num[i]
        backtrack(i+1, i+1)
        sum -= num[i]
    }
}

backtrack(0, 0)
print(count)


