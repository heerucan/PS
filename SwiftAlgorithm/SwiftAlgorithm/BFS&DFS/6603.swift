//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/04/04.
//

import Foundation

// 조합 문제 - 순서가 달라도 같은 것으로 생각

// 7 [1, 2, 3, 4, 5, 6, 7]

var numbers = readLine()!.split(separator: " ").map { String($0) }
let k = Int(numbers[0])!
let s = numbers.suffix(k).map { String($0) }
var visit = [Bool](repeating: false, count: k)

/*
 data : numbers
 curInd : 현재 인덱스
 curCnt : 현재까지 선택한 원소의 개수
 targetCnt : 선택해야 할 원소의 개수
 answer : 현재까지 선택한 원소들의 조합
 */

func combination(data: [String], curInd: Int, curCnt: Int, targetCnt: Int, answer: String) {
    // curCnt가 targetCnt와 같아지면, 현재까지 선택한 원소들의 조합을 출력
    if curCnt == targetCnt {
        print(answer)
    }
    
    for i in curInd..<data.count { // 현재 인덱스부터 끝까지 모두 순회
        if !visit[i] {
            visit[i] = true // 방문처리
            // 재귀를 통해
            combination(data: data,
                        curInd: i, // -> 현재 인덱스 i로 바꿈
                        curCnt: curCnt + 1, // 선택한 원소 개수 +1
                        targetCnt: targetCnt,
                        answer: answer + data[i] + " ") // 현재까지 선택한 원소 조합 + data[i]
            visit[i] = false // 안그럼 다 방문한 상태임
        }
    }
}
