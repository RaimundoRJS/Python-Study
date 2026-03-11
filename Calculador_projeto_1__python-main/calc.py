from tkinter import *
from tkinter import ttk


cor1 = "#0D81DE"
cor2 = "#F57C23"
cor3 = "#DED914"
cor4 = "#E1F2B3"
cor5 = "#30151B"


area=Tk()
area.title('calculadora')
area.geometry('350x490')
area.config(bg=cor4)
frame_tela = Frame(area, width=350, height=120, bg= cor5)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(area, width=350, height=480, )
frame_corpo.grid(row=1, column=0)


tot_valores = ''
valor_texto = StringVar()

def Entrada_de_Valores(event):
    global tot_valores
    tot_valores = tot_valores +str( event)

    valor_texto.set(tot_valores)


def calcular():
    global tot_valores
    resultado= eval(tot_valores)
    print(resultado)
    valor_texto.set(resultado)

def limpar_tudo():
    global tot_valores
    tot_valores = ''
    valor_texto.set("")


tela_label = Label(frame_tela, width=16 , height=3, textvariable=valor_texto, font=('Ivy 27'), relief=FLAT , anchor= 'e', justify=RIGHT   , padx=7,bg=cor5,fg='white')
tela_label.place(x=0, y=0)

bot1 = Button(frame_corpo, command= lambda: Entrada_de_Valores('%'), text="%", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot1.place(x=0 , y=0)

bot2 = Button(frame_corpo, command= limpar_tudo,text="₠", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )

bot2.place(x=87, y=0)

bot3 = Button(frame_corpo, command= limpar_tudo,text="C", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )

bot3.place(x=170, y=0)

bot4 = Button(frame_corpo, command= limpar_tudo,text="◁", width=11,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )

bot4.place(x=250, y=0)

bot5 = Button(frame_corpo, command= lambda: Entrada_de_Valores('1/χ"'),text="1/χ", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )

bot5.place(x=0, y=60)

bot6 = Button(frame_corpo, command= lambda: Entrada_de_Valores('χ^2'),text="χ^2", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )

bot6.place(x=87, y=60)

bot7 = Button(frame_corpo, command= lambda: Entrada_de_Valores('√χ'),text="√χ", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot7.place(x=170 , y=60)

bot8 = Button(frame_corpo, command= lambda: Entrada_de_Valores('/'),text="÷", width=11,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot8.place(x=250, y=60)

bot9 = Button(frame_corpo, command= lambda: Entrada_de_Valores('7'),text="7", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot9.place(x=0, y=120)

bot10 = Button(frame_corpo, command= lambda: Entrada_de_Valores('8'),text="8", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot10.place(x=87, y=120)

bot11 = Button(frame_corpo, command= lambda: Entrada_de_Valores('9'),text="9", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot11.place(x=170, y=120)

bot12 = Button(frame_corpo, command= lambda: Entrada_de_Valores('*'),text="x", width=11,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot12.place(x=250, y=120)

bot13 = Button(frame_corpo, command= lambda: Entrada_de_Valores('4'),text="4", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot13.place(x=0, y=180)

bot14 = Button(frame_corpo, command= lambda: Entrada_de_Valores('5'),text="5", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot14.place(x=87, y=180)

bot15 = Button(frame_corpo, command= lambda: Entrada_de_Valores('6'),text="6", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot15.place(x=170, y=180)

bot16 = Button(frame_corpo, command= lambda: Entrada_de_Valores('-'),text="-", width=11,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot16.place(x=250, y=180)

bot17 = Button(frame_corpo, command= lambda: Entrada_de_Valores('1'),text="1", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot17.place(x=0, y=240)

bot18 = Button(frame_corpo, command= lambda: Entrada_de_Valores('2'),text="2", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot18.place(x=87, y=240)

bot19 = Button(frame_corpo, command= lambda: Entrada_de_Valores('3'),text="3", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot19.place(x=170, y=240)

bot20 = Button(frame_corpo, command= lambda: Entrada_de_Valores('+'),text="+", width=11,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot20.place(x=250, y=240)

bot21 = Button(frame_corpo, command= lambda: Entrada_de_Valores('±'),text="±", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot21.place(x=0, y=300)

bot22 = Button(frame_corpo, command= lambda: Entrada_de_Valores('0'),text="0", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot22.place(x=87, y=300)

bot23 = Button(frame_corpo, command= lambda: Entrada_de_Valores('.'),text=".", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot23.place(x=170, y=300)

bot24 = Button(frame_corpo, command= calcular,text="=", width=11,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot24.place(x=250, y=300)



area.mainloop()
