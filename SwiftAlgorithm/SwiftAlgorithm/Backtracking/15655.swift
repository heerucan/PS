//
//  15655.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/18.
//

import Foundation

let nm = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = nm[0]
let m = nm[1]

var array = readLine()!.split(separator: " ").map { Int(String($0))! }
var answerArray = [Int]()
var answer = ""

func backtracking() {
    if answerArray.count == m {
        answer.append(answerArray.map { String($0) }.joined(separator: " "))
        answer.append("\n")
        return
    }
    
    for i in array.sorted(by: <) {
        if !answerArray.contains(i) && answerArray.last ?? 0 < i {
            answerArray.append(i)
            backtracking()
            answerArray.popLast()!
        }
    }
}

backtracking()
print(answer)
