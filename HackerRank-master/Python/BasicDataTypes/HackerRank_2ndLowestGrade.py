"""Given the names and grades for each student in a Physics class of N students, 
print the name(s) of any student(s) having the second lowest grade."""

def data(N):
    dic = {}
    for i in range(N):
        name = input("Enter name of student {}: ".format(i+1))
        score = float(input("Enter the student's grade: " ))
        dic[name] = score
    lowest = min(dic.values())
    new = {}
    for key,value in dic.items():
        if value > lowest:
            new[key] = value
    """min(new,values()) returns smallest value in new dictionary"""
    lowest_new = min(new.values())
    """sorted in alphabetical order"""
    for key, value in sorted(new.items()):
        if value == lowest_new:
            print(key)
        
    
if __name__ == '__main__':
    N = int(input('How many students will you submit?: '))
    data(N)