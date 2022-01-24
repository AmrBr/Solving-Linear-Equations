from PyQt5 import QtCore, QtGui, QtWidgets
import string

from PyQt5.QtWidgets import QTableWidgetItem


class Ui_outputWindow(object):
    def setupUi(self, outputWindow, roots, numberOfEquations, methodIndex):
        outputWindow.setObjectName("MainWindow")
        outputWindow.resize(557, 437)
        self.centralwidget = QtWidgets.QWidget(outputWindow)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 80, 557, 221))
        self.tableWidget.setColumnCount(numberOfEquations)
        font = QtGui.QFont()
        font.setPointSize(10)
        if methodIndex == 4:
            self.tableWidget.setRowCount(4)
        else:
            self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        self.methodLabel = QtWidgets.QLabel(self.centralwidget)
        self.methodLabel.setGeometry(QtCore.QRect(130, 30, 271, 31))
        self.methodLabel.setFont(font)
        self.methodLabel.setText("")
        self.methodLabel.setAlignment(QtCore.Qt.AlignCenter)
        outputWindow.setCentralWidget(self.centralwidget)

        self.setData(roots, methodIndex)

        self.retranslateUi(outputWindow)
        QtCore.QMetaObject.connectSlotsByName(outputWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("outputWindow", "outputWindow"))

    def setData(self, data, index):
        header = string.ascii_lowercase
        header2 = []
        if index == 0:
            method = "Gaussian-elimination"
        elif index == 1:
            method = "LU decomposition"
        elif index == 2:
            method = "Gaussian-jordan"
        elif index == 3:
            method = "Gauss-seidel"
        else:
            method = "All Methods"
        self.methodLabel.setText(method)
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                newItem = QTableWidgetItem(str(data[i][j]))
                self.tableWidget.setItem(i, j, newItem)
            header2.append(header[i])
        if index == 4:
            self.tableWidget.setVerticalHeaderLabels(["Gaussian-elimination", "LU decomposition", "Gaussian-jordan", "Gauss-seidel"])
        else:
            self.tableWidget.setVerticalHeaderLabels([method])
        self.tableWidget.setHorizontalHeaderLabels(header2)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


