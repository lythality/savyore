from sys import argv
from rule_checker import RuleChecker

with_gui = True

def start_saint(srcfile: str):
    trav = RuleChecker()
    trav.add_file(srcfile)
    trav.start_trav()
    trav.post_check()
    trav.print_violations()
    # for f in trav.function:
    #     print(f.get_control_flow_graph_info())


from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class My_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def button_clicked(self):
        print("pressed")
        self.ui.textEdit.setText("ABC")

    def show_code(self):
        self.ui.textEdit.setText(open('../test_res/test_expr.c', 'r').read())


# the main function
if __name__ == '__main__':
    # process files in argv
    if len(argv) > 1:
        for arg in argv[1:]:
            print(arg)
            start_saint(arg)
    elif with_gui:
        import sys
        from PyQt5 import QtGui, QtWidgets
        from ui.main_view import Ui_MainWindow
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = My_MainWindow()
        MainWindow.show()
        # test - start
        MainWindow.ui.textEdit.setText(open('../test_res/test_expr.c', 'r').read())
        lines = open('../test_res/test_expr.c', 'r').read().split("\n")
        for i in range(len(lines)):
            MainWindow.ui.codeWidget.insertRow(MainWindow.ui.codeWidget.rowCount())
            MainWindow.ui.codeWidget.setItem(i, 0, QTableWidgetItem(str(i+1)))
            MainWindow.ui.codeWidget.setItem(i, 2, QTableWidgetItem(lines[i]))
        # test - end
        app.exec_()
    else:
        # start_saint('../test_res/test_array.c')
        # start_saint('../test_res/test_bitfield.c')
        # start_saint('../test_res/test_cfg.c')
        # start_saint('../test_res/test_comments.c')
        # start_saint('../test_res/test_control.c')
        start_saint('../test_res/test_expr.c')
        # start_saint('../test_res/test_goto_15_1.c')
        # start_saint('../test_res/test_goto_15_3.c')
        # start_saint('../test_res/test_func_decl.c')
        # start_saint('../test_res/test_multi001.c')
        # start_saint('../test_res/test_multi002.c')
        # start_saint('../test_res/test_switch.c')
        # start_saint('../test_res/test_typedef.c')
        # start_saint('../test_res/test_string.c')
        # start_saint('../test_res/test_bitfield.c')
        # start_saint('../test_res/test_value.c')
