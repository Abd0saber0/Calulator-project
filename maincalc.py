# ملف الواجهه الرائيسة 

from PyQt6 import QtWidgets, uic,QtGui
from logic import CalculatorLogic
class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        FILE_PATH='./calc.ui'
        ICON_PATH='../../images/831302.png'
        self.commands = {
        'c': self.clear_screen,
        'sb': self.backspace,
        '_': self.negate,
        '.': self.add_dot,
        '=': self.calculate
                        }
        self.finish= False  # متغير لإنهاء العملية الحسابية
        self.calc=CalculatorLogic()
        uic.loadUi(FILE_PATH, self) # تحميل ملف يواي مباشرة
        self.setWindowIcon(QtGui.QIcon(ICON_PATH))
        self.show()
        self.buttons_control()
    def show_message(self,title,message,type=['critical','question','information','about','wornning']):
        fun=getattr(QtWidgets.QMessageBox,type)
        return fun(self,title,message) # عشان ترجع قيمة لو الرسالة سؤال
        
    def about(self):
        self.show_message('About',"Welcome to my calculater app\nI'm abdo saber",'about')

    def shotdown(self):
        self.close()

    def buttons_control(self):
        # shut down btn
        self.btnon.clicked.connect(self.shotdown)
        # info btn
        self.btnabt.clicked.connect(self.about)
        #Del_btns
        self.btnc.clicked.connect(lambda:self.display('c'))
        self.btnsb.clicked.connect(lambda:self.display('sb'))

        # numbers btns
        for i in range(10):
            #دي دالة بايثون بتخليك توصل لخاصية أو متغير بالاسم كسلسلة نصية
            getattr(self,f'btn{i}').clicked.connect(lambda clicked, x= i:self.display(str(x)))

        # operators btns
        self.btnx.clicked.connect(lambda:self.display('*'))
        self.btnadd.clicked.connect(lambda:self.display('+'))
        self.btnd.clicked.connect(lambda:self.display('/'))
        self.btnmin.clicked.connect(lambda:self.display('-'))
        self.btnsq.clicked.connect(lambda:self.sqrt())
        self.btnrr.clicked.connect(lambda:self.display(')'))
        self.btnlr.clicked.connect(lambda:self.display('('))
        self.btn100.clicked.connect(lambda:self.prec())
        self.btnneg.clicked.connect(lambda:self.display('_'))
        self.btn10.clicked.connect(lambda:self.display('.'))
        self.btnequal.clicked.connect(lambda:self.display('='))

    def clear_screen(self, current= None):
        self.label.setText(str(0))

    def backspace(self,current):
            if len(current) <= 1 :  
                self.label.setText(str(0))
            else:
                self.label.setText(current[:-1]) # حذف الرقم الاخير

    def negate(self,current):
            if current.startswith("-"):
                self.label.setText(current[1:])
            else:
                if current != '0': # ميضفش - للصفر
                    self.label.setText("-" + current)       

    def add_dot(self,current):
        if '.'not in current:
            self.label.setText(current + '.')

    def calculate(self,current):
            try:
                exception= self.calc.result(current)
                self.label.setText(exception)
            except:
                self.show_message("Wrong","Can't be done.",'critical')
            finally:
                self.finish= True  
                      
    def display(self, x): # x  دا الزر ال تم الضغط علية
        '''
        دالة العرض ع الشاشة
        '''
        CURRENT_TEXT= self.label.text()
        if x in self.commands:
            self.commands[x](CURRENT_TEXT)
        else:
            if CURRENT_TEXT == "0" or self.finish:
                CURRENT_TEXT = ''
                self.finish = False  # ارجاع القيمة للاصل
            self.label.setText( CURRENT_TEXT + x  )
        

    def sqrt(self):
        "دالة الجذر التربيعي"
        res=self.calc.sqr(self.label.text())
        if res == "ValueError":
            self.show_message("Error", "Can't take square root of negative number", 'critical')
        else:
            self.label.setText(str(res))

        self.finish= True 

    def prec(self):
        self.label.setText(self.calc.percentage(self.label.text()))

    def closeEvent(self, event):
        reply=self.show_message('Confirm Exit','Are you want to Exit?','question')
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


app=QtWidgets.QApplication([])
win=Window()
app.exec()




