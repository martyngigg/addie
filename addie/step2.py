# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/step2.ui'
#
# Created: Tue Jun 28 17:28:19 2016
#      by: PyQt4 UI code generator 4.10.1
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
        MainWindow.resize(1369, 712)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.populate_table = QtGui.QPushButton(self.centralwidget)
        self.populate_table.setObjectName(_fromUtf8("populate_table"))
        self.horizontalLayout.addWidget(self.populate_table)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.table = QtGui.QTableWidget(self.centralwidget)
        self.table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table.setAlternatingRowColors(True)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(9)
        self.table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, item)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setSortIndicatorShown(False)
        self.table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.table)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.background_no = QtGui.QRadioButton(self.groupBox_3)
        self.background_no.setMinimumSize(QtCore.QSize(50, 0))
        self.background_no.setMaximumSize(QtCore.QSize(50, 16777215))
        self.background_no.setChecked(True)
        self.background_no.setObjectName(_fromUtf8("background_no"))
        self.horizontalLayout_12.addWidget(self.background_no)
        self.background_no_field = QtGui.QLabel(self.groupBox_3)
        self.background_no_field.setMinimumSize(QtCore.QSize(300, 0))
        self.background_no_field.setObjectName(_fromUtf8("background_no_field"))
        self.horizontalLayout_12.addWidget(self.background_no_field)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setMaximumSize(QtCore.QSize(110, 16777215))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_12.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.background_yes = QtGui.QRadioButton(self.groupBox_3)
        self.background_yes.setObjectName(_fromUtf8("background_yes"))
        self.horizontalLayout_10.addWidget(self.background_yes)
        self.background_comboBox = QtGui.QComboBox(self.groupBox_3)
        self.background_comboBox.setEnabled(False)
        self.background_comboBox.setMinimumSize(QtCore.QSize(250, 0))
        self.background_comboBox.setObjectName(_fromUtf8("background_comboBox"))
        self.horizontalLayout_10.addWidget(self.background_comboBox)
        self.background_line_edit = QtGui.QLineEdit(self.groupBox_3)
        self.background_line_edit.setEnabled(False)
        self.background_line_edit.setMinimumSize(QtCore.QSize(200, 0))
        self.background_line_edit.setObjectName(_fromUtf8("background_line_edit"))
        self.horizontalLayout_10.addWidget(self.background_line_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.fourier_filter_from = QtGui.QLineEdit(self.groupBox)
        self.fourier_filter_from.setObjectName(_fromUtf8("fourier_filter_from"))
        self.horizontalLayout_8.addWidget(self.fourier_filter_from)
        self.label_8 = QtGui.QLabel(self.groupBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_8.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_8.addWidget(self.label_2)
        self.fourier_filter_to = QtGui.QLineEdit(self.groupBox)
        self.fourier_filter_to.setObjectName(_fromUtf8("fourier_filter_to"))
        self.horizontalLayout_8.addWidget(self.fourier_filter_to)
        self.label_6 = QtGui.QLabel(self.groupBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_8.addWidget(self.label_6)
        self.horizontalLayout_9.addWidget(self.groupBox)
        self.groupBox_7 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox_7)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.hydrogen_yes = QtGui.QRadioButton(self.groupBox_7)
        self.hydrogen_yes.setChecked(False)
        self.hydrogen_yes.setObjectName(_fromUtf8("hydrogen_yes"))
        self.horizontalLayout_2.addWidget(self.hydrogen_yes)
        self.hydrogen_no = QtGui.QRadioButton(self.groupBox_7)
        self.hydrogen_no.setChecked(True)
        self.hydrogen_no.setObjectName(_fromUtf8("hydrogen_no"))
        self.horizontalLayout_2.addWidget(self.hydrogen_no)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_4 = QtGui.QLabel(self.groupBox_7)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_11.addWidget(self.label_4)
        self.plazcek_fit_range_min = QtGui.QLineEdit(self.groupBox_7)
        self.plazcek_fit_range_min.setMinimumSize(QtCore.QSize(50, 0))
        self.plazcek_fit_range_min.setMaximumSize(QtCore.QSize(50, 16777215))
        self.plazcek_fit_range_min.setObjectName(_fromUtf8("plazcek_fit_range_min"))
        self.horizontalLayout_11.addWidget(self.plazcek_fit_range_min)
        self.label_9 = QtGui.QLabel(self.groupBox_7)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_9.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_11.addWidget(self.label_9)
        self.label_5 = QtGui.QLabel(self.groupBox_7)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_11.addWidget(self.label_5)
        self.plazcek_fit_range_max = QtGui.QLineEdit(self.groupBox_7)
        self.plazcek_fit_range_max.setMinimumSize(QtCore.QSize(50, 0))
        self.plazcek_fit_range_max.setMaximumSize(QtCore.QSize(50, 16777215))
        self.plazcek_fit_range_max.setObjectName(_fromUtf8("plazcek_fit_range_max"))
        self.horizontalLayout_11.addWidget(self.plazcek_fit_range_max)
        self.label_10 = QtGui.QLabel(self.groupBox_7)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_10.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_11.addWidget(self.label_10)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9.addWidget(self.groupBox_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(120, 0))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.muscat_yes = QtGui.QRadioButton(self.groupBox_4)
        self.muscat_yes.setObjectName(_fromUtf8("muscat_yes"))
        self.horizontalLayout_3.addWidget(self.muscat_yes)
        self.radioButton_12 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_12.setChecked(True)
        self.radioButton_12.setObjectName(_fromUtf8("radioButton_12"))
        self.horizontalLayout_3.addWidget(self.radioButton_12)
        self.horizontalLayout_6.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setMinimumSize(QtCore.QSize(120, 0))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.scale_data_yes = QtGui.QRadioButton(self.groupBox_5)
        self.scale_data_yes.setChecked(True)
        self.scale_data_yes.setObjectName(_fromUtf8("scale_data_yes"))
        self.horizontalLayout_4.addWidget(self.scale_data_yes)
        self.radioButton_14 = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_14.setChecked(False)
        self.radioButton_14.setObjectName(_fromUtf8("radioButton_14"))
        self.horizontalLayout_4.addWidget(self.radioButton_14)
        self.horizontalLayout_6.addWidget(self.groupBox_5)
        self.groupBox_6 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_6.setMinimumSize(QtCore.QSize(120, 0))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.run_rmc_yes = QtGui.QRadioButton(self.groupBox_6)
        self.run_rmc_yes.setChecked(True)
        self.run_rmc_yes.setObjectName(_fromUtf8("run_rmc_yes"))
        self.horizontalLayout_5.addWidget(self.run_rmc_yes)
        self.radioButton_16 = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton_16.setChecked(False)
        self.radioButton_16.setObjectName(_fromUtf8("radioButton_16"))
        self.horizontalLayout_5.addWidget(self.radioButton_16)
        self.horizontalLayout_6.addWidget(self.groupBox_6)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_21 = QtGui.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_21.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_7.addWidget(self.label_21)
        self.label_22 = QtGui.QLabel(self.centralwidget)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_7.addWidget(self.label_22)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.create_sample_properties_files_button = QtGui.QPushButton(self.centralwidget)
        self.create_sample_properties_files_button.setEnabled(False)
        self.create_sample_properties_files_button.setObjectName(_fromUtf8("create_sample_properties_files_button"))
        self.horizontalLayout_7.addWidget(self.create_sample_properties_files_button)
        self.run_ndabs_button = QtGui.QPushButton(self.centralwidget)
        self.run_ndabs_button.setEnabled(False)
        self.run_ndabs_button.setObjectName(_fromUtf8("run_ndabs_button"))
        self.horizontalLayout_7.addWidget(self.run_ndabs_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1369, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.populate_table, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.populate_table_clicked)
        QtCore.QObject.connect(self.hydrogen_yes, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.hidrogen_clicked)
        QtCore.QObject.connect(self.hydrogen_no, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.no_hidrogen_clicked)
        QtCore.QObject.connect(self.background_yes, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.yes_background_clicked)
        QtCore.QObject.connect(self.background_comboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.background_combobox_changed)
        QtCore.QObject.connect(self.create_sample_properties_files_button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.create_sample_properties_files_clicked)
        QtCore.QObject.connect(self.run_ndabs_button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.run_ndabs_clicked)
        QtCore.QObject.connect(self.fourier_filter_from, QtCore.SIGNAL(_fromUtf8("editingFinished()")), MainWindow.check_fourier_filter_widgets)
        QtCore.QObject.connect(self.fourier_filter_to, QtCore.SIGNAL(_fromUtf8("editingFinished()")), MainWindow.check_fourier_filter_widgets)
        QtCore.QObject.connect(self.plazcek_fit_range_min, QtCore.SIGNAL(_fromUtf8("editingFinished()")), MainWindow.check_plazcek_widgets)
        QtCore.QObject.connect(self.plazcek_fit_range_max, QtCore.SIGNAL(_fromUtf8("editingFinished()")), MainWindow.check_plazcek_widgets)
        QtCore.QObject.connect(self.table, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), MainWindow.table_right_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.populate_table.setText(_translate("MainWindow", "Populate Table", None))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Select", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Runs", None))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sample Formula", None))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Mass Density (g/cc)", None))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Radius (cm)", None))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Packing Fraction", None))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Sample Shape", None))
        item = self.table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Do Abs. Corr. ?", None))
        self.label_3.setText(_translate("MainWindow", "Sample formula example: H 2 O 1, 2H 2 O 1, 238U 1 O 2", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Background", None))
        self.background_no.setText(_translate("MainWindow", "No", None))
        self.background_no_field.setText(_translate("MainWindow", "N/A", None))
        self.label_7.setText(_translate("MainWindow", "(from exp.ini file)", None))
        self.background_yes.setText(_translate("MainWindow", "Yes", None))
        self.groupBox.setTitle(_translate("MainWindow", "Fourier Filter (ex: 1.5, 50)", None))
        self.fourier_filter_from.setText(_translate("MainWindow", "1.5", None))
        self.label_8.setText(_translate("MainWindow", "*", None))
        self.label_2.setText(_translate("MainWindow", ",", None))
        self.fourier_filter_to.setText(_translate("MainWindow", "50", None))
        self.label_6.setText(_translate("MainWindow", "*", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Plazcek", None))
        self.label.setText(_translate("MainWindow", "Type", None))
        self.hydrogen_yes.setText(_translate("MainWindow", "hydrogen", None))
        self.hydrogen_no.setText(_translate("MainWindow", "no hydrogren", None))
        self.label_4.setText(_translate("MainWindow", "Fit Range", None))
        self.plazcek_fit_range_min.setText(_translate("MainWindow", "10", None))
        self.label_9.setText(_translate("MainWindow", "*", None))
        self.label_5.setText(_translate("MainWindow", ",", None))
        self.plazcek_fit_range_max.setText(_translate("MainWindow", "50", None))
        self.label_10.setText(_translate("MainWindow", "*", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Muscat", None))
        self.muscat_yes.setText(_translate("MainWindow", "Yes", None))
        self.radioButton_12.setText(_translate("MainWindow", "No", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Scale Data", None))
        self.scale_data_yes.setText(_translate("MainWindow", "Yes", None))
        self.radioButton_14.setText(_translate("MainWindow", "No", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Run RMC", None))
        self.run_rmc_yes.setText(_translate("MainWindow", "Yes", None))
        self.radioButton_16.setText(_translate("MainWindow", "No", None))
        self.label_21.setText(_translate("MainWindow", "*", None))
        self.label_22.setText(_translate("MainWindow", ": Mandatory field", None))
        self.create_sample_properties_files_button.setText(_translate("MainWindow", "Create Sample Properties Files", None))
        self.run_ndabs_button.setText(_translate("MainWindow", "Run NDabs", None))

