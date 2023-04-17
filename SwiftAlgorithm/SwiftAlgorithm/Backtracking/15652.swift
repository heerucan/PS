//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/17.
//

import Foundation

let nm = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = nm[0]
let m = nm[1]

var answer = [Int]()

func backtracking() {
    if answer.count == m {
        answer.map { print($0, terminator: " ") }
        print()
        return
    }
    
    for i in 1...n {
        if answer.last ?? 0 <= i {
            answer.append(i)
            backtracking()
            answer.removeLast()
        }
    }
}

backtracking()
