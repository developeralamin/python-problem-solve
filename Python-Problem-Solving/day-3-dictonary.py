from itertools import count

thedic = {
   "brand": [10,20,40],
   "model": [20,30,40],
}
if 'brand' in thedic:
    count = len(thedic['brand'])
    total_sum = sum(thedic['brand'])
    print(f"{total_sum/count:.2f}")



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sumValue = sum(student_marks[query_name])
    countVal = len(student_marks[query_name])

    total_sum = sumValue / countVal

    print(f"{total_sum:.2f}")