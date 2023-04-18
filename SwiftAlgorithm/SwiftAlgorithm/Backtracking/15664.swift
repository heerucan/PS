//
//  15664.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/18.
//

import Foundation

/*
 ex. 1 7 9 9 라는 4개(N개)의 자연수 중에서 M개를 고른 수열
- 한정조건 : 비내림차순
- 제귀탈출 : m개인 경우
 
 근데 대신 9, 9는 2개라서 서로 다른 것으로 인식해야 함
 이 경우에 방문처리를 위한 배열을 만들어야 함!
 
 */


let nm = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = nm[0]
let m = nm[1]
var array = readLine()!.split(separator: " ").map { Int(String($0))! }
var sortArray = array.sorted(by: <)

var answerArray = [Int]()
var answer = ""

var visited = Array(repeating: false, count: n) // 방문처리를 해야 함!!



func backtracking() {
    // 길이가 m개가 아니고, 이미 7 9와 같이 문자열을 갖고 있다면, 조건 불충족!
    if answerArray.count == m && !answer.contains(answerArray.map { String($0) }.joined(separator: " ")){
        answer += answerArray.map { String($0) }.joined(separator: " ")
        answer += "\n"
        return
    }
    
    for (index, i) in sortArray.enumerated() {
        // 방문하지 않은 아이 && 마지막 수가 크거나 같아야 함 9 9 의 경우를 위해서
        if !visited[index] && answerArray.last ?? 0 <= i {
            answerArray.append(i)
            visited[index] = true
            backtracking()
            visited[index] = false
            answerArray.removeLast()
        }
    }
}

backtracking()
print(answer)
