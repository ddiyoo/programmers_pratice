array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array,commands):
    answer = []
    for a in range(len(commands)):
        i = commands[a][0]
        j = commands[a][1]
        k = commands[a][2]
        s_commands=sorted(array[i-1:j])
        answer.append(s_commands[k-1])
    return answer
# print(solution(array,commands))

## upgrade!!
def solution_2(array,commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer
print(solution_2(array,commands))

##other solution
def solution_3(array,commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1],commands))
print(solution_3(array,commands))