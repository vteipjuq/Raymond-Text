# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui41.ui'
#
# Created: Fri Sep 15 22:38:45 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(650, 400)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
		self.verticalLayout_4.setContentsMargins(2, 5, 0, 0)
		self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		# self.frame = QtGui.QFrame(self.centralwidget)
		# self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
		# self.frame.setFrameShadow(QtGui.QFrame.Raised)
		# self.frame.setObjectName(_fromUtf8("frame"))
		# self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
		# self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		# self.label = QtGui.QLabel(self.frame)
		# self.label.setObjectName(_fromUtf8("label"))
		# self.verticalLayout_3.addWidget(self.label)
		# self.treeWidget = QtGui.QTreeWidget(self.frame)
		# self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
		# item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
		# item_1 = QtGui.QTreeWidgetItem(item_0)
		# item_2 = QtGui.QTreeWidgetItem(item_1)
		# item_2 = QtGui.QTreeWidgetItem(item_1)
		# item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
		# item_1 = QtGui.QTreeWidgetItem(item_0)
		# item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
		# item_1 = QtGui.QTreeWidgetItem(item_0)
		# self.verticalLayout_3.addWidget(self.treeWidget)

		# self.listWidget = QtGui.QListWidget(self.frame)
		# self.listWidget.setObjectName(_fromUtf8("listWidget"))
		# item = QtGui.QListWidgetItem()
		# self.listWidget.addItem(item)
		# item = QtGui.QListWidgetItem()
		# self.listWidget.addItem(item)
		# item = QtGui.QListWidgetItem()
		# self.listWidget.addItem(item)
		# item = QtGui.QListWidgetItem()
		# self.listWidget.addItem(item)
		# item = QtGui.QListWidgetItem()
		# self.listWidget.addItem(item)
		# item = QtGui.QListWidgetItem()
		# self.listWidget.addItem(item)
		# self.verticalLayout_3.addWidget(self.listWidget)
		# self.horizontalLayout.addWidget(self.frame)

		self.tabWidget = QtGui.QTabWidget(self.centralwidget)
		#允许tab点击关闭
		self.tabWidget.setTabsClosable(True)
		#显示右键菜单
		# self.tabWidget.setContextMenuPolicy(3)
		#选项卡的形状
		self.tabWidget.setTabShape(1)
		# self.tab = QtGui.QWidget()
		# self.tab.setObjectName(_fromUtf8("tab"))
		# self.verticalLayout = QtGui.QVBoxLayout(self.tab)
		# self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		# self.textEdit = Qsci.QsciScintilla(self.tab)
		# self.textEdit.setToolTip(_fromUtf8(""))
		# self.textEdit.setWhatsThis(_fromUtf8(""))
		# self.textEdit.setObjectName(_fromUtf8("textEdit"))
		# self.verticalLayout.addWidget(self.textEdit)
		# self.tabWidget.addTab(self.tab, _fromUtf8(""))
		# self.tab_2 = QtGui.QWidget()
		# self.tab_2.setObjectName(_fromUtf8("tab_2"))
		# self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_2)
		# self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		# self.textEdit_2 = Qsci.QsciScintilla(self.tab_2)
		# self.textEdit_2.setToolTip(_fromUtf8(""))
		# self.textEdit_2.setWhatsThis(_fromUtf8(""))
		# self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
		# self.verticalLayout_2.addWidget(self.textEdit_2)
		# self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
		self.horizontalLayout.addWidget(self.tabWidget)
		self.horizontalLayout.setStretch(1, 100)
		self.verticalLayout_4.addLayout(self.horizontalLayout)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 26))
		self.menu = QtGui.QMenu(self.menubar)
		self.menu_2 = QtGui.QMenu(self.menubar)
		self.menu_3 = QtGui.QMenu(self.menubar)
		self.menu_4 = QtGui.QMenu(self.menubar)
		self.menu_5 = QtGui.QMenu(self.menubar)
		self.menu_6 = QtGui.QMenu(self.menubar)
		self.menu_7 = QtGui.QMenu(self.menubar)
		self.menu_8 = QtGui.QMenu(self.menubar)
		MainWindow.setMenuBar(self.menubar)

		self.statusbar = QtGui.QStatusBar(MainWindow)
		MainWindow.setStatusBar(self.statusbar)
		#----------文件----------#
		self.file_newFile = QtGui.QAction(MainWindow)
		self.file_newFile.setShortcut("Ctrl+N")
		self.file_openFile = QtGui.QAction(MainWindow)
		self.file_openFile.setShortcut("Ctrl+O")
		self.file_openFolder = QtGui.QAction(MainWindow)
		self.file_openRecentFile = QtGui.QAction(MainWindow)
		self.file_newLabelOpenFile = QtGui.QAction(MainWindow)
		self.file_save= QtGui.QAction(MainWindow)
		self.file_save.setShortcut("Ctrl+S")
		self.file_saveAs = QtGui.QAction(MainWindow)
		self.file_saveAs.setShortcut("Ctrl+Shift+S")
		self.file_setFileEncoding = QtGui.QAction(MainWindow)
		self.file_quit = QtGui.QAction(MainWindow)
		#----------end 文件----------#

		#----------编辑----------#
		self.edit_revoke = QtGui.QAction(MainWindow)
		self.edit_revoke.setShortcut("Ctrl+Z")
		self.edit_redo = QtGui.QAction(MainWindow)
		self.edit_redo.setShortcut("Ctrl+Y")
		self.edit_undo_selection = QtGui.QAction(MainWindow)
		self.edit_copy = QtGui.QAction(MainWindow)
		self.edit_copy.setShortcut("Ctrl+C")
		self.edit_shear = QtGui.QAction(MainWindow)
		self.edit_shear.setShortcut("Ctrl+X")
		self.edit_paste = QtGui.QAction(MainWindow)
		self.edit_paste.setShortcut("Ctrl+V")
		self.edit_record_paste = QtGui.QAction(MainWindow)
		#----------end 编辑----------#

		#----------选择----------#
		#----------end 选择----------#

		#----------查找----------#
		self.lookup_match_value = QtGui.QAction(MainWindow)
		self.lookup_match_value.setShortcut("Ctrl+V")
		self.lookup_next = QtGui.QAction(MainWindow)
		self.lookup_next.setShortcut("F3")
		self.lookup_prev = QtGui.QAction(MainWindow)
		self.lookup_prev.setShortcut("Shift+F3")
		self.lookup_replace_match_value = QtGui.QAction(MainWindow)
		self.lookup_replace_match_value.setShortcut("Ctrl+H")
		self.lookup_replace_next = QtGui.QAction(MainWindow)
		self.lookup_quick_find = QtGui.QAction(MainWindow)
		self.lookup_quick_find.setShortcut("Ctrl+F3")
		self.lookup_quick_find_all = QtGui.QAction(MainWindow)
		self.lookup_quick_find_all.setShortcut("Alt+F3")
		self.lookup_fast_selected_next = QtGui.QAction(MainWindow)
		self.lookup_fast_selected_next.setShortcut("Ctrl+D")
		self.lookup_fast_jumpTo_next = QtGui.QAction(MainWindow)
		self.lookup_fast_jumpTo_next.setShortcut("Ctrl+K,Ctrl+D")
		self.lookup_selected_lookup = QtGui.QAction(MainWindow)
		self.lookup_selected_replace = QtGui.QAction(MainWindow)
		self.lookup_selected_replace.setShortcut("Ctrl+Shift+E")
		self.lookup_file_search = QtGui.QAction(MainWindow)
		self.lookup_file_search.setShortcut("Ctrl+Shift+F")
		self.lookup_result = QtGui.QAction(MainWindow)
		#----------end 查找----------#

		#----------查看----------#
		#----------end 查看----------#

		#----------工具----------#
		#----------end 工具----------#

		#----------选项----------#
		#----------end 选项----------#

		#----------帮助----------#
		self.help_web = QtGui.QAction(MainWindow)
		self.help_about = QtGui.QAction(MainWindow)
		#----------end 帮助----------#

		self.menu.addAction(self.file_newFile)
		self.menu.addAction(self.file_openFile)
		self.menu.addAction(self.file_openFolder)
		self.menu.addAction(self.file_openRecentFile)
		self.menu.addAction(self.file_newLabelOpenFile)
		self.menu.addAction(self.file_save)
		self.menu.addAction(self.file_saveAs)
		self.menu.addSeparator()
		self.menu.addAction(self.file_setFileEncoding)
		self.menu.addSeparator()
		self.menu.addAction(self.file_quit)

		self.menu_2.addAction(self.edit_revoke)
		self.menu_2.addAction(self.edit_redo)
		self.menu_2.addAction(self.edit_undo_selection)
		self.menu_2.addSeparator()
		self.menu_2.addAction(self.edit_copy)
		self.menu_2.addAction(self.edit_shear)
		self.menu_2.addAction(self.edit_paste)
		self.menu_2.addAction(self.edit_record_paste)

		# self.menu_3.addAction(self.edit_record_paste)

		self.menu_4.addAction(self.lookup_match_value)
		self.menu_4.addAction(self.lookup_next)
		self.menu_4.addAction(self.lookup_prev)
		self.menu_4.addSeparator()
		self.menu_4.addAction(self.lookup_replace_match_value)
		self.menu_4.addAction(self.lookup_replace_next)
		self.menu_4.addSeparator()
		self.menu_4.addAction(self.lookup_quick_find)
		self.menu_4.addAction(self.lookup_quick_find_all)
		self.menu_4.addAction(self.lookup_fast_selected_next)
		self.menu_4.addAction(self.lookup_fast_jumpTo_next)
		self.menu_4.addSeparator()
		self.menu_4.addAction(self.lookup_selected_lookup)
		self.menu_4.addAction(self.lookup_selected_replace)
		self.menu_4.addSeparator()
		self.menu_4.addAction(self.lookup_file_search)
		self.menu_4.addAction(self.lookup_result)

		self.menu_8.addAction(self.help_web)
		self.menu_8.addAction(self.help_about)

		self.menubar.addAction(self.menu.menuAction())
		self.menubar.addAction(self.menu_2.menuAction())
		self.menubar.addAction(self.menu_3.menuAction())
		self.menubar.addAction(self.menu_4.menuAction())
		self.menubar.addAction(self.menu_5.menuAction())
		self.menubar.addAction(self.menu_6.menuAction())
		self.menubar.addAction(self.menu_7.menuAction())
		self.menubar.addAction(self.menu_8.menuAction())

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		# self.label.setText(_translate("MainWindow", "目录", None))
		# self.treeWidget.headerItem().setText(0, _translate("MainWindow", "1", None))
		# __sortingEnabled = self.treeWidget.isSortingEnabled()
		# self.treeWidget.setSortingEnabled(False)
		# self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "1111111111", None))
		# self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "2222222222", None))
		# self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "3333333", None))
		# self.treeWidget.topLevelItem(0).child(0).child(1).setText(0, _translate("MainWindow", "新建项目", None))
		# self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "44444444", None))
		# self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "55555555", None))
		# self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "666666666666", None))
		# self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "77777777", None))
		# self.treeWidget.setSortingEnabled(__sortingEnabled)
		# __sortingEnabled = self.listWidget.isSortingEnabled()
		# self.listWidget.setSortingEnabled(False)
		# item = self.listWidget.item(0)
		# item.setText(_translate("MainWindow", "111111111", None))
		# item = self.listWidget.item(1)
		# item.setText(_translate("MainWindow", "222222222222", None))
		# item = self.listWidget.item(2)
		# item.setText(_translate("MainWindow", "333333333333", None))
		# item = self.listWidget.item(3)
		# item.setText(_translate("MainWindow", "444444444444", None))
		# item = self.listWidget.item(4)
		# item.setText(_translate("MainWindow", "55555555555", None))
		# item = self.listWidget.item(5)
		# item.setText(_translate("MainWindow", "6666666666", None))
		# self.listWidget.setSortingEnabled(__sortingEnabled)
		# self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
		# self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
		self.menu.setTitle(_translate("MainWindow", "文件(F)", None))
		self.menu_2.setTitle(_translate("MainWindow", "编辑(E)", None))
		self.menu_3.setTitle(_translate("MainWindow", "选择(S)", None))
		self.menu_4.setTitle(_translate("MainWindow", "查找(I)", None))
		self.menu_5.setTitle(_translate("MainWindow", "查看(V)", None))
		self.menu_6.setTitle(_translate("MainWindow", "工具(T)", None))
		self.menu_7.setTitle(_translate("MainWindow", "首选项(N)", None))
		self.menu_8.setTitle(_translate("MainWindow", "帮助(H)", None))

		self.file_newFile.setText(_translate("MainWindow", "新建文件", None))
		self.file_openFile.setText(_translate("MainWindow", "打开文件", None))
		self.file_openFolder.setText(_translate("MainWindow", "打开文件夹", None))
		self.file_openRecentFile.setText(_translate("MainWindow", "打开最近的文件", None))
		self.file_newLabelOpenFile.setText(_translate("MainWindow", "新标签中打开当前文件", None))
		self.file_save.setText(_translate("MainWindow", "保存", None))
		self.file_saveAs.setText(_translate("MainWindow", "另存为", None))
		self.file_setFileEncoding.setText(_translate("MainWindow", "设置文件编码", None))
		self.file_quit.setText(_translate("MainWindow", "退出(X)", None))

		self.edit_revoke.setText(_translate("MainWindow", "撤销(U)", None))
		self.edit_redo.setText(_translate("MainWindow", "重做(R)", None))
		self.edit_undo_selection.setText(_translate("MainWindow", "撤销选择()", None))
		self.edit_copy.setText(_translate("MainWindow", "复制(C)", None))
		self.edit_shear.setText(_translate("MainWindow", "剪切(T)", None))
		self.edit_paste.setText(_translate("MainWindow", "粘贴(P)", None))
		self.edit_record_paste.setText(_translate("MainWindow", "从历史记录粘贴", None))

		self.lookup_match_value.setText(_translate("MainWindow", "查找匹配值...", None))
		self.lookup_next.setText(_translate("MainWindow", "查找下一个", None))
		self.lookup_prev.setText(_translate("MainWindow", "查找上一个", None))
		self.lookup_replace_match_value.setText(_translate("MainWindow", "替换匹配值...", None))
		self.lookup_replace_next.setText(_translate("MainWindow", "替换下一个", None))
		self.lookup_quick_find.setText(_translate("MainWindow", "快速查找", None))
		self.lookup_quick_find_all.setText(_translate("MainWindow", "快速查找全部", None))
		self.lookup_fast_selected_next.setText(_translate("MainWindow", "快速选中下一个", None))
		self.lookup_fast_jumpTo_next.setText(_translate("MainWindow", "快速跳至下一个", None))
		self.lookup_selected_lookup.setText(_translate("MainWindow", "在所选内容中查找", None))
		self.lookup_selected_replace.setText(_translate("MainWindow", "在所选内容中替换", None))
		self.lookup_file_search.setText(_translate("MainWindow", "在文件中查找...", None))
		self.lookup_result.setText(_translate("MainWindow", "查找结果", None))

		self.help_web.setText(_translate("MainWindow", "官方网站", None))
		self.help_about.setText(_translate("MainWindow", "关于我们", None))

from PyQt4 import Qsci
if __name__=="__main__":
	import sys
	app=QtGui.QApplication(sys.argv)
	uiw = QtGui.QMainWindow()
	ui=Ui_MainWindow()
	ui.setupUi(uiw)
	uiw.show()
	sys.exit(app.exec_())