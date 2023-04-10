//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/10.
//

import Foundation

let n = Int(readLine()!)!
var sb = [[Int]]()
for _ in 0..<n {
    sb.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}
// 순서대로 s, b

var minDiff = Int.max // 9223372036854775807

func sum(_ index: Int, s: Int, b: Int) {
    guard index < n else { return } // index가 n보다 작은 경우에만 실행
    let newS = s * sb[index][0] // s는 곱
    let newB = b + sb[index][1] // b는 합
    
    // 신맛과 쓴맛의 차가 현재까지의 최솟값보다 더 작으면
    // minDiff를 더 작은 값으로 갱신
    if minDiff > abs(newS-newB) {
        minDiff = abs(newS-newB)
    }
    // 모든 가능한 조합을 만들기 위함 
    sum(index+1, s: newS, b: newB) // 현재 맛을 더한 후의 새로운 값
    sum(index+1, s: s, b: b) // 현재 맛을 더하지 않고 다음 상태로 넘어감
}

sum(0, s: 1, b: 0)
print(minDiff)

/*
 예를 들어, 3개의 아이스크림이 있고, 각각의 아이스크림에는 S, B라는 값을 가지고 있다.

 아이스크림1: S1, B1 = [1,2]
 아이스크림2: S2, B2 = [3,4]
 아이스크림3: S3, B3 = [5,6]
 위와 같이 세 개의 아이스크림이 있다면, 우리는 아래와 같은 조합을 만들 수 있다.

 S1S2S3, B1+B2+B3
 S1*S2, B1+B2
 S1*S3, B1+B3
 S2*S3, B2+B3
 S1, B1
 S2, B2
 S3, B3
 
 현재 아이스크림을 더하는 경우, 안 더하는 경우 모두 고려하는 이유는 모든 가능한 조합을 만들기 위함
 */
