from tkinter import *
from tkinter import messagebox as mb
root = Tk()
root.resizable(width=False, height=False)
root.iconbitmap('Fh.ico')
root.geometry('400x250')
root.title('Калькулятор ИМТ')
root['bg'] = '#3d3838'
Inlabel = Label(root,width = 17, bg='#3d3883')
def clear(event):
    root.destroy()
    

def check1():
    Größe = entry_1.get()
    Gewicht = entry_2.get()
    Größe = Größe.replace(',', '.')
    Gewicht = Gewicht.replace(',','.')
    Größe = Größe.replace('.', '1')
    Gewicht = Gewicht.replace('.','1')
    if (Größe.isdigit() == False) or (Gewicht.isdigit() == False):
        mb.showerror('Ошибка ввода данных','Строка Роста/Веса может состоять только из цифр и дробного разделителя')
    else:
        pass

def indexzähler(event):
    Größe = entry_1.get()
    Gewicht = entry_2.get()
    Größe = Größe.replace(',', '.')
    Gewicht = Gewicht.replace(',','.')
    mGröße = float
    mGewicht = float(Gewicht)
    mGröße = (float(Größe))/100
    Ausgabe = str
    Ergebnis = float
    Ergebnis = (mGewicht)/((mGröße)**2)
    if Ergebnis < 16.500:
        label3['text'] = 'Отрицательное'
        label3['fg'] = '#ff001e'
        labelD1A['text'] = round(Ergebnis,3)
        labelD2A['text'] = (round(18.5-Ergebnis, 3))
        labelD3['text'] = 'Набрать(кг)='
        labelD3A['text'] = ((round(((18.5*(mGröße**2))-mGewicht), 3))+0.01)
        labelD4A['text'] = 'Выраженный дефицит массы '
        Inlabel['bg'] = '#ff001e'
        Inlabel['text']='*****'
    elif 16.500 <= Ergebnis < 18.5:
        label3['text'] = 'Выше отрицательного'
        label3['fg'] = '#fff70a'
        labelD1A['text'] = round(Ergebnis,3)
        labelD2A['text'] = round(18.5-Ergebnis, 3)
        labelD3['text'] = 'Набрать(кг)='
        labelD3A['text'] = ((round(((18.5*(mGröße**2))-mGewicht), 3))+0.01)
        labelD4A['text'] = 'дефицит массы тела'
        Inlabel['bg'] = '#fff70a'
        Inlabel['text']='***'
    elif 18.5 <= Ergebnis <= 24.999:
        label3['text'] = 'норма'
        label3['fg'] = '#21f700'
        labelD1A['text'] = round(Ergebnis,3)
        labelD2A['text'] = 'Отсутствует'
        labelD3['text'] ='Cбрости/Набрать'
        labelD3A['text'] = 'Не надо'
        labelD4A['text'] = 'Хорошее'
        Inlabel['bg'] = '#21f700'
        Inlabel['text']='*'
    elif 25 <= Ergebnis <= 29.999:
        label3['text'] = 'чуть выше нормы'
        label3['fg'] = '#8a9e37'
        labelD1A['text'] = round(Ergebnis,3)
        labelD2A['text'] = (round(Ergebnis-24.99,3))
        labelD3['text'] = 'Сбросить(кг)='
        labelD3A['text'] = ((round((mGewicht-(24.99*(mGröße**2))),3))+0.01)
        labelD4A['text'] = 'Избыточная масса тела'
        Inlabel['bg'] = '#8a9e37'
        Inlabel['text']='**'
    elif 30.000 <= Ergebnis <= 34.999:
        label3['text'] = 'Выше нормы'
        label3['fg'] = '#fff70a'
        labelD1A['text'] = round(Ergebnis, 3)
        labelD2A['text'] = (round(Ergebnis-24.99,3))
        labelD3['text'] = 'Сбросить(кг)='
        labelD3A['text'] = ((round((mGewicht-(24.99*(mGröße**2))),3))+0.01)
        labelD4A['text'] = 'Ожирение первой степени'
        Inlabel['bg'] = '#fff70a'
        Inlabel['text']='***'
    elif 35.000 <= Ergebnis <= 39.999:
        label3['text'] = 'Значительно выше нормы'
        label3['width']='20'
        label3['fg'] = '#ff700a'
        labelD1A['text'] = round(Ergebnis,3)
        labelD2A['text'] = (round(Ergebnis-24.99,3))
        labelD3['text'] = 'Сбросить(кг)='
        labelD3A['text'] = ((round((mGewicht-(24.99*(mGröße**2))),3))+0.01)
        labelD4A['text'] = 'Ожирение второй степени'
        Inlabel['bg'] = '#ff700a'
        Inlabel['text']='****'
    elif Ergebnis>=40.000:
        label3['text'] = 'Опасно для жизни'
        label3['fg'] = '#ff001e'
        labelD1A['text'] = round(Ergebnis,3)
        labelD2A['text'] = (round(Ergebnis-24.99,3))
        labelD3['text'] = 'Сбросить(кг)='
        labelD3A['text'] = ((round((mGewicht-(24.99*(mGröße**2))),3))+0.01)
        labelD4A['text'] = 'Ожирение третьей степени'
        Inlabel['bg'] = '#ff001e'
        Inlabel['text']='*****' 
labeZ = Label(root, text = 'Запуск →→→', width=15, height=1,bg='#3d3838',fg='#df0')
labelZZ = Label(root, text = 'Или нажмите:', width=15, height=1,bg='#3d3838',fg='#ff601c',font = 'Comfortaa 7')
labeZ1 = Label(root,text = '⋙⋙', width = 5, height=1,bg='#3d3838', fg='#0ff')
labeZ2 = Label(root,text = '⋙⋙', width = 5, height=1,bg='#3d3838', fg='#0ff')
labelD = Label(root,text = 'Данные:', width=6, height=1,bg='#3d3838',fg='#ff9575',font = 'Comfortaa 10',justify = 'left' )
label1 = Label(root, text='Рост',width=8,height=1,bg='#7f34c9',fg='#2fc3d6',font = 'Comfortaa 15',relief = 'raised', justify = 'left')
label2 = Label(root, text='Вес',width=8,height=1,bg='#7f34c9',fg='#2fc3d6',font='Comfortaa 15', relief = 'raised', justify = 'left')
labelInfo = Label(root, text='Краткая сводка:', width=12,height=1, bg='#3d3838',fg='#68f791',font='Comfortaa 11')
labelIn = Label(root,text = '*****:менее 16.5\n **:16.5—18.49 \n *:18.5—24.99 \n **:25—29.99 \n ***:30—34.99 \n ****: 35—39.99 \n *****: 40 и более', width=15, height=10, bg ='#3d3838', fg='#df0', font = 'Comfortaa 10')
labelIm = Label(root, text = '⇊ ИМТ ⇊', width=10, height=1,bg='#3d3838', fg='#eef786', font = 'comfortaa 10' )
label4 = Label(root, text = 'Вердикт:',width=10,height=1, bg='#3d3838',fg='#dfebe2',font='Comfortaa 10' )
label3 = Label(root,width = 17,bg='#3d3838',fg='#f5b5bd')
labelD1 = Label(root,text = 'Ваш ИМТ=', width=10, height=1,bg='#3d3838',fg='#dfebe2',font='Comfortaa 10')
labelD1A = Label(root, width=10, height=1,bg='#3d3838',fg='#dfebe2',font='Comfortaa 8')
labelD2 = Label(root,text = 'Отклонение=', width=10, height=1,bg='#3d3838',fg='#dfebe2',font='Comfortaa 10')
labelD2A = Label(root, width=10, height=1,bg='#3d3838',fg='#dfebe2',font='Comfortaa 8')
labelD3 = Label(root,text = 'Сбросить/Набрать', width=13, height=1,bg='#3d3838',fg='#dfebe2',font='Comfortaa 10')
labelD3A = Label(root, width=18, height=1,bg='#3d3838',fg='#dfebe2',font='Comfortaa 8')
labelD4 = Label(root,text='Состояние тела', width=13, height=1,bg='#3d3838',fg='#dfebe2',font='Comfortaa 10')
labelD4A = Label(root, width=25, height=1,bg='#3d3838',fg='#dfebe2',font='Comfortaa 8')
Ilabel1 = Label(root,bg='#3d3838',fg='#ede72b', text='Информация индикатора\nЧем краснее, тем хуже:',width=30,height=2, font='Comfortaa 8', justify = 'right')
labelSt = Label(root,width=5,height=5,bg='#ff0505' )
entry_1 = Entry(root,font = 'Consolas 15', fg='#cfc1de', bg = '#3f3c42',relief = 'solid', width = 5)
entry_2 = Entry(root, font = 'Consolas 15', fg='#cfc1de', bg = '#3f3c42',relief = 'solid', width = 5)
Button_1 = Button(root,text = 'Enter',font = 'Consolas 10', bg='green',fg='#5c0d4b',highlightcolor='#35ff03',relief = 'solid', width = 8, height = 2,command=check1)
Button_1.bind("<Button-1>", indexzähler)
root.bind("<Return>", indexzähler)
labelD.grid(row=0,column=0)
label1.grid(row=1,column=0)
entry_1.grid(row=1,column=1)
label2.grid(row=2,column=0)
entry_2.grid(row=2,column=1)
labelInfo.grid(row=5,column=0)
label4.grid(row=6,column=0)
label3.grid(row=6,column=1)
labelD1.grid(row=7,column=0)
labelD1A.grid(row=7,column=1)
labelD2.grid(row=8,column=0)
labelD2A.grid(row=8,column=1)
labelD3.grid(row=9,column=0)
labelD3A.grid(row=9, column=1)
labelD4.grid(row=10, column=0)
labelD4A.grid(row=10, column=1)
Ilabel1.place(x=240,y=40)
Inlabel.place(x=270, y=75)
labeZ.place(x=250,y=0)
labelZZ.place(x=250, y=20)
labeZ1.place(x=115,y=30)
labeZ2.place(x=115,y=54)
labelIm.place(x=300, y = 100)
labelIn.place(x=280, y=100)

Button_1.place(x=332,y=0)
root.mainloop()


