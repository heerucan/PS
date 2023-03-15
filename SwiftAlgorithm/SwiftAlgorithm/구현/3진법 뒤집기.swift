//
//  3진법 뒤집기.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/15.
//

import Foundation

func solution(_ n:Int) -> Int {
    var three = 0
    var arr: [Int] = []
    var N = n
    while N > 0 {
        arr.append(N%3)
        N /= 3
    }
    
    for i in 0..<arr.count {
        var value = Int(pow(Double(3), Double(arr.count-1-i)))
        three += value*arr[i]
    }
    
    return three
}
