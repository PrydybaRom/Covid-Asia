import covid19cases as covid
import openpyxl
from tkinter import*
window_asia = Tk()
window_asia.geometry('700x450')
window_asia['bg'] = 'Blue'

def home ():
    window_asia.quit()
    pass

button_home = Button(window_asia, text='Home',command=home)
button_home.place(x=10,y=10)

api = covid.get_global_cases()
Asia = covid.get_continent_cases("Asia")


book = openpyxl.Workbook()
Excel_file = book.active


A1 = Excel_file['A1'] = u'Інформація по Азії'
A1.encode('cp1125')
A2 = Excel_file['A2'] = u'Всього випадків'
A2.encode('cp1125')
A3 = Excel_file['A3'] = u'Загальна кількість смертей'
A3.encode('cp1125')
A4 = Excel_file['A4'] = u'Число одужавших'
A4.encode('cp1125')

B1 = Excel_file['B1'] = covid.get_continent_cases("Asia")['TotalCases']
B2 = Excel_file['B2'] = covid.get_continent_cases("Asia")['TotalDeaths']
B3 = Excel_file['B3'] = covid.get_continent_cases("Asia")['TotalRecovered']


label_asia = Label(window_asia,bg='blue',fg='white',font=('Arial',15))
label_asia['text']=f'{A1}\n \n \n{A2}  — {B1} \n \n               {A3} — {B2}  \n \n {A4} — {B3}'
label_asia.place(x=120,y=50)


book.save("Europe_book.xlsx")
book.close()
window_asia.mainloop()