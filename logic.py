from PyQt6 import QtWidgets,uic
import math
class CalculatorLogic:
    def __init__(self):
        pass
    def percentage(self,text):
        return str(float(text)/100)
    def sqr(self,text):
        try:
            return math.sqrt(float(text))   # float عشان لو ضغطت مرتين ميحصلش خطأ
        except ValueError:
            return "ValueError"
    def result(self,exprestion):
        return str(eval(exprestion))