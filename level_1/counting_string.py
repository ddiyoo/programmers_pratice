s = 'pPoooyY'
# s = 'Pppyy'


# ddiyoo #1
def solution(s):

    answer = True
    s = list(s.lower())
    string = ['p','y']
    numberOfString = []
    for i in string:
        list_index = []
        basket = s
        while True:
            try:
                list_index.append(basket.index(i) + (list_index[-1]+1 if len(list_index) != 0 else 0 ))
                basket = s[list_index[-1] + 1:]
            except:
                break
        numberOfString.append(list_index)
    if len(numberOfString[0]) != len(numberOfString[1]) :
        answer = False
    return answer

### ddiyoo #2
def solution(s):
    answer = True
    s = list(s.lower())
    if s.count('p') != s.count('y'):
        answer = False
    return answer


### other solution

def solution(s):
    return s.lower().count('p') == s.lower().count('y')
