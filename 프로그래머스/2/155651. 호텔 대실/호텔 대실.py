# 다음 타임의 시작시간 < 이전 타임의 끝시간 -> 방+=1
# 다음 타임의 끝시간 <= 이전 타임의 끝시간
import heapq
def solution(book_time):
    for i in book_time:
        time = i[1].split(":")
        time[1] = str(int(time[1])+10)
        if time[1] >= "60":
            if int(time[0]) < 9:
                time[0] = "0" + str(int(time[0])+1)
            else:
                time[0] = str(int(time[0])+1)
            time[1] = "0" + str(int(time[1])%60)
        i[1] = ":".join(time)
            
    book_time.sort()
    end_time = []
    heapq.heappush(end_time, book_time[0][1])
    
    for i in range(1,len(book_time)):
        next_start_time = book_time[i][0]
        next_end_time = book_time[i][1]
        
        if end_time[0] > next_start_time: # 대실 끝나는시간 > 그다음 대실 시작시간  -> 룸+=1
            heapq.heappush(end_time, next_end_time)
        else: # 대실 끝나는시간 <= 그다음 대실 시작시간
            heapq.heappop(end_time)
            heapq.heappush(end_time, next_end_time)
        
    return len(end_time)