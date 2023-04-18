//
//  15651.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/17.
//

import Foundation

/*
 한정조건 : 중복 가능
 재귀탈출 : m개
 */

let nm = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = nm[0]
let m = nm[1]

var answer = [Int]()
var answerString = ""

func backtracking() {
    if answer.count == m {
        // 시간초과가 나서 문자열에 더해서 한 번에 출력하는 방식
        answerString += answer.map { String($0) }.joined(separator: " ")
        answerString += "\n"
        return
    }
    
    for i in 1...n {
        answer.append(i)
        backtracking()
        answer.removeLast()
    }
}

backtracking()
print(answerString)
