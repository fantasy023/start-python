#! /usr/bin/python

# coding=utf-8
# [sample] 输出中文在linux bash下正常，windows控制台需要特殊处理

# [sample] print
print ("hello, world")

# [sample] 变量赋值
name = "bryan"
print name

# [sample] 多行字符串，以及缩进控制
info = """bryan, 
fantasy023, 
    @github.com
a    h"""
print info

# [sample] 同一行打印多个变量，以逗号分隔
given_name = "bryan"
surname = "Ennnn"
print given_name, surname

# [sample] 多分支判断
import time
day = time.strftime('%d',time.localtime(time.time()))
print day
day = int(day)
if day <= 10 :
    print "beginning"
elif day <= 20 :
    print "middle"
else :
    print "last"

# [sample] 基础类型－5种
var_number = 100.12
var_string = "Just a string."
var_list = [0, 1, 2, 3, "a"]
#tuple 可看作是一个不可更改的list
var_tuple = (100, 200, 'physics', 'chemistry')
# dictionary 即 key-value
var_dictionary = {"alice": "female", "bob": "male", "cindy": "female"}

print var_number
print var_string
print var_list
print var_tuple
print var_dictionary


# [sample] 算术运算 / 和 //
# "/" 会依据除数、被除数，来自动调整自己的类型，两个整数相除，会得整数，此时和“//”效果一样
# 当除数、被除数中有浮点数时，“/”会得到浮点数，而“//”仍将取整
print "-------arithmetic calulate-------"
aritha = 23.2
arithb = 11
arith_multi = aritha / arithb
arith_multi_multi = aritha // arithb

print arith_multi
print arith_multi_multi
print (arith_multi == arith_multi_multi)

# [sample] 位运算
print "-------binary calulate-------"
bina = 60
binb = 13
print (bina & binb)
print (bina | binb)
print (bina ^ binb)
print (~ binb)

# [sample] 随机数，及while循环
import random
print "-------random in while loop-------"
randindex = 5
while (randindex > 0):
    print random.random()
    # python 没有-- 或 ++ 运算符
    randindex -= 1    
print "------end-------"

# [sample] 字符串操作
print "-------string operations-------"
var_string_op = "My name is Bryan, and I am 10 year old"
print var_string_op[5:15]

var_string_op_format = "My name is %s, and I am %d year old"
print var_string_op_format % ("Bryan01", 18)

# 多行、复杂字符串
str_html = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>xx</B><P>  \t\r\n
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print str_html
# 内建函数
print str_html.count("</")

# [sample] list 操作
print "-------list--------"
list1 = ["a", "b"] + ["c", "d"] + [1] * 3
print list1
list_index = 4
while (list_index > 0):
    list1.append(list_index)
    list_index -= 1
print list1
print ("c" in list1)
list1.reverse()
list1.pop()
list1.remove(1)
print list1

print list1.count(1)

# [sample] tuple 运算
print "-------tuple--------"
tx, ty, tz = 1, 2, 3
print tz, ty, tx

# 注，后面的（1,）必须有逗号，否则报错，而list 无此限制
tuplea = ("a", "b") + ("c", "d") + (1,) * 3
print tuplea

print ("c" in tuplea)
print tuplea[-3], tuplea[-4], tuplea[-5] 

# [sample] dictionary运算
print "-------dictionary--------"
dictionary = {"list": list1, "tuple": tuplea, "str": var_string}
print dictionary

dictionary["number"] = var_number
del dictionary["tuple"]
print dictionary.keys()
print dictionary.values()

dict2 = {"list": "I am a list...", "fantasy023": "hoho~"}
# 使用dict2的对应值，来更新dictionary自身对应key的值，有对应，则修改；无对应，则新增
dictionary.update(dict2) 
print dictionary

# [sample] time
import time
import calendar

print "-------time--------"
localtime = time.localtime(time.time())
print localtime
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

cal = calendar.month(2016, 1)
print cal

# [sample] 函数
print "-------functions--------"
def printinfo (name, age = 18, *vars):
    print "name: ", name
    print "age: ", age
    for v in vars:
        print v
    return

printinfo("bryan", 20)
printinfo("bryan")
printinfo("bryan", 15, " year old")
