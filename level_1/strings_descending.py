s = 'Zbcdefg'
b = ['Z', 'b', 'c', 'd', 'e', 'f', 'g']
# print(sorted(s))
#
# print(sorted(s).sort(reverse=True))
def solution(s):
    answer = ''.join(sorted(b,reverse=True))
    return answer


