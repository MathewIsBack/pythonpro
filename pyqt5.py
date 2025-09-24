import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI")
        self.setGeometry(700, 300, 500, 500)
        # self.setWindowIcon(QIcon("profilepic.jpg"))

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("profilepic.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2,
                            (self.height() - label.height()) // 2,
                            label.width(),
                            label.height())

        # label = QLabel("Hello", self)
        # label.setFont(QFont("Arial", 30))
        # label.setGeometry(0, 0, 500, 100)
        # label.setStyleSheet("color: #404142;"
        #                     "background-color: #34ebc9;"
        #                     "font-weight: bold;"
        #                     "font-style: italic;"
        #                     "text-decoration: underline;")
        
        # label.setAlignment(Qt.AlignTop) #Vertically top
        # label.setAlignment(Qt.AlignBottom) #Vertically Bottom
        # label.setAlignment(Qt.AlignVCenter) #Vertically Center


        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignHCenter)

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()








