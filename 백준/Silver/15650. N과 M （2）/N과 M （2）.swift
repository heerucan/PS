import Foundation

let nm = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = nm[0]
let m = nm[1]
var answer = [Int]()

func backtracking() {
    // 숫자 길이가 m이랑 같으면 더해서 반환
    if answer.count == m {
        answer.map { print($0, terminator: " ") }
        print()
        return
    }
    
    for i in 1...n { // 1부터 n까지 돌면서
        if !answer.contains(i) { // 중복X
            if answer.last ?? 0 < i {
                answer.append(i)
                backtracking()
                answer.popLast()
            }
        }
    }
}

backtracking()