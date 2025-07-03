#x="hello"
#print(type("hello"))

#str1="12345"
#print(f"str1 is {str1}")

#name="小明"
#print("你好，{}！".format(name))

#str="This is an \"apple\""
#print(str)

#str='This is an \"apple\"'
#print(str)

#str1="Hi my name is "
#str2="Hong jung"
#print(str1,"\n",str2)

#name=input("what's your name?")
#print("hello","\t"+name+":)")

#=0.25
#y=0.2589
#sum=x+y
#print(round(sum,2))

#kg=float(input("輸入體重(公斤):"))
#hight=float(input("輸入身高(公分):"))/100
#BMI=kg/hight**2
#print(BMI)

#x="happy"
#y=0.256
#z=False
#print(type(x))
#print(type(y))
#print(type(z))

#x=10
#y=0.3
#print(x+y,type(x+y))

#3
#a=100
#b=200
#print(str(a+b))

#4
#a=100
#b=200
#print(str(a)+str(b))

#5
#s1="hello"
#s2="python"
#print(s1+s2)

#6
#word="GO!"
#print(word*5)

#7
# sentence="the quick brown fox jumps over the lazy dog"
#print("fox" in sentence)
#print("cat" in sentence)

#8
#str="it is a file named \"My Document\""
#print(str)

#9
#str="  learning python is funny!  "
#print(f'{str.strip().capitalize().title()}')

#10
#data="my favorite food is potato."
#print(f'{data[0].capitalize()}')
#print(len(data))

#11
#code="1257893"
#text="李帝努是小狗狗"
#print(text.isnumeric())
#print(text.isalpha())
#print(code.isdigit())

#12
#str="hello my dog"
#print(str.find("dog"))
#print(str[10])
#print(str[-1])

#13
#name="王曉明"
#ch=78
#en=56
#ma=98
#av=(ch+en+ma)/3
#print(name+str(round(av,2)))

#list
#list1=[5,48,65,78]
#list1.insert(2,56) >這一行要單獨寫，沒辦法簡寫成下面那樣
#print((list1.insert(2,56)))

#list1 = [5]
#print((list1.insert(2, 56)))
#print(list1)

#a=6
#a%=5
#print(a)

def add_list3(no_list):
    sum=0
    sum+=no_list[0]
    sum+=no_list[1]
    sum+=no_list[2]
    return sum
ans=add_list3([4,4,3])
#print(ans)

#def say_hi():
 #   print("Hello !!!")
#say_hi()

def x():
    print(5+6+7)
x()