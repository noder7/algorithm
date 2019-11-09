# link below
# https://www.hackerrank.com/challenges/nested-list/problem
'''
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

<Input Format>

The first line contains an integer, N , the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

<Constraints>

2 <= N <= 5
There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

<Sample Input 0>

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
<Sample Output 0>

Berry
Harry
<Explanation 0>

There are 5 students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
'''

if __name__ == '__main__':

    l = []
    for i in range(int(input())):
        l.append([])
        name = input()
        score = float(input())
        l[i].append(name)
        l[i].append(score)

    a = []
    for i in range(len(l)):
        for j in range(1, len(l)):
            if l[j-1][1] > l[j][1]:
                a = l[j-1]
                l[j-1] = l[j]
                l[j] = a
            elif l[j-1][1] == l[j][1]:
                if l[j-1][0] > l[j][0]:
                    a = l[j-1]
                    l[j-1] = l[j]
                    l[j] = a

    second = []
    # find the second lowest score!
    for i in range(1, len(l)):
        if l[i-1][1] < l[i][1]:
            second.append(l[i])
            break
    
    for i in range(len(l)):
        if second[0][0] != l[i][0] and second[0][1] == l[i][1]:
            second.append(l[i])
    
    for i in range(len(second)):
        print(second[i][0])