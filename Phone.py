import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

from kivy.uix.button import Button
from kivy.uix.label import Label

import random

class MainWindow(Screen):
	pass

class CodeWindow(Screen):
	code = ObjectProperty(None)
	inputcode = ObjectProperty(None)

	def on_enter(self):
		self.codeText = [str(random.randint(1,9)) for i in range(6)]
		self.checkCode = self.codeText.copy()
		self.code.text = "The code: " + "".join(self.codeText)
		self.inputcode.text = "Input: "

	def btn1(self):
		if "1" == self.checkCode[0]:
			self.checkCode.pop(0)
			self.check()
			self.inputcode.text = self.inputcode.text + "1"
		else:
			self.checkCode = self.codeText.copy()
			
			self.inputcode.text = "Input: "

	def btn2(self):
		if "2" == self.checkCode[0]:
			self.checkCode.pop(0)
			self.check()
			self.inputcode.text = self.inputcode.text + "2"
		else:
			self.checkCode = self.codeText.copy()
			self.inputcode.text = "Input: "

	def btn3(self):
		if "3" == self.checkCode[0]:
			self.checkCode.pop(0)
			self.check()
			self.inputcode.text = self.inputcode.text + "3"
		else:
			self.checkCode = self.codeText.copy()
			self.inputcode.text = "Input: "

	def btn4(self):
		if "4" == self.checkCode[0]:
			self.checkCode.pop(0)
			self.check()
			self.inputcode.text = self.inputcode.text + "4"
		else:
			self.checkCode = self.codeText.copy()
			self.inputcode.text = "Input: "
	
	def btn5(self):
		if "5" == self.checkCode[0]:
			self.checkCode.pop(0)
			self.check()
			self.inputcode.text = self.inputcode.text + "5"
		else:
			self.checkCode = self.codeText.copy()
			self.inputcode.text = "Input: "
	
	def btn6(self):
		if "6" == self.checkCode[0]:
			self.checkCode.pop(0)
			self.check()
			self.inputcode.text = self.inputcode.text + "6"
		else:
			self.checkCode = self.codeText.copy()
			self.inputcode.text = "Input: "
	
	def btn7(self):
		if "7" == self.checkCode[0]:
			self.checkCode.pop(0)
			self.check()
			self.inputcode.text = self.inputcode.text + "7"
		else:
			self.checkCode = self.codeText.copy()
			self.inputcode.text = "Input: "
	
	def btn8(self):
		if "8" == self.checkCode[0]:
			self.checkCode.pop(0)
			self.check()
			self.inputcode.text = self.inputcode.text + "8"
		else:
			self.checkCode = self.codeText.copy()
			self.inputcode.text = "Input: "
	
	def btn9(self):
		if "9" == self.checkCode[0]:
			self.checkCode.pop(0)
			self.check()
			self.inputcode.text = self.inputcode.text + "9"
		else:
			self.checkCode = self.codeText.copy()
			self.inputcode.text = "Input: "
	
	def check(self):
		if len(self.checkCode) == 0:
			print('Completed')

	pass

class WindowManager(ScreenManager):
	pass

windows = Builder.load_file('windows.kv')

class main(App):
	def build(self):
		return windows

if __name__ == "__main__":
	main().run()