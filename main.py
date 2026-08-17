#day from date

def check_day (d,m,y):
    
    if m not in range(1,13):
        return 'month must be correct as only 12 months'
    k=0
    w=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    DD=[2,0,5,3]
    y1=y//100
    y2=y%100
    Dc=DD[y1%4]
    Dy=((((y2//4)+y2)%7)+Dc)%7
    Dm=[3,28,14,4,9,6,11,8,5,10,7,12]
    if y%4==0:
        Dm[0],Dm[1]=4,29
    dm=Dm[m-1]
    if d==dm:
        c=w[Dy]
    elif d<dm:
        a=(dm-d)%7
        b=7-a
        c=w[(Dy+b)%7]
    elif d>dm:
        a=(d-dm)%7
        c=w[(Dy+a)%7]
    month={1:'jan',2:'feb',3:'mar',4:'apr',5:'may',6:'jun',7:'july',8:'aug',9:'sep',10:'oct',11:'nov',12:'dec'}
    from colorama import Fore
    k=f'''
    Date:{d}
    Month:{month[m]}
    Year:{y} {Fore.RED}
    The day is {c}
    '''
    return k
print('this is mathematically so the date and year invalid may also give results but month should be legit \n input should be integer only')
x=int(input("enter date: "))
y=int(input("enter month: "))
z=int(input("enter year: "))
print(check_day(x,y,z))
