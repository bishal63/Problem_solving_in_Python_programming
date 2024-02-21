#1.result sheet ar prapto number theke grade bair korar problem
'''number=input("prapto number")
number=int(number)
if number>=80:
    grade="a+"
elif number>=70:
    grade="a"
elif number>=60:
    grade="a-"
elif number>=50:
    grade="b"
elif number>=40:
    grade="c"
else:
    grade="f"
print("your grade is",grade)'''

#2.tinti sonngha ar moddhe boro sonngha bai korar problem
a=40
b=56
c=60
if a>b:
    boro=a
else:
    boro=b
if c>boro:
    boro=c
print("sobche boro digit",boro)

#3.list ar moddhe kono value present acce naki ta dekhar problem
'''family_members=["muksadul","mahafuja","mahabub","mitu","mahim"]
members=input("name")
if members in family_members:
    print(members, "also a family members")
else:
    print(members, "not also a family members")'''

#4.leap year sal bair korar problem
'''year=input("shal")
year=int(year)
if year%4==0: 
    print(year,"leap year shal")
else:
    print(year,"not leap year shal")'''

#5.leap year shal bair korar problem
'''year=input("shal")
year=int(year)
if year%4==0:
    print(year,"leap year shal")
elif year%400==0:
    print(year,"leap year shal")
elif year%100==0:
    print(year,"not leap year shal")
else:
    print(year,"not leap year shal")'''

#6.somobahu trivuj toiri korar problem
'''import turtle
turtle.shape("turtle")
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.exitonclick()'''

#7.loop babohar kore kono sentence(i love programming)ke 1000 bar print korar problem
'''for sentence in range(1000):
    print("I love programming")'''

#8.loop babohar kore index number 1000 print korar problem
'''for sentence in range(1001):
    print("programming lover")'''

#9.list ar sokol upadan a loop baboharer problem solve kori
'''name=["mahabub","papel","shakib","jannat"]
for student in name:
    print(student,"is a student")'''
#10.1-100 ar moddhe joor songha gulo print korar problem
'''number=0
while number<=100:
    print(number)
    number=number+2'''

'''numbers=[6,1,3,0,9,3,2,5]
big_number=numbers[0]
for n in numbers:
    if n>big_number:
        big_number=n
        print(big_number)'''

'''income_money=[7,8,9,3,6,2]
more_income=income_money[0]
for money in income_money:
    if money>more_income:
        more_income=money
        print(more_income)'''

#11.15 ar namota toiri korar problem solve kori
'''n=input("enter your number")
n=int(n)
m=1
while m<=10:
    print(n,"x",m,"=",n*m)
    m=m+1'''

#12.function use kore 5 ti songhar jogfol ninnoy korar problem
'''def number(a,b,c,d,e):
    f=a+b+c+d+e
    print(f)
number(10,12,15,17,10)'''

#list ar upadan gulo jog korar problem solving
'''def list1(a,b,c,d,e):
    f=[a,b,c,d,e]
    print(sum(f))
list1(10,12,14,16,18)'''

#13.list a kono akti notun item jog korar problem
'''number=[123,125,234,876,678,345,345,678,456,234,565,433,234,774,234,654,766]
number.append(234)
print(number)

number=[123,125,234,876,678,345,345,678,456,234,565,433,234,774,234,654,766]
number.insert(2,234)
print(number)'''

#14.list a kono akti item ke badh korar problem
'''number=[123,125,234,876,678,345,345,678,456,234,565,433,234,774,234,654,766]
number.remove(766)
print(number)

number=[123,125,234,876,678,345,345,678,456,234,565,433,234,774,234,654,766]
number.pop(0)
print(number)

number=[123,125,234,876,678,345,345,678,456,234,565,433,234,774,234,654,766]
number.clear()
print(number)'''

#15.list a kono akti item ke change korar problem
'''number=[123,125,234,876,678,345,345,678,456,234,565,433,234,774,234,654,766]
number[1]=123
print(number)'''

#16.list ar item gulo ke choto theke boro ooo boro theke choto sajanor problem
'''number=[123,125,234,876,678,345,345,678,456,234,565,433,234,774,234,654,766]
number.sort()
print(number)

number=[123,125,234,876,678,345,345,678,456,234,565,433,234,774,234,654,766]
number.reverse()
print(number)'''

#17.aker odhik list ke akottirito korar jonno
'''number=[123,125,234,876,678,345,345,678,456,234,565,433,234,774,234,654,766]
number2=[123,125,234,876,678,345,345,678,456,234,565,433,234,774,234,654,766]
number.extend(number2)
print(number)

number=[123,125,234,876,678,345,345,678,456,234,565,433,234,774,234,654,766]
number2=[123,125,234,876,678,345,345,678,456,234,565,433,234,774,234,654,766]
print(number+number2)

#18.list ar moto ar akti list toiri korar problem
number=[123,125,234,876,678,345,345,678,456,234,565,433,234,774,234,654,766]
number2=[i+3 for i in number]
print(number2)

mahabub=[1,3,5,7,9]
bishal=[i*i for i in mahabub]
print(bishal)'''







