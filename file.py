#! /usr/bin/python


# [sample] 
fo = open("./test/2.dat", "a+")
print "File Name: ", fo.name
print "Mode: ", fo.mode

fo.write("This is a blank file for test. \n")

fo.close()

# [sample] 
fo = open("./test/2.dat", "a+")

str = fo.read(10)
print "Have read as: ", str
position = fo.tell()
print "Current Position: ", position

fo.seek(0, 0)
str = fo.read(10)
print "Have read as: ", str

fo.close()

# [sample] 
import os
 
# 给出当前的目录
print os.getcwd()




