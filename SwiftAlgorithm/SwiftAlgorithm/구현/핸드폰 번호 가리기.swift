//
//  핸드폰 번호 가리기.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/06.
//

import Foundation

func solution(_ phone_number:String) -> String {
    var except = String(phone_number.prefix(phone_number.count-4))
    var result = ""
    except.map { String($0) }.forEach {
        let converExcept = String($0).replacingOccurrences(of: $0, with: "*")
        result += converExcept
    }
    return result + String(phone_number.suffix(4))
}

// MARK: - 더 좋은 풀이!!

func solution2(_ phone_number: String) -> String {
    return String(repeating:"*", count:phone_number.count-4)+phone_number.suffix(4)
}

print(solution2("01033334444"))
