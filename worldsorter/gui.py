from PyQt5 import QtWidgets, uic
import sys, os

class Main(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)

        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "main.ui"), self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
