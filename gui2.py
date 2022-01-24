import re

from PyQt5 import QtCore, QtGui, QtWidgets
import output
import functions
import seidel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # Font Setting
        font = QtGui.QFont()
        font.setPointSize(7)

        # ComboBox Initialization
        self.methods = QtWidgets.QComboBox(self.centralwidget)
        self.methods.setGeometry(QtCore.QRect(70, 150, 131, 22))
        self.methods.addItem("")
        self.methods.addItem("")
        self.methods.addItem("")
        self.methods.addItem("")
        self.methods.addItem("")

        # LineEdit Initialization
        self.numberOfEqInput = QtWidgets.QLineEdit(self.centralwidget)
        self.numberOfEqInput.setGeometry(QtCore.QRect(60, 70, 151, 20))
        self.iterationsInput = QtWidgets.QLineEdit(self.centralwidget)
        self.iterationsInput.setGeometry(QtCore.QRect(110, 490, 141, 21))
        self.percisionInput = QtWidgets.QLineEdit(self.centralwidget)
        self.percisionInput.setGeometry(QtCore.QRect(550, 490, 131, 20))
        self.valuesInput = QtWidgets.QLineEdit(self.centralwidget)
        self.valuesInput.setGeometry(QtCore.QRect(90, 290, 181, 20))
        self.fileInput = QtWidgets.QLineEdit(self.centralwidget)
        self.fileInput.setGeometry(QtCore.QRect(460, 80, 201, 20))

        # Labels Initialization
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 180, 291, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 460, 141, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 460, 131, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 520, 141, 20))
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(550, 520, 131, 20))
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 260, 181, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)

        # Buttons Initialization
        self.finishButton = QtWidgets.QPushButton(self.centralwidget)
        self.finishButton.setGeometry(QtCore.QRect(350, 520, 101, 31))

        # Radio Buttons Initialization
        self.fileRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.fileRadio.setGeometry(QtCore.QRect(460, 50, 201, 17))
        self.equationRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.equationRadio.setGeometry(QtCore.QRect(60, 40, 151, 17))

        # TextEdit Initialization
        self.equationsInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.equationsInput.setGeometry(QtCore.QRect(450, 220, 271, 151))

        MainWindow.setCentralWidget(self.centralwidget)

        # Set default radio button option
        self.equationRadio.setChecked(True)
        self.fileInput.setEnabled(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.methods.setItemText(0, _translate("MainWindow", "Gaussian Eliminiation"))
        self.methods.setItemText(1, _translate("MainWindow", "LU Decomposition"))
        self.methods.setItemText(2, _translate("MainWindow", "Gaussian-Jordan"))
        self.methods.setItemText(3, _translate("MainWindow", "Gauss-Seidel"))
        self.methods.setItemText(4, _translate("MainWindow", "All Methods"))
        self.label_2.setText(_translate("MainWindow", "Equations"))
        self.label_3.setText(_translate("MainWindow", "Iterations"))
        self.label_4.setText(_translate("MainWindow", "Precision"))
        self.label_5.setText(_translate("MainWindow", "Default 50"))
        self.label_6.setText(_translate("MainWindow", "Default 0.00001"))
        self.finishButton.setText(_translate("MainWindow", "Calculate"))
        self.label_7.setText(_translate("MainWindow", "Initial Values "))
        self.fileRadio.setText(_translate("MainWindow", "File Name"))
        self.equationRadio.setText(_translate("MainWindow", "Number of Equations"))

        # On State change functions
        self.fileRadio.toggled.connect(self.checked)
        self.finishButton.clicked.connect(self.clicked)

    def clicked(self):
        equations = []

        # Set number of iterations and precision to default if no value is entered
        if self.iterationsInput.text().strip() == "":
            maxIterations = 50
        else:
            maxIterations = self.iterationsInput.text().strip()

        if self.percisionInput.text().strip() == "":
            percision = 0.00001
        else:
            percision = self.percisionInput.text().strip()

        # file is selected as an input method
        if self.fileRadio.isChecked():
            file_name = self.fileInput.text() + ".txt"
            f = open(file_name, 'r')
            fileContent = f.readlines()
            numberOfEquations = int(fileContent[0].strip())
            method = fileContent[1].strip()

            if method == "Gaussian-elimination":
                index = 0
            elif method == "LU decomposition":
                index = 1
            elif method == "Gaussian-jordan":
                index = 2
            elif method == "Gauss-seidel":
                index = 3

            for i in range(0, numberOfEquations):
                equations.append(fileContent[i + 2].strip())

            if index == 3:
                initialValues = fileContent[numberOfEquations + 2].strip().split(" ")

        # insert the data using the GUI
        else:
            index = self.methods.currentIndex()
            numberOfEquations = int(self.numberOfEqInput.text().strip())
            equationsTextInput = self.equationsInput.toPlainText()
            equations = equationsTextInput.split("\n")
            initialValues = self.valuesInput.text().strip().split()
            initialValues = [float(i) for i in initialValues]
        matrix = []
        roots = []

        # Get Coefficients of the equations
        for j in range(0, numberOfEquations):
            coeff = re.findall(r'[\d.\-+]+', equations[j])
            coeff = [float(i) for i in coeff]
            coeff[-1] = coeff[-1] * -1
            matrix.append(coeff)

        matrix1 = matrix.copy()
        matrix2 = matrix.copy()
        matrix3 = matrix.copy()

        # Calling functions for each Method
        if index == 0:
            roots.append(functions.Gauss_Elimination(matrix))
        elif index == 1:
            roots.append(functions.LU_Decomposition(matrix))
        elif index == 2:
            roots.append(functions.Gauss_Jordan(matrix))
        elif index == 3:
            roots.append(seidel.gauss_seidel(matrix, initialValues, int(maxIterations), float(percision)))
        else:
            roots.append(functions.Gauss_Elimination(matrix))
            roots.append(functions.LU_Decomposition(matrix1))
            roots.append(functions.Gauss_Jordan(matrix2))
            roots.append(seidel.gauss_seidel(matrix3, initialValues, int(maxIterations), float(percision)))

        self.outputWindow = QtWidgets.QMainWindow()
        self.ui2 = output.Ui_outputWindow()
        self.ui2.setupUi(self.outputWindow, roots, numberOfEquations, index)
        self.outputWindow.show()

    def checked(self):
        if self.fileRadio.isChecked():
            self.fileInput.setEnabled(True)
            self.equationsInput.setEnabled(False)
            self.numberOfEqInput.setEnabled(False)
            self.valuesInput.setEnabled(False)
            self.methods.setEnabled(False)
        else:
            self.equationsInput.setEnabled(True)
            self.numberOfEqInput.setEnabled(True)
            self.valuesInput.setEnabled(True)
            self.fileInput.setEnabled(False)
            self.methods.setEnabled(True)
