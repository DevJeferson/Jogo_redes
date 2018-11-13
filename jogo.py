#Desenvolvimento de Interface Grafica
#coding: utf8

from tkinter import *

#Funcoes
#-----------------------------------------------------------------
def bt_click():
    print("bt_click")

    lb["text"] = "NUM de Casas a Percorrer"

#funcao do bot usr
#serve para obter valor que foi digitado
def bt_onclick():
    print(ed.get())  #a funcao get retorna o valor que foi digitado no nosso campo



#-------------------------------------------------------------------

janela = Tk()
janela.title("Jogo de Redes")

#componente nome pessoa(caixa de entrada)
ed = Entry(janela)
ed.place(x=900,y=200) #posicao

janela["bg"] = "green"
janela["background"] = "green"

#botoes
#--------------------------------------------------------------------

bt = Button(janela, width=20,text="OK" , command=bt_onclick)  #botao nome usr
bt.place(x=900,y=250)
lb= Label(janela, text = "Insira seu Nome:", bg="green")
lb.place(x=900,y=150)

#BOT Gerar num--
bt0= Button(janela, width=20, height=3, text="CLIQUE AQUI PARA INICIAR",command=bt_click)
bt0.place(x=350, y=400)
#---

bt = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt.place(x=50, y=50)

bt1 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt1.place(x=50, y=200)

bt2 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt2.place(x=50, y=350)

bt3 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt3.place(x=50, y=500)
#-------------------------------------------------------------------
bt4 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt4.place(x=165, y=500)

bt5 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt5.place(x=280, y=500)

bt6 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt6.place(x=395, y=500)

bt7 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt7.place(x=510, y=500)

bt8 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt8.place(x=625, y=500)

bt9 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt9.place(x=740, y=500)
#-------------------------------------------------------------------

bt10 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt10.place(x=740, y=350)

bt11 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt11.place(x=740, y=200)

bt12 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt12.place(x=740, y=50)
#-----------------------------------------------------------------
bt13 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt13.place(x=625, y=50)

bt14 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt14.place(x=510, y=50)

bt15 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt15.place(x=395, y=50)

bt16 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt16.place(x=280, y=50)

bt17 = Button(janela, width=8, height=8, text="OK",command=bt_click)
bt17.place(x=165, y=50)

























#label INICIO JOGO
lb = Label(janela, text="...", bg="green")
lb.place(x=360, y=300)
#label vazio
lb_on= Label(janela,width=5, height=3, text="                        ", bg="White")
lb_on.place(x=420, y=330)



#LxA+dist_Esq+dist_Topo-video
#300x300+100+100
janela.geometry("2000x720+200+200")
janela.mainloop()
