//
//  부족한 금액 계산하기.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/09.
//

import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    var answer:Int64 = 0
    for i in 1...count {
        answer += Int64(i*price)
    }
    if money > answer {
        return 0
    } else {
        return answer - Int64(money)
    }
}
