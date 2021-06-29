import tkinter as tk

class Gui():
    def __init__(self):
        self.root = tk.Tk()
        self.settingWindow()
        self.declareWidget()
        self.placeWidget()

    def settingWindow(self):
        self.root.title('Монитор DL')
        self.root.geometry('600x400')

    def declareWidget(self):
        self.strLbl01_begin = 'Время запуска предыдущей проверки: '
        self.strLbl01 = self.strLbl01_begin + '00:00'
        self.strLbl02 = 'Интервал 20 мин '
        self.lbl01 = tk.Label(text=self.strLbl01)
        self.lbl02 = tk.Label(text=self.strLbl02)
        self.btnProcess = tk.Button(text='Обработка')
        self.btnExit = tk.Button(text='  Выход  ', command=exit)
        self.txtMain = tk.Text()

    def placeWidget(self):
        self.lbl01.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.lbl02.grid(row=0, column=4, padx=10, pady=10)
        self.btnProcess.grid(row=0, column=7, padx=10, pady=10)
        self.btnExit.grid(row=0, column=8, padx=10, pady=10)
        self.txtMain.grid(row=1, column=0, columnspan=14)
