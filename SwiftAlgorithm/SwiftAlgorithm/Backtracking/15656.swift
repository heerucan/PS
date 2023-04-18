//
//  15656.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/18.
//

import Foundation

let nm = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = nm[0]
let m = nm[1]

var array = readLine()!.split(separator: " ").map { Int(String($0))! }.sorted(by: <)
var answerArray = [String]() // 시간초과가 나기 때문에 map을 사용하지 않기 위해서 string 배열로 변경
var answer = ""

func backtracking() {
    if answerArray.count == m {
        answer += answerArray.joined(separator: " ") // map을 없앰
        answer += "\n"
        return
    }
    
    for i in array {
        answerArray.append("\(i)")
        backtracking()
        answerArray.removeLast()
    }
}

backtracking()
print(answer)
