# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_editSq.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(859, 298)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox_workspaces = QtGui.QComboBox(Dialog)
        self.comboBox_workspaces.setObjectName(_fromUtf8("comboBox_workspaces"))
        self.comboBox_workspaces.addItem(_fromUtf8(""))
        self.comboBox_workspaces.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox_workspaces)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_shift = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_shift.sizePolicy().hasHeightForWidth())
        self.lineEdit_shift.setSizePolicy(sizePolicy)
        self.lineEdit_shift.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_shift.setObjectName(_fromUtf8("lineEdit_shift"))
        self.gridLayout.addWidget(self.lineEdit_shift, 0, 1, 1, 1)
        self.lineEdit_scaleFactor = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_scaleFactor.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_scaleFactor.setObjectName(_fromUtf8("lineEdit_scaleFactor"))
        self.gridLayout.addWidget(self.lineEdit_scaleFactor, 1, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalSlider_shift = QtGui.QSlider(self.groupBox)
        self.horizontalSlider_shift.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_shift.setObjectName(_fromUtf8("horizontalSlider_shift"))
        self.horizontalLayout.addWidget(self.horizontalSlider_shift)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalSlider_scale = QtGui.QSlider(self.groupBox)
        self.horizontalSlider_scale.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_scale.setObjectName(_fromUtf8("horizontalSlider_scale"))
        self.horizontalLayout_2.addWidget(self.horizontalSlider_scale)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 3, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_editSQ = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_editSQ.setFont(font)
        self.pushButton_editSQ.setObjectName(_fromUtf8("pushButton_editSQ"))
        self.gridLayout.addWidget(self.pushButton_editSQ, 0, 2, 1, 1)
        self.pushButton_cache = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cache.setFont(font)
        self.pushButton_cache.setObjectName(_fromUtf8("pushButton_cache"))
        self.gridLayout.addWidget(self.pushButton_cache, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_shiftMin = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_shiftMin.sizePolicy().hasHeightForWidth())
        self.lineEdit_shiftMin.setSizePolicy(sizePolicy)
        self.lineEdit_shiftMin.setMaximumSize(QtCore.QSize(80, 80))
        self.lineEdit_shiftMin.setObjectName(_fromUtf8("lineEdit_shiftMin"))
        self.gridLayout_2.addWidget(self.lineEdit_shiftMin, 0, 1, 1, 1)
        self.lineEdit_shiftMax = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_shiftMax.sizePolicy().hasHeightForWidth())
        self.lineEdit_shiftMax.setSizePolicy(sizePolicy)
        self.lineEdit_shiftMax.setMaximumSize(QtCore.QSize(80, 80))
        self.lineEdit_shiftMax.setObjectName(_fromUtf8("lineEdit_shiftMax"))
        self.gridLayout_2.addWidget(self.lineEdit_shiftMax, 0, 2, 1, 1)
        self.pushButton_setShiftRange = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_setShiftRange.setObjectName(_fromUtf8("pushButton_setShiftRange"))
        self.gridLayout_2.addWidget(self.pushButton_setShiftRange, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 4, 1, 1)
        self.lineEdit_scaleMin = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_scaleMin.sizePolicy().hasHeightForWidth())
        self.lineEdit_scaleMin.setSizePolicy(sizePolicy)
        self.lineEdit_scaleMin.setMaximumSize(QtCore.QSize(80, 80))
        self.lineEdit_scaleMin.setObjectName(_fromUtf8("lineEdit_scaleMin"))
        self.gridLayout_2.addWidget(self.lineEdit_scaleMin, 1, 1, 1, 1)
        self.lineEdit_scaleMax = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_scaleMax.sizePolicy().hasHeightForWidth())
        self.lineEdit_scaleMax.setSizePolicy(sizePolicy)
        self.lineEdit_scaleMax.setMaximumSize(QtCore.QSize(80, 80))
        self.lineEdit_scaleMax.setObjectName(_fromUtf8("lineEdit_scaleMax"))
        self.gridLayout_2.addWidget(self.lineEdit_scaleMax, 1, 2, 1, 1)
        self.pushButton_setScaleRange = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_setScaleRange.setObjectName(_fromUtf8("pushButton_setScaleRange"))
        self.gridLayout_2.addWidget(self.pushButton_setScaleRange, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton_saveNewSq = QtGui.QPushButton(Dialog)
        self.pushButton_saveNewSq.setObjectName(_fromUtf8("pushButton_saveNewSq"))
        self.horizontalLayout_3.addWidget(self.pushButton_saveNewSq)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_quit = QtGui.QPushButton(Dialog)
        self.pushButton_quit.setObjectName(_fromUtf8("pushButton_quit"))
        self.horizontalLayout_3.addWidget(self.pushButton_quit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.comboBox_workspaces.setItemText(0, _translate("Dialog", "workspace 1", None))
        self.comboBox_workspaces.setItemText(1, _translate("Dialog", "workspace 2", None))
        self.groupBox.setTitle(_translate("Dialog", "Edit S(Q)", None))
        self.lineEdit_shift.setText(_translate("Dialog", "0", None))
        self.lineEdit_scaleFactor.setText(_translate("Dialog", "1", None))
        self.label_2.setText(_translate("Dialog", "Scale", None))
        self.label.setText(_translate("Dialog", "Shift", None))
        self.pushButton_editSQ.setText(_translate("Dialog", "Edit S(Q)", None))
        self.pushButton_cache.setToolTip(_translate("Dialog", "<html><head/><body><p>Cache the edited S(Q)</p></body></html>", None))
        self.pushButton_cache.setText(_translate("Dialog", "Cache Edited", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Setup", None))
        self.label_3.setText(_translate("Dialog", "Shift Range", None))
        self.label_4.setText(_translate("Dialog", "Scale Range", None))
        self.pushButton_setShiftRange.setText(_translate("Dialog", "Set Range", None))
        self.pushButton_setScaleRange.setText(_translate("Dialog", "Set Range", None))
        self.pushButton_saveNewSq.setText(_translate("Dialog", "Save As", None))
        self.pushButton_quit.setText(_translate("Dialog", "Quit", None))

