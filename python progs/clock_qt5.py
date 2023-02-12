# write a qt gui clock program in python

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtCore import QTimer, QTime

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt GUI Clock")
        self.setGeometry(50,50,500,300)
        self.UI()
        
    def UI(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.time)
        self.timer.start(1000)      
        self.labelTime = QLabel("Time:                   ", self)
        self.labelTime.move(200,50)                
        self.show()
        
    def time(self):
        time = QTime.currentTime().toString()
        self.labelTime.setText("Time: " + time)
        

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
    

"""

        #self.labelTime.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) 
        self.labelTime.setAlignment(Qt.AlignRight | Qt.AlignVCenter) 
"""    
