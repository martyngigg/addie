# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow.ui'
#
# Created: Thu Jun  9 14:56:05 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from ipythondockwidget import IPythonDockWidget
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
        MainWindow.resize(1269, 942)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_runNumber = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_runNumber.sizePolicy().hasHeightForWidth())
        self.lineEdit_runNumber.setSizePolicy(sizePolicy)
        self.lineEdit_runNumber.setObjectName(_fromUtf8("lineEdit_runNumber"))
        self.gridLayout_2.addWidget(self.lineEdit_runNumber, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.pushButton_setRunNumber = QtGui.QPushButton(self.centralwidget)
        self.pushButton_setRunNumber.setObjectName(_fromUtf8("pushButton_setRunNumber"))
        self.gridLayout_2.addWidget(self.pushButton_setRunNumber, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_6.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_6.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_6.addWidget(self.lineEdit_4, 3, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_6.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_6.addWidget(self.label_8, 4, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_6.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_6.addWidget(self.lineEdit_5, 4, 2, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_6.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_6.addWidget(self.label_7, 3, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_6.addWidget(self.pushButton_3, 1, 3, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_6.addWidget(self.lineEdit_3, 2, 2, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_6.addWidget(self.lineEdit_6, 5, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_6.addWidget(self.label_9, 5, 0, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout_6.addWidget(self.checkBox_2, 2, 3, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout_6.addWidget(self.checkBox_3, 3, 3, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout_6.addWidget(self.checkBox_4, 4, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.tab)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_bragg = QtGui.QWidget()
        self.tab_bragg.setObjectName(_fromUtf8("tab_bragg"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_bragg)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.tab_bragg)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.graphicsView_bragg = BraggView(self.tab_bragg)
        self.graphicsView_bragg.setObjectName(_fromUtf8("graphicsView_bragg"))
        self.verticalLayout_5.addWidget(self.graphicsView_bragg)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.comboBox_xUnit = QtGui.QComboBox(self.tab_bragg)
        self.comboBox_xUnit.setObjectName(_fromUtf8("comboBox_xUnit"))
        self.comboBox_xUnit.addItem(_fromUtf8(""))
        self.comboBox_xUnit.addItem(_fromUtf8(""))
        self.comboBox_xUnit.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.comboBox_xUnit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.pushButton_loadBraggFile = QtGui.QPushButton(self.tab_bragg)
        self.pushButton_loadBraggFile.setObjectName(_fromUtf8("pushButton_loadBraggFile"))
        self.verticalLayout_4.addWidget(self.pushButton_loadBraggFile)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        self.verticalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        self.verticalLayout_4.addItem(spacerItem3)
        self.checkBox_bank1 = QtGui.QCheckBox(self.tab_bragg)
        self.checkBox_bank1.setObjectName(_fromUtf8("checkBox_bank1"))
        self.verticalLayout_4.addWidget(self.checkBox_bank1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        self.verticalLayout_4.addItem(spacerItem4)
        self.checkBox_bank2 = QtGui.QCheckBox(self.tab_bragg)
        self.checkBox_bank2.setObjectName(_fromUtf8("checkBox_bank2"))
        self.verticalLayout_4.addWidget(self.checkBox_bank2)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        self.verticalLayout_4.addItem(spacerItem5)
        self.checkBox_bank3 = QtGui.QCheckBox(self.tab_bragg)
        self.checkBox_bank3.setObjectName(_fromUtf8("checkBox_bank3"))
        self.verticalLayout_4.addWidget(self.checkBox_bank3)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        self.verticalLayout_4.addItem(spacerItem6)
        self.checkBox_bank4 = QtGui.QCheckBox(self.tab_bragg)
        self.checkBox_bank4.setObjectName(_fromUtf8("checkBox_bank4"))
        self.verticalLayout_4.addWidget(self.checkBox_bank4)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        self.verticalLayout_4.addItem(spacerItem7)
        self.checkBox_bank5 = QtGui.QCheckBox(self.tab_bragg)
        self.checkBox_bank5.setObjectName(_fromUtf8("checkBox_bank5"))
        self.verticalLayout_4.addWidget(self.checkBox_bank5)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        self.verticalLayout_4.addItem(spacerItem8)
        self.checkBox_bank6 = QtGui.QCheckBox(self.tab_bragg)
        self.checkBox_bank6.setObjectName(_fromUtf8("checkBox_bank6"))
        self.verticalLayout_4.addWidget(self.checkBox_bank6)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.treeWidget_braggWSList = QtGui.QTreeWidget(self.tab_bragg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_braggWSList.sizePolicy().hasHeightForWidth())
        self.treeWidget_braggWSList.setSizePolicy(sizePolicy)
        self.treeWidget_braggWSList.setObjectName(_fromUtf8("treeWidget_braggWSList"))
        self.treeWidget_braggWSList.headerItem().setText(0, _fromUtf8("1"))
        self.horizontalLayout_4.addWidget(self.treeWidget_braggWSList)
        self.tabWidget.addTab(self.tab_bragg, _fromUtf8(""))
        self.tab_gR = QtGui.QWidget()
        self.tab_gR.setObjectName(_fromUtf8("tab_gR"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_gR)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton_loadSQ = QtGui.QPushButton(self.tab_gR)
        self.pushButton_loadSQ.setObjectName(_fromUtf8("pushButton_loadSQ"))
        self.verticalLayout_2.addWidget(self.pushButton_loadSQ)
        self.radioButton_sq = QtGui.QRadioButton(self.tab_gR)
        self.radioButton_sq.setObjectName(_fromUtf8("radioButton_sq"))
        self.verticalLayout_2.addWidget(self.radioButton_sq)
        self.radioButton_sqm1 = QtGui.QRadioButton(self.tab_gR)
        self.radioButton_sqm1.setObjectName(_fromUtf8("radioButton_sqm1"))
        self.verticalLayout_2.addWidget(self.radioButton_sqm1)
        self.radioButton_qsqm1 = QtGui.QRadioButton(self.tab_gR)
        self.radioButton_qsqm1.setObjectName(_fromUtf8("radioButton_qsqm1"))
        self.verticalLayout_2.addWidget(self.radioButton_qsqm1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.labelQmax = QtGui.QLabel(self.tab_gR)
        self.labelQmax.setObjectName(_fromUtf8("labelQmax"))
        self.gridLayout_4.addWidget(self.labelQmax, 1, 0, 1, 1)
        self.doubleSpinBoxQmax = QtGui.QDoubleSpinBox(self.tab_gR)
        self.doubleSpinBoxQmax.setMinimum(1.0)
        self.doubleSpinBoxQmax.setMaximum(50.0)
        self.doubleSpinBoxQmax.setSingleStep(0.5)
        self.doubleSpinBoxQmax.setObjectName(_fromUtf8("doubleSpinBoxQmax"))
        self.gridLayout_4.addWidget(self.doubleSpinBoxQmax, 1, 1, 1, 1)
        self.doubleSpinBoxQmin = QtGui.QDoubleSpinBox(self.tab_gR)
        self.doubleSpinBoxQmin.setMinimum(0.01)
        self.doubleSpinBoxQmin.setMaximum(10.0)
        self.doubleSpinBoxQmin.setSingleStep(0.01)
        self.doubleSpinBoxQmin.setObjectName(_fromUtf8("doubleSpinBoxQmin"))
        self.gridLayout_4.addWidget(self.doubleSpinBoxQmin, 0, 1, 1, 1)
        self.labelQmin = QtGui.QLabel(self.tab_gR)
        self.labelQmin.setObjectName(_fromUtf8("labelQmin"))
        self.gridLayout_4.addWidget(self.labelQmin, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab_gR)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 3, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.tab_gR)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_4.addWidget(self.checkBox, 3, 1, 1, 1)
        self.pushButton_showQMinMax = QtGui.QPushButton(self.tab_gR)
        self.pushButton_showQMinMax.setObjectName(_fromUtf8("pushButton_showQMinMax"))
        self.gridLayout_4.addWidget(self.pushButton_showQMinMax, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.pushButton_generateGR = QtGui.QPushButton(self.tab_gR)
        self.pushButton_generateGR.setObjectName(_fromUtf8("pushButton_generateGR"))
        self.gridLayout_7.addWidget(self.pushButton_generateGR, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_7)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem10)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.treeWidget_grWsList = GofRTree(self.tab_gR)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_grWsList.sizePolicy().hasHeightForWidth())
        self.treeWidget_grWsList.setSizePolicy(sizePolicy)
        self.treeWidget_grWsList.setObjectName(_fromUtf8("treeWidget_grWsList"))
        self.verticalLayout_3.addWidget(self.treeWidget_grWsList)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.labelRmin = QtGui.QLabel(self.tab_gR)
        self.labelRmin.setObjectName(_fromUtf8("labelRmin"))
        self.gridLayout_3.addWidget(self.labelRmin, 0, 0, 1, 1)
        self.labeldelR = QtGui.QLabel(self.tab_gR)
        self.labeldelR.setObjectName(_fromUtf8("labeldelR"))
        self.gridLayout_3.addWidget(self.labeldelR, 0, 2, 1, 1)
        self.labelRmax = QtGui.QLabel(self.tab_gR)
        self.labelRmax.setObjectName(_fromUtf8("labelRmax"))
        self.gridLayout_3.addWidget(self.labelRmax, 0, 4, 1, 1)
        self.doubleSpinBoxRmin = QtGui.QDoubleSpinBox(self.tab_gR)
        self.doubleSpinBoxRmin.setMinimum(0.1)
        self.doubleSpinBoxRmin.setMaximum(4.0)
        self.doubleSpinBoxRmin.setSingleStep(0.1)
        self.doubleSpinBoxRmin.setObjectName(_fromUtf8("doubleSpinBoxRmin"))
        self.gridLayout_3.addWidget(self.doubleSpinBoxRmin, 1, 0, 1, 1)
        self.doubleSpinBoxDelR = QtGui.QDoubleSpinBox(self.tab_gR)
        self.doubleSpinBoxDelR.setMinimum(0.01)
        self.doubleSpinBoxDelR.setMaximum(1.0)
        self.doubleSpinBoxDelR.setSingleStep(0.01)
        self.doubleSpinBoxDelR.setProperty("value", 0.1)
        self.doubleSpinBoxDelR.setObjectName(_fromUtf8("doubleSpinBoxDelR"))
        self.gridLayout_3.addWidget(self.doubleSpinBoxDelR, 1, 2, 1, 1)
        self.doubleSpinBoxRmax = QtGui.QDoubleSpinBox(self.tab_gR)
        self.doubleSpinBoxRmax.setMinimum(5.0)
        self.doubleSpinBoxRmax.setMaximum(100.0)
        self.doubleSpinBoxRmax.setProperty("value", 20.0)
        self.doubleSpinBoxRmax.setObjectName(_fromUtf8("doubleSpinBoxRmax"))
        self.gridLayout_3.addWidget(self.doubleSpinBoxRmax, 1, 4, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.pushButton_saveGR = QtGui.QPushButton(self.tab_gR)
        self.pushButton_saveGR.setObjectName(_fromUtf8("pushButton_saveGR"))
        self.verticalLayout_3.addWidget(self.pushButton_saveGR)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 4, 2, 1, 1)
        self.graphicsView_gr = GofRView(self.tab_gR)
        self.graphicsView_gr.setMinimumSize(QtCore.QSize(0, 300))
        self.graphicsView_gr.setObjectName(_fromUtf8("graphicsView_gr"))
        self.gridLayout_5.addWidget(self.graphicsView_gr, 4, 0, 1, 1)
        self.graphicsView_sq = SofQView(self.tab_gR)
        self.graphicsView_sq.setMinimumSize(QtCore.QSize(0, 300))
        self.graphicsView_sq.setObjectName(_fromUtf8("graphicsView_sq"))
        self.gridLayout_5.addWidget(self.graphicsView_sq, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab_gR, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1269, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_ipython = IPythonDockWidget(MainWindow)
        self.dockWidget_ipython.setMaximumSize(QtCore.QSize(524287, 300))
        self.dockWidget_ipython.setObjectName(_fromUtf8("dockWidget_ipython"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.dockWidget_ipython.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_ipython)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Run Numbers", None))
        self.pushButton_setRunNumber.setText(_translate("MainWindow", "Set", None))
        self.pushButton.setText(_translate("MainWindow", "Reduce Bragg", None))
        self.groupBox.setTitle(_translate("MainWindow", "Reduction Template", None))
        self.label_4.setText(_translate("MainWindow", "Calibration File", None))
        self.label_5.setText(_translate("MainWindow", "Characterization File", None))
        self.label_6.setText(_translate("MainWindow", "Empty Run Correction", None))
        self.label_8.setText(_translate("MainWindow", "Vanadium Background Run Correction", None))
        self.pushButton_2.setText(_translate("MainWindow", "Browse", None))
        self.label_7.setText(_translate("MainWindow", "Vanadium Run Correction", None))
        self.pushButton_3.setText(_translate("MainWindow", "Browse", None))
        self.label_9.setText(_translate("MainWindow", "ResampleX", None))
        self.checkBox_2.setText(_translate("MainWindow", "Disable", None))
        self.checkBox_3.setText(_translate("MainWindow", "Disable", None))
        self.checkBox_4.setText(_translate("MainWindow", "Disable", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Sample", None))
        self.pushButton_4.setText(_translate("MainWindow", "Reduce PDF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Reduce Data", None))
        self.label_3.setText(_translate("MainWindow", "SNS Powder Reduction Configuration for NOMAD", None))
        self.comboBox_xUnit.setItemText(0, _translate("MainWindow", "TOF", None))
        self.comboBox_xUnit.setItemText(1, _translate("MainWindow", "d-Spacing", None))
        self.comboBox_xUnit.setItemText(2, _translate("MainWindow", "Q", None))
        self.pushButton_loadBraggFile.setToolTip(_translate("MainWindow", "<html><head/><body><p>Load GSS/S(Q)/general 3-column ASCII</p><p>1. GSS: load and then split to 6 workspaces with single spectrum.  Finally group all 6 workspaces to a workspace group</p></body></html>", None))
        self.pushButton_loadBraggFile.setText(_translate("MainWindow", "Load", None))
        self.checkBox_bank1.setText(_translate("MainWindow", "Bank 1", None))
        self.checkBox_bank2.setText(_translate("MainWindow", "Bank 2", None))
        self.checkBox_bank3.setText(_translate("MainWindow", "Bank 3", None))
        self.checkBox_bank4.setText(_translate("MainWindow", "Bank 4", None))
        self.checkBox_bank5.setText(_translate("MainWindow", "Bank 5", None))
        self.checkBox_bank6.setText(_translate("MainWindow", "Bank 6", None))
        self.treeWidget_braggWSList.setToolTip(_translate("MainWindow", "<html><head/><body><p>List of workspace names.  Each workspace is an individual bank</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_bragg), _translate("MainWindow", "Bragg Peaks", None))
        self.pushButton_loadSQ.setToolTip(_translate("MainWindow", "<html><head/><body><p>Load S(Q) from the reduction tab. Plot S(Q), S(Q)-1 or Q[S(Q)-1] according to the selected radio buttons below.</p><p><span style=\" font-weight:600;\">Use regular file loader at this phase.</span></p><p>Duplicate the function in FastGR/scripts/fastgr</p><p>149     def read_SQ_file(self):</p><p><br/></p></body></html>", None))
        self.pushButton_loadSQ.setText(_translate("MainWindow", "Load SQ", None))
        self.radioButton_sq.setText(_translate("MainWindow", "S(Q)", None))
        self.radioButton_sqm1.setText(_translate("MainWindow", "S(Q)-1", None))
        self.radioButton_qsqm1.setText(_translate("MainWindow", "Q[S(Q)-1]", None))
        self.labelQmax.setText(_translate("MainWindow", "Qmax", None))
        self.labelQmin.setText(_translate("MainWindow", "Qmin", None))
        self.label_2.setText(_translate("MainWindow", "More Options ...", None))
        self.checkBox.setText(_translate("MainWindow", "CheckBox", None))
        self.pushButton_showQMinMax.setToolTip(_translate("MainWindow", "<html><head/><body><p>Show or hide the vertical indicators for Qmin and Qmax</p></body></html>", None))
        self.pushButton_showQMinMax.setText(_translate("MainWindow", "Show Min/Max", None))
        self.pushButton_generateGR.setText(_translate("MainWindow", "Generate GR", None))
        self.treeWidget_grWsList.setToolTip(_translate("MainWindow", "<html><head/><body><p>write click on the workspace name should give user the option to plot/over plot </p></body></html>", None))
        self.labelRmin.setText(_translate("MainWindow", "Rmin", None))
        self.labeldelR.setText(_translate("MainWindow", "deltaR", None))
        self.labelRmax.setText(_translate("MainWindow", "Rmax", None))
        self.pushButton_saveGR.setText(_translate("MainWindow", "Save GR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_gR), _translate("MainWindow", "Calculate G(R)", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))

from graphicviewlib import SofQView, BraggView, GofRView
from treelib import GofRTree
