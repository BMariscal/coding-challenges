# finding the percentage, hackerrank
# Python > Basic Data Types > Finding the percentage
#http://stackoverflow.com/questions/13861594/python-3-3-programming-valueerror-invalid-literal-for-int-with-base-10-be

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

a=sum(student_marks[query_name])/len(student_marks[query_name])

print ("%.2f" % a)
