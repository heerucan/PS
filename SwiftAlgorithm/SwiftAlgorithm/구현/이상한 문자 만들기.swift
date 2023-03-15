//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/15.
//

import Foundation

func solution(_ s:String) -> String {
    let sArr = s.components(separatedBy: " ")
    var result = ""
    for i in sArr {
        result.append(changeWord(String(i)))
        result.append(" ")  // 단어 사이에 공백 추가
    }
    result.removeLast()  // 마지막 공백 제거
    
    return result
}

func changeWord(_ s: String) -> String {
    var result = ""
    let sArr = s.map { String($0) }
    for i in 0..<sArr.count {
        if i % 2 == 0 {
            result.append(sArr[i].uppercased())
        } else {
            result.append(sArr[i].lowercased())
        }
    }
    return result
}
