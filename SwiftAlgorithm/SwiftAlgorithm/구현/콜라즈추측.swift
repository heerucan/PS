//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/06.
//

import Foundation

func calculate(_ value: Int) -> Int {
    if value % 2 == 0 {
        return value/2
    } else {
        return value*3+1
    }
}

func solution(_ num: Int) -> Int {
    var cnt = 0
    var value = num
    while value != 1 {
        value = calculate(value)
        cnt += 1
        if cnt == 500 {
            return -1
        }
    }
    return cnt
}

//print(solution(16))
