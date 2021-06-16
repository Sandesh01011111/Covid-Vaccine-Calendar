#SOURCE CODE FOR ASSIGNING FUNTIONS TO THE COVIDvaccine.py ui
#THIS FILE IS SAVED AS covidDate.pyw
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from COVIDvaccine import *

class MyCal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_Ui()
       

    def init_Ui(self):
    	self.timerUpdate()
    	self.showlcd()
    	self.dispDateEdit()
    	self.ui.vaccCalendarWidget.selectionChanged.connect(self.dispDateEdit)
    	self.ui.pushButton.clicked.connect(self.getDates)
    	self.currentCalendar()
    	self.inputCalendar()
    	self.getDates()


    def timerUpdate(self):
    	timer = QtCore.QTimer(self)
    	timer.timeout.connect(self.showlcd)
    	timer.start(1000)

    def showlcd(self):
    	time = QtCore.QTime.currentTime()
    	text = time.toString('hh:mm')
    	self.ui.lcdNumber.display(text)

    def dispDateEdit(self):
    	self.ui.dateEdit.setDisplayFormat('dd.MM.yyyy')
    	self.ui.dateEdit.setDate(self.ui.vaccCalendarWidget.selectedDate())

    def currentCalendar(self):
    	noSel = self.ui.currCalendarWidget
    	noSel.setSelectionMode(noSel.NoSelection)
    	

    
    def inputCalendar(self):
    	dateSel = self.ui.vaccCalendarWidget.selectedDate()
    	

    def getDates(self):
    	currDate = QtCore.QDate.currentDate()
    	currDay = currDate.day()
    	currMonth = currDate.month()
    	currYear = currDate.year()
    	
    	dateSel = self.ui.vaccCalendarWidget.selectedDate()
    	vaccDay = dateSel.day()
    	vaccMonth = dateSel.month()
    	vaccYear = dateSel.year()

    	goDay = currDate.daysTo(dateSel)
    	if goDay < 0:
    		goDay = self.ui.vDayLabel.setText("")
    	daysMonths = dateSel.daysInMonth() 
    	goDayStr = str(goDay)

    	
    	daysMonthsStr = str(daysMonths)
    	self.ui.vDayLabel.setText("YOU HAVE " + goDayStr + " DAY(S) UNTIL")
    	self.ui.vDayLabel_2.setText("YOUR COVID VACCINATION.")
    	


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyCal()
    win.show()
    sys.exit(app.exec_())
        
