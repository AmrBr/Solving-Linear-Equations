from PyQt5 import QtWidgets
import gui2
import functions

if __name__ == "__main__":
    import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = gui2.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())

    A = [
        [1, 1, 2],
        [-1, -2, 3],
        [3, 7, 4]
    ]
    AA = [
        8, 1, 10
    ]
    B = [
        [1, 1, 2, 8],
        [-1, -2, 3, 1],
        [3, 7, 4, 10]
    ]
    C = [
        [1, 1, 2, 8],
        [-1, -2, 3, 1],
        [3, 7, 4, 10]
    ]

    print(functions.LU_Decomposition(A, AA))
    print(functions.Gauss_Elimination(B))
    print(functions.Gauss_Jordan(C))

