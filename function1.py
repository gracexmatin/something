def reverse(a):
    for i in range(len(a)):
        if (300+i)<len(a):
            for j in range(i,300+i,1):
                x = 0
                y = 0
                if a[i,0]>a[j,0]:
                    x = a[i,0]
                    a[i,0] = a[j,0]
                    a[j,0] = x
                    y = a[i, 1]
                    a[i,1] = a[j,1]
                    a[j,1] = y
        else:
            for j in range(i,len(a),1):
                x = 0
                y = 0
                if a[i, 0] > a[j, 0]:
                    x = a[i, 0]
                    a[i, 0] = a[j, 0]
                    a[j, 0] = x
                    y = a[i, 1]
                    a[i, 1] = a[j, 1]
                    a[j, 1] = y
        if (i-300)>0:
            for j in range(i-300,i,1):
                x = 0
                y = 0
                if a[i,0] < a[j,0]:
                    x = a[i,0]
                    a[i,0] = a[j,0]
                    a[j,0] = x
                    y = a[i, 1]
                    a[i,1] = a[j,1]
                    a[j,1] = y
        else:
            for j in range(0,i,1):
                x = 0
                y = 0
                if a[i, 0] < a[j, 0]:
                    x = a[i, 0]
                    a[i, 0] = a[j, 0]
                    a[j, 0] = x
                    y = a[i, 1]
                    a[i, 1] = a[j, 1]
                    a[j, 1] = y
    return 0