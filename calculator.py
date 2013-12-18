#/usr/bin/python
# coding: utf-8

from Tkinter import *

# 按键返回函数
def call(num):
	content = display.get() + num
	display.set(content)
# 使用eval 函数计算
def calculate():
	try:
		content = display.get()
		result = eval(content)
		display.set(content + '=\n' + str(result))
	except:
		display.set('Error')
		clear()
# 清空内容栏
def clear():
	display.set('')
# 删除前一个字符
def backspace():
	display.set(str(display.get()[:-1]))

def main():
	# 定义主窗口
	root = Tk()
	root.title('Calculator')
	root.geometry('210x200+300+400')
	# 将display定义成global，main() 函数外的call, calculate等可以调用
	global display
	display = StringVar()	
	#　设置内容显示栏，使用label，anchor是靠右，默认居中
	label = Label(root, relief = 'sunken', borderwidth = 3, anchor = SE)
	label.config(bg = 'grey', width = 25, height = 3)
	label['textvariable'] = display
	label.grid(row = 0, column = 0, columnspan = 4)

#	text = Text(root, relief = 'sunken', borderwidth = 3)
#	text.insert(INSERT, str(display))
#	text.grid(row = 0, column = 0, columnspan = 4)
	# 添加各个按钮，并绑定行为,使用lambda很方便，是用的是grid布局
	Button(root, text = 'C', fg = '#EF7321', width = 3, command = lambda: clear()).grid(row = 1, column = 0)
	Button(root, text = 'DEL', width = 3, command = lambda:backspace()).grid(row = 1, column = 1)
	
	Button(root, text = '/', width = 3, command = lambda:call('/')).grid(row = 1, column = 2)
	Button(root, text = '*', width = 3, command = lambda:call('*')).grid(row = 1, column = 3)
	Button(root, text = '7', width = 3, command = lambda:call('7')).grid(row = 2, column = 0)
	Button(root, text = '8', width = 3, command = lambda:call('8')).grid(row = 2, column = 1)
	Button(root, text = '9', width = 3, command = lambda:call('9')).grid(row = 2, column = 2)
	Button(root, text = '-', width = 3, command = lambda:call('-')).grid(row = 2, column = 3)
	Button(root, text = '4', width = 3, command = lambda:call('4')).grid(row = 3, column = 0)
	Button(root, text = '5', width = 3, command = lambda:call('5')).grid(row = 3, column = 1)
	Button(root, text = '6', width = 3, command = lambda:call('6')).grid(row = 3, column = 2)
	Button(root, text = '+', width = 3, command = lambda:call('+')).grid(row = 3, column = 3)
	Button(root, text = '1', width = 3, command = lambda:call('1')).grid(row = 4, column = 0)
	Button(root, text = '2', width = 3, command = lambda:call('2')).grid(row = 4, column = 1)
	Button(root, text = '3', width = 3, command = lambda:call('3')).grid(row = 4, column = 2)
	Button(root, text = '=', width = 3, bg = '#EF7321', height = 3,command = lambda:calculate()).grid(row = 4, column = 3, rowspan = 2)
	Button(root, text = '0', width = 10, command = lambda:call('0')).grid(row = 5, column = 0, columnspan = 2)
	Button(root, text = '.', width = 3, command = lambda:call('.')).grid(row = 5, column = 2) 

	root.mainloop()
if __name__ == '__main__':
	main()
