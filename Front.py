
import PyQt5.QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
import pyqtgraph as pg
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Backend


class Ui_MainWindow(QDialog):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 851)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 243, 213);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_count = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_count.setGeometry(QtCore.QRect(660, 120, 131, 41))
        self.pushButton_count.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_count.setObjectName("pushButton_count")

        self.pushButton_browse_prices = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browse_prices.setGeometry(QtCore.QRect(450, 130, 70, 31))
        self.pushButton_browse_prices.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_browse_prices.setObjectName("pushButton_browse_prices")

        self.pushButton_browse_costs = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browse_costs.setGeometry(QtCore.QRect(450, 190, 70, 31))
        self.pushButton_browse_costs.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_browse_costs.setObjectName("pushButton_costs")

        self.pushButton_browse_model_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browse_model_file.setGeometry(QtCore.QRect(450, 250, 70, 31))
        self.pushButton_browse_model_file.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_browse_model_file.setObjectName("pushButton_browse_model_file")

        self.pushButton_browse_generated_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browse_generated_file.setGeometry(QtCore.QRect(450, 310, 70, 31))
        self.pushButton_browse_generated_file.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_browse_generated_file.setObjectName("pushButton_generated_file")

        self.pushButton_get_costs_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_get_costs_file.setGeometry(QtCore.QRect(650, 260, 150, 31))
        self.pushButton_get_costs_file.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_get_costs_file.setObjectName("pushButton_get_costs_file")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 60, 91, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_model = QtWidgets.QLabel(self.centralwidget)
        self.label_model.setGeometry(QtCore.QRect(80, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_model.setFont(font)
        self.label_model.setAlignment(QtCore.Qt.AlignCenter)
        self.label_model.setObjectName("label_model")

        self.label_maximize = QtWidgets.QLabel(self.centralwidget)
        self.label_maximize.setGeometry(QtCore.QRect(295, 30, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_maximize.setFont(font)
        self.label_maximize.setAlignment(QtCore.Qt.AlignCenter)
        self.label_maximize.setObjectName("label_maximize")

        self.label_start = QtWidgets.QLabel(self.centralwidget)
        self.label_start.setGeometry(QtCore.QRect(587, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_start.setFont(font)
        self.label_start.setAlignment(QtCore.Qt.AlignCenter)
        self.label_start.setObjectName("label_start")

        self.label_step = QtWidgets.QLabel(self.centralwidget)
        self.label_step.setEnabled(True)
        self.label_step.setGeometry(QtCore.QRect(715, 30, 24, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_step.setFont(font)
        self.label_step.setAlignment(QtCore.Qt.AlignCenter)
        self.label_step.setObjectName("label_step")

        self.label_number_of_steps = QtWidgets.QLabel(self.centralwidget)
        self.label_number_of_steps.setGeometry(QtCore.QRect(790, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_number_of_steps.setFont(font)
        self.label_number_of_steps.setAlignment(QtCore.Qt.AlignCenter)
        self.label_number_of_steps.setObjectName("label_number_of_steps")

        self.label_prices = QtWidgets.QLabel(self.centralwidget)
        self.label_prices.setGeometry(QtCore.QRect(170, 110, 101, 21))
        self.label_prices.setFont(font)
        self.label_prices.setAlignment(QtCore.Qt.AlignCenter)
        self.label_prices.setObjectName("label_prices")

        self.label_costs = QtWidgets.QLabel(self.centralwidget)
        self.label_costs.setGeometry(QtCore.QRect(170, 170, 101, 21))
        self.label_costs.setFont(font)
        self.label_costs.setAlignment(QtCore.Qt.AlignCenter)
        self.label_costs.setObjectName("label_costs")

        self.label_model_file = QtWidgets.QLabel(self.centralwidget)
        self.label_model_file.setGeometry(QtCore.QRect(170, 230, 101, 21))
        self.label_model_file.setFont(font)
        self.label_model_file.setAlignment(QtCore.Qt.AlignCenter)
        self.label_model_file.setObjectName("label_model_file")

        self.label_generated_file = QtWidgets.QLabel(self.centralwidget)
        self.label_generated_file.setGeometry(QtCore.QRect(170, 290, 101, 21))
        self.label_generated_file.setFont(font)
        self.label_generated_file.setAlignment(QtCore.Qt.AlignCenter)
        self.label_generated_file.setObjectName("label_generated_file")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(280, 60, 101, 31))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.textEdit_start = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_start.setGeometry(QtCore.QRect(560, 60, 101, 31))
        self.textEdit_start.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_start.setObjectName("textEdit_start")
        self.textEdit_start.setFont(QFont('Arial', 12))

        self.textEdit_step = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_step.setGeometry(QtCore.QRect(680, 60, 91, 31))
        self.textEdit_step.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_step.setObjectName("textEdit_step")
        self.textEdit_step.setFont(QFont('Arial', 12))

        self.textEdit_number_of_steps = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_number_of_steps.setGeometry(QtCore.QRect(790, 60, 101, 31))
        self.textEdit_number_of_steps.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_number_of_steps.setObjectName("textEdit_number_of_steps")
        self.textEdit_number_of_steps.setFont(QFont('Arial', 12))

        self.textEdit_prices = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_prices.setGeometry(QtCore.QRect(30, 130, 400, 31))
        self.textEdit_prices.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_prices.setObjectName("textEdit_prices")
        self.textEdit_prices.setFont(QFont('Arial', 12))

        self.textEdit_costs = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_costs.setGeometry(QtCore.QRect(30, 190, 400, 31))
        self.textEdit_costs.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_costs.setObjectName("textEdit_costs")
        self.textEdit_costs.setFont(QFont('Arial', 12))

        self.textEdit_model_file = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_model_file.setGeometry(QtCore.QRect(30, 250, 400, 31))
        self.textEdit_model_file.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_model_file.setObjectName("textEdit_model_file")
        self.textEdit_model_file.setFont(QFont('Arial', 12))

        self.textEdit_generated_file = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_generated_file.setGeometry(QtCore.QRect(30, 310, 400, 31))
        self.textEdit_generated_file.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_generated_file.setObjectName("textEdit_generated_file")
        self.textEdit_generated_file.setFont(QFont('Arial', 12))

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 400, 283, 401))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(350, 400, 600, 401))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")

        self.label_Table = QtWidgets.QLabel(self.centralwidget)
        self.label_Table.setGeometry(QtCore.QRect(80, 370, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Table.setFont(font)
        self.label_Table.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Table.setObjectName("label_number")

        self.label_Graphic = QtWidgets.QLabel(self.centralwidget)
        self.label_Graphic.setGeometry(QtCore.QRect(620, 370, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Graphic.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.progressbar = QtWidgets.QProgressBar()
        #
        self.progress_bar = QProgressBar(MainWindow)
        self.progress_bar.setValue(0)
        self.progress_bar.setGeometry(550,190,400,30)
        self.progress_bar_max_value = 1
        self.progress_bar_curr_value = 0
        #
        self.filling_error = 0
        self.value_error = 0


        self.table_values = np.array([])

        x = np.arange(50)
        y = np.random.normal(size=(3, 50))
        pg.setConfigOptions(antialias=True)
        pen = pg.mkPen(color=(0, 0, 0), width = 2,style=QtCore.Qt.SolidLine)

        self.plot = self.graphicsView.plot()


        self.graphicsView.setBackground(QtGui.QColor('white'))


        self.add_functions()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def get_costs_file(self):
        self.progress_bar.setValue(0)
        Backend.Optimizer.printpoint(Backend.Optimizer, self.current_hover[0])
        self.progress_bar.setValue(100)

    def browse_prices_files(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C://', 'txt files (*.txt)')
        if(fname[0] != ''):
            self.textEdit_prices.setText(fname[0])

    def browse_costs_files(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C://', 'txt files (*.txt)')
        if(fname[0] != ''):
            self.textEdit_costs.setText(fname[0])

    def browse_model_files(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C://', 'txt files (*.txt)')
        if(fname[0] != ''):
            self.textEdit_model_file.setText(fname[0])           # ИСПРАВИТЬ

    def browse_generated_files(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C://', 'txt files (*.txt)')
        if(fname[0] != ''):
            self.textEdit_generated_file.setText(fname[0])           # ИСПРАВИТЬ
            
    def exception_message_fields(self):
        QMessageBox.critical(self, "FILLING_ERROR ", "Fill in all fields", QMessageBox.Ok)

    def exception_value_error(self):
        QMessageBox.critical(self, "FILLING_ERROR ", "Incorrect type in some fields", QMessageBox.Ok)

    def progress_bar_add(self, c):
        self.progress_bar_curr_value += c
        self.progress_bar.setValue(int(self.progress_bar_curr_value / self.progress_bar_max_value * 100))

    def button_count_clicked(self):

        self.setData()
        if self.filling_error:
            return
        number_of_steps = int(self.textEdit_number_of_steps.toPlainText())
        # настройка таблицы
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(number_of_steps)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 134)

        #Mouse tracking
        self.tableWidget.setMouseTracking(True)
        self.current_hover = [0, 0]
        self.tableWidget.cellClicked.connect(self.cell_hover)

        # base
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Revenue'))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Margin'))
        self.tableWidget.setItem(0, 0, QTableWidgetItem('Max Revenue 125'))

        # заполнение таблицы
        for i in range(number_of_steps):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.table_values[i][0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.table_values[i][1])))      # подставить подсчитанное значение маржи


    def cell_hover(self, row, column):
        item = self.tableWidget.item(row, column)
        old_item = self.tableWidget.item(self.current_hover[0], self.current_hover[1])
        if self.current_hover != [row, column]:
            old_item.setBackground(QBrush(QColor('white')))
            item.setBackground(QBrush(QColor('yellow')))
        self.current_hover = [row, column]



    def add_functions(self):
        self.pushButton_count.clicked.connect(self.button_count_clicked)
        self.pushButton_browse_prices.clicked.connect(self.browse_prices_files)
        self.pushButton_browse_costs.clicked.connect(self.browse_costs_files)
        self.pushButton_browse_model_file.clicked.connect(self.browse_model_files)
        self.pushButton_browse_generated_file.clicked.connect(self.browse_generated_files)
        self.pushButton_get_costs_file.clicked.connect(self.get_costs_file)

    def setData(self):

        model_type = self.comboBox.currentText()
        rev_or_margin = self.comboBox_2.currentText()
        start = self.textEdit_start.toPlainText()
        step = self.textEdit_step.toPlainText()
        number_of_steps = self.textEdit_number_of_steps.toPlainText()
        prices_file = self.textEdit_prices.toPlainText()
        costs_file = self.textEdit_costs.toPlainText()
        model_file = self.textEdit_model_file.toPlainText()
        generated_file = self.textEdit_generated_file.toPlainText()

        self.filling_error = 0
        if model_type == '' or rev_or_margin == '' or start == '' or step == '' or number_of_steps == '' or prices_file == '' or\
                costs_file == '' or model_file == '' or generated_file == '':
            self.exception_message_fields()
            self.filling_error = 1
            return

        self.value_error = 0
        try:
            start = float(start)
            step = float(step)
            number_of_steps = int(number_of_steps)
        except ValueError:
            self.exception_value_error()
            self.value_error = 1
            return

        # Progress bar
        self.progress_bar_max_value = number_of_steps
        self.progress_bar_curr_value = 0
        self.progress_bar.setValue(0)

        Backend.Optimizer.setData(Backend.Optimizer, model_type, rev_or_margin, start, step, number_of_steps, prices_file, costs_file, model_file, generated_file)
        arr_res = np.array(Backend.Optimizer.run(Backend.Optimizer, self))
        self.table_values = arr_res
        x = np.array([])
        y = np.array([])
        for i in range(len(arr_res)):
            x = np.append(x, arr_res[i][0])
            y = np.append(y, arr_res[i][1])
        if(rev_or_margin == 'revenue'):
            x,y = y, x
            self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Margin'))
            self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Revenue'))

        pen = pg.mkPen(color=(0, 0, 0), width=2, style=QtCore.Qt.SolidLine)
        self.plot.setData(x, y, pen=pen)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Primo"))
        self.pushButton_count.setText(_translate("MainWindow", "Count"))
        self.pushButton_browse_prices.setText(_translate("MainWindow", "browse file"))
        self.pushButton_browse_costs.setText(_translate("MainWindow", "browse file"))
        self.pushButton_browse_model_file.setText(_translate("MainWindow", "browse file"))
        self.pushButton_browse_generated_file.setText(_translate("MainWindow", "browse file"))

        self.pushButton_get_costs_file.setText(_translate("MainWindow", "get costs file"))

        self.comboBox.setItemText(0, _translate("MainWindow", "linear"))
        self.comboBox.setItemText(1, _translate("MainWindow", "log10"))
        self.comboBox.setItemText(2, _translate("MainWindow", "loge"))
        self.label_model.setText(_translate("MainWindow", "Model"))
        self.label_maximize.setText(_translate("MainWindow", "Maximize"))
        self.label_start.setText(_translate("MainWindow", "start"))
        self.label_step.setText(_translate("MainWindow", "step"))
        self.label_number_of_steps.setText(_translate("MainWindow", "Number of steps"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "revenue"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "margin"))
        self.label_Table.setText(_translate("MainWindow", "Table"))
        self.label_Graphic.setText(_translate("MainWindow", "Graphic"))
        self.label_prices.setText(_translate("MainWindow", "Prices_file"))
        self.label_costs.setText(_translate("MainWindow", "Costs_file"))
        self.label_model_file.setText(_translate("MainWindow", "Model file"))
        self.label_generated_file.setText(_translate("MainWindow", "Generating file"))
        self.textEdit_prices.setText('D:')
        self.textEdit_costs.setText('D:')
        self.textEdit_model_file.setText('D:')
        self.textEdit_generated_file.setText('D:')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
