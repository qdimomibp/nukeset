#coding:utf8
import os
from PySide2.QtWidgets import *

class CheckEnv(Qwidget):
	def __init__(self):
	super(CheckEnv, self).__init__()
	self.layout = QVBoxLayout()
	self.setLayout(self.layout)
	self.setEnv()

	def setEnv(self):
		envs= ["USER", "OCIO", "NUKE_PATH", "NUKE_FON_TPATH"]
		for e in envs:
			self.layout.addWidget(QLable())
