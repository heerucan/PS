def solution(park, routes):
    answer = []
    h,w = len(park[0])-1, len(park)-1
    x,y = 0,0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                x,y = i,j
    
    resX, resY = x,y
    for i in range(len(park)):
        for j in range(len(park[i])):
            for route in routes: 
                cnt = int(route[2])
                if route[0] == "E":
                    while cnt > 0 and 0 <= y+cnt <= h: 
                        y += 1
                        if park[x][y] == 'X':
                            y = resY
                            break
                        cnt -= 1

                elif route[0] == "W":
                    while cnt > 0 and 0 <= y-cnt <= h: 
                        y -= 1
                        if park[x][y] == 'X':
                            y = resY
                            break
                        cnt -= 1
                
                elif route[0] == "S":
                    while cnt > 0 and 0 <= x+cnt <= w: 
                        x += 1
                        if park[x][y] == 'X':
                            x = resX
                            break
                        cnt -= 1

                else:
                    while cnt > 0 and 0 <= x-cnt <= w: 
                        x -= 1
                        if park[x][y] == 'X':
                            x = resX
                            break
                        cnt -= 1
                resX, resY = x, y
                
            break
        break
        
    return [x,y]