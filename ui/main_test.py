# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.treeWidget = QtWidgets.QTreeWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.horizontalLayout_4.addWidget(self.treeWidget)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.textEdit = QtWidgets.QTextEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setObjectName("tabWidget_2")
#         self.tab_3 = QtWidgets.QWidget()
#         self.tab_3.setObjectName("tab_3")
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_3)
#         self.horizontalLayout_3.setObjectName("horizontalLayout_3")
#         self.tableView = QtWidgets.QTableView(self.tab_3)
#         self.tableView.setObjectName("tableView")
#         self.horizontalLayout_3.addWidget(self.tableView)
#         self.tabWidget_2.addTab(self.tab_3, "")
#         self.tab_4 = QtWidgets.QWidget()
#         self.tab_4.setObjectName("tab_4")
#         self.tabWidget_2.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
#         self.toolButton_2 = QtWidgets.QToolButton(self.tab)
#         self.toolButton_2.setObjectName("toolButton_2")
#         self.horizontalLayout.addWidget(self.toolButton_2)
#         self.toolButton = QtWidgets.QToolButton(self.tab)
#         self.toolButton.setObjectName("toolButton")
#         self.horizontalLayout.addWidget(self.toolButton)
#         self.toolButton_3 = QtWidgets.QToolButton(self.tab)
#         self.toolButton_3.setObjectName("toolButton_3")
#         self.horizontalLayout.addWidget(self.toolButton_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab, "")
#         self.tab_2 = QtWidgets.QWidget()
#         self.tab_2.setObjectName("tab_2")
#         self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_new = QtWidgets.QAction(MainWindow)
        self.action_new.setObjectName("action_new")
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_import = QtWidgets.QAction(MainWindow)
        self.action_import.setObjectName("action_import")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_QT = QtWidgets.QAction(MainWindow)
        self.action_QT.setObjectName("action_QT")
        self.menu_F.addAction(self.action_new)
        self.menu_F.addAction(self.action_open)
        self.menu_F.addAction(self.action_import)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_QT)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mysql管理工具"))
#         self.pushButton.setText(_translate("MainWindow", "执行"))
#         self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
#         self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
#         self.toolButton_2.setText(_translate("MainWindow", "..."))
#         self.toolButton.setText(_translate("MainWindow", "..."))
#         self.toolButton_3.setText(_translate("MainWindow", "..."))
#         self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
#         self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
#         self.menu_F.setTitle(_translate("MainWindow", "文件(&F)"))
#         self.menu.setTitle(_translate("MainWindow", "帮助(H)"))
#         self.action_new.setText(_translate("MainWindow", "新建(&N)"))
#         self.action_open.setText(_translate("MainWindow", "打开(&O)"))
#         self.action_import.setText(_translate("MainWindow", "导入(&I)"))
#         self.action.setText(_translate("MainWindow", "关于我们"))
#         self.action_QT.setText(_translate("MainWindow", "关于QT"))











if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()

    sys.exit(app.exec_())