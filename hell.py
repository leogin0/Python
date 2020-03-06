# -*- encoding: utf-8 -*-
'''
@File : hell.py
@Time : 2020/02/21 08:55:39
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# xinxi = {'name':'杨玥琪','number': 120181080327,'class': '软件1801','year':19}
# print(xinxi['name'])
# xx = {'tex':21,'chen':22,'joy':23,'bob':24,'cidy':25}
# print(xx)

# del xinxi['name']  #删除
# print(xinxi)

# xinxi['school'] = 'ncepu'  #增加
# print(xinxi)

# xinxi['year'] = 18
# print(xinxi)

# thisset = set((9,8,7,6))
# print(thisset)
# set2 = {8,9,0}
# print(set2)
# thisset.pop()
# print(thisset)

#3.4练习1
# x=input("输入一组数，用空格隔开")
# y = x.split(" ")
# y = [int(y[i]) for i in range(len(y))]
# print(tuple(list(y)))

#3.4练习2
# x = int(input("请输入需要购买的苹果的重量（斤）："))
# y = int(input("请输入每斤的价格："))
# z = x * y
# print("您需要支付：",z)

#3.4练习3
# name = input("name:") 
# age = input("age:")
# skill = input("skill:")
# salary = input("salary:") 
# info = ''' --- info of ''' + name + ''' name: ''' + name + ''' age: ''' + age + ''' skill: ''' + skill + ''' salary: ''' + salary + ''' ''' 
# print(info)

# name = input("name:") 
# age = input("age:") 
# skill = input("skill:") 
# salary = input("salary:") 
# info1 = ''' --- info of %s --- Name:%s Age:%s Skill:%s Salary:%s ''' % (name,name,age,skill,salary) #注意这里的变量要一 一对应，缺少一个就会报错
# print(info1)

# name = input("username：") 
# age = input("age：") 
# skill = input("skill：") 
# salary = input("salary：") 
# info = ''' --- info of {_name} Name：{_name} Age：{_age} Skill：{_skill} Salary：{_salary} '''.format(_name=name, _age=age, _skill=skill, _salary=salary) #此处是赋值 print(info)

# name = input("name：") 
# age = input("age：") 
# skill = input("skill：") 
# salary = input("salary：") 
# info = ''' --- info of {0}--- Name：{0} Age：{1} Skill：{2} Salary：{3} '''.format(name, age, skill, salary) 
# print(info)

#3.4练习4
a = list(range(10))
for i in a:
    print(i)
print( )
for i in a:
    if i % 2 == 0:
        print(i)
