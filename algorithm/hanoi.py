def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    print(num_disks, start_peg, end_peg)
    if num_disks == 1:
        return move_disk(num_disks, start_peg, end_peg)

    other_peg = (6 - start_peg - end_peg)

    hanoi(num_disks-1, start_peg, other_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks-1, other_peg, end_peg)


# 코드를 입력하세요.

# # 테스트 코드 (포함하여 제출해주세요)
##설명 포함
hanoi(3, 1, 3) #1
##위의 코드가 실행하는 코드
## 9번행 other_peg는 6- 1- 3 = 2
hanoi(2,1,2) #2
move_disk(3,1,3) #6
hanoi(2,2,3) #7
## 여기서 hanoi(2,1,2)는 다시
## 9번행 other peg는 6- 1-2 = 3
hanoi(1,1,3) #3
move_disk(2,1,2) #4
hanoi(1,3,2) #5
## num_disk가 1이므로 hanoi(1,1,3)의 결과가 제일 먼저 출력

## hanoi(2,2,3)은 다시
## 9번행 other_peg는 6-2-3 = 1
hanoi(1,2,1) #8
move_disk(2,2,3) #9
hanoi(1,1,3) #10


