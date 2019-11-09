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