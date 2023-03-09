//
//  수박수박수박수박수박수?.swift
//  SwiftAlgorithm
//
//  Created by heerucan on 2023/03/09.
//

import Foundation

func solution(_ n:Int) -> String {
    if n % 2 == 0 {
        return String(repeating: "수박", count: n/2)
    } else {
        return String(repeating: "수박", count: n/2)+"수"
    }
}
