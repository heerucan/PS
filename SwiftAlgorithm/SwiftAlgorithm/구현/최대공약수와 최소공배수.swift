//
//  최대공약수와 최소공배수.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/10.
//

import Foundation

// MARK: - 내 풀이

func solution(_ n:Int, _ m:Int) -> [Int] {
    
    var nArr: [Int] = []
    var mArr: [Int] = []
    
    for i in 1...n {
        if n % i == 0 {
            nArr.append(i)
        }
    }
    
    for i in 1...m {
        if m % i == 0 {
            mArr.append(i)
        }
    }
    
    var total = Array(Set(nArr).intersection(Set(mArr)))
    total.sort()
    var last = total[total.count-1]
    return [last, (n/last) * (m/last) * last]
}


// MARK: - 더 좋은 풀이

func solution2(_ n:Int, _ m:Int) -> [Int] {
    var first: [Int] = []
    for index in 1...n {
        if n % index == 0  && m % index == 0 {
            first.append(index)
        }
    }
    let maxValue: Int = first[first.count-1]
    return [maxValue ,(n * m)/maxValue ]
}
