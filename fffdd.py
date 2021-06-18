Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> file ('C:\Users\1321m\OneDrive\Desktop')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> 
>>> 
>>> 
>>> file ('C:/Users/1321m/OneDrive/Desktop/hehe.txt')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    file ('C:/Users/1321m/OneDrive/Desktop/hehe.txt')
NameError: name 'file' is not defined
>>> file=open('C:/Users/1321m/OneDrive/Desktop/hehe.txt')
>>> 
>>> 
>>> 
>>> file.read
<built-in method read of _io.TextIOWrapper object at 0x000001F8B7D7F450>
>>> file.read()
'udgruhuhbfbdlkfjhngljkdhfjghdjfhgj'
>>> file.read()
'djfhgjudgruhuhbfbdlkfjhngljkdhfjghdjfhgjudgruhuhbfbdlkfjhngljkdhfjghdjfhgj\nudgruhuhbfbdlkfjhngljkdhfjghdjfhgj\nudgruhuhbfbdlkfjhngljkdhfjghdjfhgj\nudgruhuhbfbdlkfjhngljkdhfjghdjfhgj\nudgruhuhbfbdlkfjhngljkdhfjghdjfhgj\nudgruhuhbfbdlkfjhngljkdhfjghdjfhgj\nudgruhuhbfbdlkfjhngljkdhfjghdjfhgj\nudgruhuhbfbdlkfjhngljkdhfjghdjfhgj\n\n\nudgruhuhbfbdlkfjhngljkdhfjghdjfhgjudgruhuhbfbdlkfjhngljkdhfjghdjfhgjudgruhuhbfbdlkfjhngljkdhfjghdjfhgjudgruhuhbfbdlkfjhngljkdhfjghdjfhgjudgruhuhbfbdlkfjhngljkdhfjghdjfhgjudgruhuhbfbdlkfjhngljkdhfjghdjfhgjudgruhuhbfbdlkfjhngljkdhfjghdjfhgjudgruhuhbfbdlkfjhngljkdhfjghdjfhgjudgruhuhbfbdlkfjhngljkdhfjghdjfhgj'
>>> file.readlines()
[]
>>> 
>>> file=open('C:/Users/1321m/OneDrive/Desktop/hehe.txt')
>>> 
>>> file.readlines()
['i am mehakpreet\n', 'from punjab\n', 'i am in 8th grade\n', 'done']
>>> name="MehakPreet Singh Handa"
>>> name.split
<built-in method split of str object at 0x000001F8B808DEE0>
>>> name.split()
['MehakPreet', 'Singh', 'Handa']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
NameError: name 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh' is not defined
>>> name="me.tg.th.dr.se.hg.se.bf.xd.op,yup."
>>> name.split()
['me.tg.th.dr.se.hg.se.bf.xd.op,yup.']
>>> name.split(,)
SyntaxError: invalid syntax
>>> name.split(",")
['me.tg.th.dr.se.hg.se.bf.xd.op', 'yup.']
>>> name.split(".")
['me', 'tg', 'th', 'dr', 'se', 'hg', 'se', 'bf', 'xd', 'op,yup', '']
>>> def greet(name):
	print ("helo i am a human"+ name)

	
>>> 
>>> greet("name")
helo i am a humanname
>>> greet(" being")
helo i am a human being
>>> def countword():
	filename=input("enter the file path ")
	numberofword=0
	filw=open(filename,'r')
	for i in filw:
		word=i.
		
SyntaxError: invalid syntax
>>> def countword():
	filename=input("enter the file path ")
	numberofword=0
	filw=open(filename,'r')
	for i in filw:
		word=i.split

		
>>>  def countword():
	filename=input("enter the file path ")
	numberofword=0
	filw=open(filename,'r')
	for i in filw:
		word=i.split()
		
SyntaxError: unexpected indent
>>> def countword():
	filename=input("enter the file path ")
	numberofword=0
	filw=open(filename,'r')
	for i in filw:
		words=i.split()
		numberofword=numberofword+len(words)
	print("words=")
	print(numberofword)

	
>>> countword()
enter the file path 
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    countword()
  File "<pyshell#64>", line 4, in countword
    filw=open(filename,'r')
FileNotFoundError: [Errno 2] No such file or directory: ''
>>> countword()
enter the file path C:/Users/1321m/OneDrive/Desktop/etry.py
words=
7617
>>> 