import os

import random

import time as t

import sys

import MySQLdb

import subprocess 

from datetime import datetime 

try:

	parameter=sys.argv[1]

	if parameter=='c':

		for file in os.listdir('.'):

			fix=file.split('.')[-1]

			if fix=='class':

				os.remove(file)

except Exception as e:

	pass

route=input('Use the file last ?')

if route=='y':

	if os.path.exists('route.txt'):

		f=open('route.txt','r')

		filename=f.readline()

		f.close()

else:
	
	filename=input("Enter the java file you want to compile \n")

	f=open('route.txt','w')

	f.write(filename+'\n')

	f.close()

filename=filename.strip('\n')

filenames=filename+'.java'

conn=MySQLdb.connect('localhost','root','666666','server',charset="UTF8")

time=datetime.now()

time=time.strftime('%Y-%m-%d %H:%M:%S')

cursor=conn.cursor()

print('javac {}'.format(filenames)+'...')

status,result=subprocess.getstatusoutput('javac {} -encoding utf-8'.format(filenames))

if status==1:

	print("error compile")

	cursor.execute('insert into filename(name,dates,compileresult,reason) values("%s","%s","%s","%s")'%(filenames,time,'false',result))

else:

	cursor.execute('insert into filename(name,dates,compileresult) values("%s","%s","%s")'%(filenames,time,'success'))

conn.commit()

conn.close()

while True:

	print('java {} {} {}'.format(filename,str(random.randint(0,127)),str(random.randint(0,127)))+'...')
	
	os.system('javac {} -encoding utf-8'.format(filenames))

	os.system('java {} {} {}'.format(filename,str(random.randint(0,127)),str(random.randint(0,127))))

	t.sleep(1)

	print('-------------------------')

	if input('enter any key to continue')=='q':

		break

print("success")
