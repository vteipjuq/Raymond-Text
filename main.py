#-*- coding:utf-8 -*-
#------------------------------------------------------------
#程序作者：raymond
#开发日期：2017-09-15
#功能描述：代码编辑器
#注意事项：没有
#更新历史：没有
#------------------------------------------------------------

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from PyQt4 import QtGui,QtCore
from PyQt4.Qsci import QsciScintilla, QsciLexerPython
from MainWindow_ui import Ui_MainWindow
import os
from functools import partial
from sqlite3 import connect,Row

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class HorizontalTabBar(QtGui.QTabBar):
	def __init__(self, *args, **kwargs):
		super(HorizontalTabBar, self).__init__(*args, **kwargs)
	# def __init__(self,parent = None):  
	# 	QtGui.QTabBar.__init__(self,parent)  
		#显示右键菜单
		self.setContextMenuPolicy(3)
		self.customContextMenuRequested.connect(self.addItemMenu)
	#分组右键菜单
	def addItemMenu(self):
		self.popMenu = QtGui.QMenu()
		self.popMenu.setStyleSheet("QMenu{background:#fff;border:1px solid #C4C4C4;}QMenu:item{padding:6px 70px 6px 30px;}QMenu:item:selected:enabled{background:lightgray;color:#000}QMenu:item:selected:!enabled{background:transparent;}QMenu:separator{margin:1px 1px 1px 1px;}" )
		self.additem = self.popMenu.addAction(u'新建分组')
		# self.sortRight = self.popMenu.addAction(u'按名称排序')
		self.rename = self.popMenu.addAction(u'重命名')
		self.delPacket = self.popMenu.addAction(u'删除分组')
		self.popMenu.move(QtGui.QCursor.pos())
		self.popMenu.show()
		
		self.additem.triggered.connect(self.ss)
		# self.sortRight.triggered.connect(self.addItem)
		self.rename.triggered.connect(self.ss)
		self.delPacket.triggered.connect(self.ss)
	def ss(self):
		self.emit(QtCore.SIGNAL("tabCloseRequested(int)"),1) 

class MainClass(QtGui.QMainWindow,Ui_MainWindow,QsciScintilla):
	def __init__(self,parent=None):
		super(MainClass, self).__init__(parent)
		self.setupUi(self)
		self.setAcceptDrops(True)#拖拽
		self.setWindowIcon(QtGui.QIcon('image/Raymond_logo.png'))
		# self.setWindowTitle(u"Raymond")
		self.dataBaseName="RaymondText.db"
		self.newFile(0)
		self.setTextEdit()
		#所有信号与槽都放在这里
		self.signalsAndSlots()

	#----------所有信号与槽都放在这里----------#
	def signalsAndSlots(self):
		self.file_newFile.triggered.connect(self.newFile)
		self.file_openFile.triggered.connect(self.openFile)
		self.file_save.triggered.connect(self.saveFile)
		self.connect(self.tabWidget, QtCore.SIGNAL("tabCloseRequested(int)"),self.closeTab)
		self.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"),self.getTabData,)
		



		# self.connect(self.file_newFile, QtCore.SIGNAL('clicked()'), self.newFile)
	#----------end 所有信号与槽都放在这里----------#
	#拖拽处理函数
	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls():
			event.acceptProposedAction()
			# for url in event.mimeData().urls():
				#url=str(url.toLocalFile()).decode('UTF-8').encode('GBK')
		else:
			super(MainClass, self).dragEnterEvent(event)

	def dragMoveEvent(self, event):
		super(MainClass, self).dragMoveEvent(event)
		
	#拖拽释放处理函数
	def dropEvent(self, event):
		if event.mimeData().hasUrls():
			for url in event.mimeData().urls():
				file=str(url.toLocalFile()).decode('UTF-8')
				self.newFile(file)
		else:
			super(MainClass,self).dropEvent(event)

#==========文件菜单中所有功能==========#
	#----------新建文件----------#
	def newFile(self,file):
		# self.tabWidget.setTabBar(HorizontalTabBar())
		#获取QtabBar id信号槽
		self.NewTab = QtGui.QWidget()
		#显示右键菜单
		self.NewTab.setContextMenuPolicy(3)
		self.NewTab.customContextMenuRequested.connect(self.TabRightMenu)
		self.loxLayout = QtGui.QVBoxLayout(self.NewTab)
		self.loxLayout.setContentsMargins(0, 0, 0, 0)
		self.textEdit = QsciScintilla(self.NewTab)
		self.textEdit.setToolTip(_fromUtf8(""))
		self.textEdit.setWhatsThis(_fromUtf8(""))
		if file:
			self.loxLayout.addWidget(self.textEdit)
			self.tabWidget.addTab(self.NewTab, _fromUtf8(""))
			self.textEdit.setText(open(file,'r').read())
			#获取文件名称
			file_name = os.path.basename(file)
			self.tabWidget.setTabText(self.tabWidget.indexOf(self.NewTab), _translate("MainWindow", file_name, None))
			self.setWindowTitle(file+"  - Raymond Text")
		else:
			self.loxLayout.addWidget(self.textEdit)
			self.tabWidget.addTab(self.NewTab, _fromUtf8(""))
			self.tabWidget.setTabText(self.tabWidget.indexOf(self.NewTab), _translate("MainWindow", "新建文件", None))
			self.setWindowTitle(u"Raymond Text")
		# self.tabWidget.setStatusTip(u'行 113, 列 55')
		self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex()+1)
		self.setTextEdit()
	#----------end 新建文件----------#
	#----------打开文件----------#
	def openFile(self):
		file_path =  QtGui.QFileDialog.getOpenFileName(self,u'打开文件',"" ,u"All Files(*.*);;纯文本 (*.txt)")
		self.setWindowTitle(file_path+"  - Raymond Text")
		self.NewTab = QtGui.QWidget()
		#显示右键菜单
		self.NewTab.customContextMenuRequested.connect(self.TabRightMenu)
		self.loxLayout = QtGui.QVBoxLayout(self.NewTab)
		self.loxLayout.setContentsMargins(0, 0, 0, 0)
		self.textEdit = QsciScintilla(self.NewTab)
		self.textEdit.setToolTip(_fromUtf8(""))
		self.textEdit.setWhatsThis(_fromUtf8(""))
		if file_path:
			self.loxLayout.addWidget(self.textEdit)
			self.tabWidget.addTab(self.NewTab, _fromUtf8(""))
			self.textEdit.setText(open(file_path,'r').read())
			#获取文件名称
			file_name=os.path.basename(str(file_path))
			con=connect(self.dataBaseName)
			cur=con.cursor()
			res=(file_name,str(file_path),0,0)
			cur.execute('insert into grouping_data (name,address,groupid,iconPath) values (?,?,?,?)',res)
			con.commit()
			con.close()
			self.tabWidget.setTabText(self.tabWidget.indexOf(self.NewTab), _translate("MainWindow", file_name, None))
			self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex()+1)
			self.setTextEdit()
		
	#----------end 打开文件----------#

	#----------保存文件----------#
	def saveFile(self):
		#获取空口标题
		# print self.windowTitle()
		print self.textEdit.toPlainText()
	#----------end 保存文件----------#
	#----------另存为文件----------#
	def saveAsFile(self):
		file_path =  QtGui.QFileDialog.getSaveFileName(self,u'另存为',"" ,u"All Files(*.*);;纯文本 (*.txt)")
		if file_path:
			fp = open(file_path,"w")     #直接打开一个文件，如果文件不存在则创建文件
			for row in cur:
				data="名称："+row[1]+"      密码："+row[2]+"\n"
				print data
				fp.writelines(data)
			fp.close()
	#----------end 另存为文件----------#



#==========end 文件菜单中所有功能==========#

#==========编辑菜单中所有功能==========#
#==========end 编辑菜单中所有功能==========#
	#----------------------杂项.功能--------------------#
	#设置textEdit字体，行号，颜色
	def setTextEdit(self):
		# 设置默认字体
		font = QtGui.QFont()
		font.setFamily('Courier')
		font.setFixedPitch(True)
		font.setPointSize(12)
		self.textEdit.setFont(font)
		self.textEdit.setMarginsFont(font)
		# Margin 0用于行号
		fontmetrics = QtGui.QFontMetrics(font)
		# self.textEdit.setMarginsFont(font)
		# 行号宽度
		# self.textEdit.setMarginWidth(0, fontmetrics.width("00000") + 6)
		self.textEdit.setMarginWidth(0, 60)
		# self.textEdit.setMarginLineNumbers(0, True)
		# 行号背景色
		self.textEdit.setMarginsBackgroundColor(QtGui.QColor("#C7EDCC"))
		# 行号字体颜色
		self.textEdit.setMarginsForegroundColor(QtGui.QColor("#000000"))
		# 高亮当前行与特殊的背景颜色
		self.textEdit.setCaretLineVisible(True)
		self.textEdit.setCaretLineBackgroundColor(QtGui.QColor("#C7EDCC"))
		#光标颜色
		self.textEdit.setCaretForegroundColor(QtGui.QColor("white"))
		#选择字体的背景颜色
		self.textEdit.setSelectionBackgroundColor(QtGui.QColor("#606060"))
		#选择字体的颜色
		self.textEdit.setSelectionForegroundColor(QtGui.QColor("#FFFFFF"))
		#折叠边缘
		self.textEdit.setFolding(QsciScintilla.PlainFoldStyle)
		self.textEdit.setMarginWidth(2,12)
		#括号匹配
		self.textEdit.setBraceMatching(QsciScintilla.StrictBraceMatch)


		#不要看到所有的水平滚动条
		#在这里使用原始消息给Scintilla（所有消息都记录
		#在这里＃这里：http://www.scintilla.org/ScintillaDoc.html）
		self.textEdit.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR,0)

	#删除TabWidget中的tab
	def closeTab(self,tabId):
		#关闭置顶信号槽  
		self.tabWidget.removeTab(tabId)
	#获取tab中的数据
	def getTabData(self,tabId):
		if self.tabWidget.tabText(tabId)==u"新建文件":
			self.setWindowTitle(u"新建文件  - Raymond Text")
		else:
			con=connect(self.dataBaseName)
			cur=con.cursor()
			cur.execute('select * from grouping_data where name="%s"'%self.tabWidget.tabText(tabId))
			row=cur.fetchall()
			self.setWindowTitle(row[0][2]+"  - Raymond Text")
			con.commit()
			con.close()
	#tab右键菜单
	def TabRightMenu(self,id):
		self.popMenu = QtGui.QMenu()
		self.popMenu.setStyleSheet("QMenu{background:#fff;border:1px solid #C4C4C4;}QMenu:item{padding:6px 70px 6px 30px;}QMenu:item:selected:enabled{background:#EAEAEA;color:#000}QMenu:item:selected:!enabled{background:transparent;}QMenu:separator{margin:1px 1px 1px 1px;}" )
		self.rc_close = self.popMenu.addAction(u'关闭')
		self.rc_close_other = self.popMenu.addAction(u'关闭其它')
		self.rc_close_right_label = self.popMenu.addAction(u'关闭右侧标签')
		self.rc_new_file = self.popMenu.addAction(u'新建文件')
		self.rc_open_file = self.popMenu.addAction(u'打开文件')
		self.popMenu.move(QtGui.QCursor.pos())
		self.popMenu.show()
		
		self.rc_close.triggered.connect(self.addItem)
		self.rc_close_other.triggered.connect(self.addItem)
		self.rc_close_right_label.triggered.connect(self.addItem)
		self.rc_new_file.triggered.connect(self.addItem)
		self.rc_open_file.triggered.connect(self.addItem)
	def addItem(self):
		print "rc"
	#----------------------end 杂项.功能--------------------#


if __name__ == "__main__":
	app=QtGui.QApplication(sys.argv)
	# 加载样式
	with open('qss/qss.qss', 'r') as qss:
		app.setStyleSheet(qss.read())
	ui=MainClass()
	ui.show()
	sys.exit(app.exec_())