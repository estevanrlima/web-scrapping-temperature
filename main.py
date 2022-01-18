from tkinter import *
from get_city import get_city_tmin_and_tmax
from help import help

def print_temps(index):
    cidade, tmin, tmax = get_city_tmin_and_tmax(str(city_index[index]))
    sample = Label(text=cidade + ': temperatura mínima: ' + tmin + ', temperatura máxima: ' + tmax, background='#dde') # texto a ser colocado na interface
    sample.pack()  

def print_city(index):
    for child in app.winfo_children():
        child.destroy()
    print_temps(index = index)

city_index = [262,263,264,265,266,267,268,269,270,271] # lista com cidades, pode ser alterada por outros números

city_list = [] # inicia uma lista que armazenará os nomes das cidades
tmin_list = [] # inicia uma lista que armazenará as temperaturas mínimas das cidades
tmax_list = [] # inicia uma lista que armazenará as temperaturas máximas das cidades

app = Tk() # inicia uma instância da classe Tk

app.title('Temperatura') # título da aplicação
app.geometry('500x300') # tamanho da tela
app.configure(background="#dde") # cor de fundo da tela

Label(app, text="Escolha uma cidade", background="#dde").place(x=180, y=0, width=150, height=20)

Button(app, text="Paulista - PI", command= lambda: print_city(index=0)).place(x=200,y=20,width=100,height=20)
Button(app, text="Picos - PI", command= lambda: print_city(index=1)).place(x=200,y=40,width=100,height=20)
Button(app, text="Teresina - PI", command= lambda: print_city(index=2)).place(x=200,y=60,width=100,height=20)
Button(app, text="Andirá - PI", command= lambda: print_city(index=3)).place(x=200,y=80,width=100,height=20)
Button(app, text="Arapongas - PR", command= lambda: print_city(index=4)).place(x=200,y=100,width=100,height=20)
Button(app, text="C. Mourao - PR", command= lambda: print_city(index=5)).place(x=200,y=120,width=100,height=20)
Button(app, text="Cascavel - PR", command= lambda: print_city(index=6)).place(x=200,y=140,width=100,height=20)
Button(app, text="Castro - PR", command= lambda: print_city(index=7)).place(x=200,y=160,width=100,height=20)
Button(app, text="Cianorte - PR", command= lambda: print_city(index=8)).place(x=200,y=180,width=100,height=20)
Button(app, text="Curitiba - PR", command= lambda: print_city(index=9)).place(x=200,y=200,width=100,height=20)

app.mainloop()
