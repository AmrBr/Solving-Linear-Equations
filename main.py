from PyQt5 import QtWidgets
import gui2
import functions
import seidel

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

    D=[
        [12,3,-5],
        [1,5,3],
        [3,7,13]
    ]

    DD = [1, 28, 76]
    init_values = [1, 0, 1]

    M=[
        [12,3,-5,1],
        [1,5,3,28],
        [3,7,13,76]
    ]
    X,XX=seidel.split(M)
    print(seidel.gauss_seidel(X, XX, init_values, 6, 0.001))

    #print(functions.LU_Decomposition(A, AA))
    #print(functions.Gauss_Elimination(B))
    #print(functions.Gauss_Jordan(C))

