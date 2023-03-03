//
//  main.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/03.
//

import Foundation

/*
 입출력 연습
 readLine()
 swift 터미널 Input에서는 엔터가 입력되면 EOF(End of File)처리가 된다.
 즉, 엔터가 한 번 입력되면 readLine() 한 개가 끝난다.
 
 - ' '를 기준으로 입력을 여러 개 받으면 - readLine() 한 개로 처리
 - 엔터 기준으로 여러 개 입력 받으면 - readLine() 여러 개
*/

if let value = readLine() {
    print(value)
}

// MARK: -  readLine()의 반환값은 String?형이라서 Int형으로 형변환 필요
// readLine 언래핑하면 String이 되고, Int로 감싸면 Int?가 된다.
// 왜 옵셔널이 되냐면, Int로 형 변환이 실패할 경우 nil을 할당하기 때문이다.
// 결과적으로 String? -> String -> Int? -> Int
let input = readLine()!
let intInput = Int(input)!
let intInput2 = Int(readLine()!)! // 이렇게 써주면 되겠지?!
print(input, intInput)


// MARK: - split()과 components()로 공백 단위로 입력받기
// h e l l o 를 입력하면 -> ["h", "e", "l", "l", "o"]
// split은 Array<Substring>, components는 Array<String>을 반환한다.

// Array<Substring>으로 반환됨
let result = input.split(separator: " ")
let result2 = input.split { $0 == " " } // 클로저를 이용해서 가능

// String으로 반환하려면 components는 Foundation 프레임워크에 포함되어서 import Foundation으로 사용해야 함
let result3 = input.components(separatedBy: " ")
print(result, result2, result3)


// MARK: - 개행(줄바꿈) 단위로 입력받기
// 줄바꿈 단위는 readLine() 여러번 써서 하면 가능

let firstInput = readLine()!
let secondInput = readLine()!
print(firstInput, secondInput)


// MARK: - 정수 여러 개 입력받기
// split(separator: " ")를 통해서 문자열로 먼저 공백 기준으로 입력을 받은 후에
// 각각의 값을 Int로 형 변환하였음
// 3 4 5 -> [3, 4, 5]

let severalInput = readLine()!.split(separator: " ").map { Int(String($0))! }
print(severalInput)


// MARK: - 연속적으로 입력 받기
// 12345를 입력받아서 1 2 3 4 5 개별 문자로 분리시키는 것
// 0099 -> ["0", "0", "9", "9] -> [0, 0, 9, 9]

let arrayInput = Array(readLine()!)
print("Array",arrayInput) // Array<Character>
let arrayResultInput = arrayInput.map { Int(String($0))! }
print("Array<Int>",arrayResultInput) // Array<Int>


// MARK: - 최종적으로 요약

/// 정수 한 개 입력
let oneIntInput = Int(readLine()!)!
print(oneIntInput) // 1 -> 1

/// 정수 여러 개 입력
let severalIntInput = readLine()!.split(separator: " ").map { Int(String($0))! }
print(severalIntInput) // 1 2 222 3 -> [1, 2, 222, 3]

/// 문자열 한 개 입력
let characterInput = readLine()!
print(characterInput) // hiruhee -> hiruhee

/// 문자열 여러 개 입력
let severalCharacterInput = readLine()!.split(separator: " ")
let severalCharacterInput2 = readLine()!.split { $0 == " " }
print(severalCharacterInput) // hi ruhee hi hii -> ["hi", "ruhee", "hi", "hii"]
print(severalCharacterInput2) // ruhee hi -> ["ruhee", "hi"]

/// 연속적인 정수 입력
let continuousInput = Array(readLine()!.map { Int(String($0))! })
print(continuousInput) // 982 -> [9, 8, 2]
