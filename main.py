d=input()
if len (s) !=16
    print('ошибка')
else:
    sum1=0
    for i in range(0, len(d),2):
        n=int(d[i])
        if n*2>9
            sum1=sum1+(n*2-9)
        else:
            sum1=sum1+n*2
    sum2=0
    for x in range(1,len(s),2):
        f=int(s[x])
        sum2=sum2+f
    n=sum1+sum2
    if n%10==0:
        print('Карта корректна')
    else:
        print('ошибка')