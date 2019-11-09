def solution(k, room_number):
    N = len(room_number)
    set_room = set(room_number)
    _min, _max = min(set_room), max(set_room)
    ceil = _max+(N-len(set_room))
    
    room = list(range(_min,ceil+1))
    visited = [0]*len(room)

    answer = []
    for rn in room_number:
        idx = rn-_min
        while True:
            if not visited[idx]:
                visited[idx] = 1
                answer.append(idx+_min)
                break
            else:
                idx+=1
    return answer



# 2nd try
def solution(k, room_number):
    rooms = sorted(list(set(room_number)))
    bound = {}
    gateway = {r:r for r in rooms}
    max_v = rooms[-1]
    for a,b in zip(rooms[0:-1],rooms[1:]):
        bound[a]=b
    bound[max_v] = 200001
    answer = []
    for rn in room_number:
        while True:
            if gateway[rn] != None:
                v = gateway[rn]
                answer.append(v)
                if v+1 == bound[rn]:
                    gateway[rn]= None
                else:
                    gateway[rn]+=1
                break
            else:
                rn = bound[rn]
    return answer


# 3rd try
def solution(k, room_number):
    rooms = sorted(list(set(room_number)))
    bound = {}
    gateway = {r:r for r in rooms}
    converter = {r:r for r in rooms}
    max_v = rooms[-1]
    for a,b in zip(rooms[0:-1],rooms[1:]):
        bound[a]=b
    bound[max_v] = 200001
    
    answer = []
    for rn in room_number:
        new_rn = converter[rn]
        while True:
            if gateway[new_rn] != None:
                v = gateway[new_rn]
                answer.append(v)
                if v+1 == bound[new_rn]:
                    gateway[new_rn]= None
                else:
                    gateway[new_rn]+=1
                break
            else:
                new_rn = bound[new_rn]
        converter[rn] = new_rn
    return answer

k = 10
rn = [1,3,4,1,3,1]
print(solution(k,rn))

# 5th try

def solution(k, room_number):
    rooms = sorted(list(set(room_number)))
    bound = {}
    gateway = {r:r for r in rooms}
    converter = {r:r for r in rooms}
    max_v = rooms[-1]
    for a,b in zip(rooms[0:-1],rooms[1:]):
        bound[a]=b
    bound[max_v] = 200001

    answer = []
    for rn in room_number:
        new_rn = converter[rn]
        while True:
            if gateway[new_rn] != None:
                v = gateway[new_rn]
                answer.append(v)
                if v+1 == bound[new_rn]:
                    gateway[new_rn]= None
                else:
                    gateway[new_rn]+=1
                break
            else:
                new_rn = bound[new_rn]
        if rn < new_rn:
            converter[rn] = new_rn
    return answer

k = 10
rn = [1,3,4,1,3,1]
print(solution(k,rn))