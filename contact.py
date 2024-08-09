from tkinter import *
from tkinter import ttk
import customtkinter

janela = Tk()
lista = []

def salvar(nome, numero, email, frame_comando_soma):
    nome = nome.get()
    numero = numero.get()
    email = email.get()
    
    lista.append((nome, numero, email))
    atualizar(lista) 
    frame_comando_soma.destroy() 

def atualizar(lista_todos_os_ctts): 
    for widget in sc.winfo_children():
        widget.destroy() #parte que destroi a lista antiga para criar uma nova
        
    for nome, numero, email in lista_todos_os_ctts:#recria a lista em frames
        frame_a_mostra = customtkinter.CTkFrame(sc, fg_color='orange', height=80, width=355)
        frame_a_mostra.grid(pady=2)
        
        label = customtkinter.CTkLabel(frame_a_mostra, text=("Nome: {}\nNúmero: {}\nEmail: {}").format(nome,numero,email))
        label.place(relx=0.05, rely=0.1)
        
        botao_de_frame_a_mostra = Button(frame_a_mostra, text="x", command=lambda: frame_a_mostra.destroy()) 
        botao_de_frame_a_mostra.place(relx=0.92, rely=0.05, relwidth=0.07, relheight=0.23)

def sair(frame_comando_soma):
    frame_comando_soma.destroy()

def comando_soma():
    frame_comando_soma = Frame(janela, bg="orange")
    frame_comando_soma.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)
    
    botao_quit = customtkinter.CTkButton(frame_comando_soma, text_color="black", text="X", font=("Comic Sans MS", 13, "bold"), command=lambda: sair(frame_comando_soma))
    botao_quit.place(relx=0.92, rely=0.02, relwidth=0.072, relheight=0.07)
    
    Label(frame_comando_soma, fg="black", bg="orange", text="Novo\n Contato !".upper(), font=("Comic Sans MS", 15, "bold")).place(relx=0.3, rely=0.08)
    
    nome_label = Label(frame_comando_soma, fg="black", bg="orange", text="Nome:", font=("Comic Sans MS", 13, "bold"))
    nome_label.place(relx=0.15, rely=0.4)
    nome = customtkinter.CTkEntry(frame_comando_soma, placeholder_text="Nome do contato")
    nome.place(relx=0.37, rely=0.4)
    
    numero_label = Label(frame_comando_soma, fg="black", bg="orange", text="Número:", font=("Comic Sans MS", 13, "bold"))
    numero_label.place(relx=0.13, rely=0.5)
    numero = customtkinter.CTkEntry(frame_comando_soma, placeholder_text="Nº de telefone")
    numero.place(relx=0.37, rely=0.5)
    
    email_label = Label(frame_comando_soma, fg="black", bg="orange", text="Email:", font=("Comic Sans MS", 13, "bold"))
    email_label.place(relx=0.15, rely=0.6)
    email = customtkinter.CTkEntry(frame_comando_soma, placeholder_text="Email do contato")
    email.place(relx=0.37, rely=0.6)
    
    botao_salvar_contato = customtkinter.CTkButton(frame_comando_soma, text_color="black", text="SALVAR", command=lambda: salvar(nome, numero, email, frame_comando_soma))
    botao_salvar_contato.place(relx=0.38, rely=0.73, relwidth=0.3, relheight=0.14)

def pesquisa_func():
    texto_pesquisa = pesquisa.get().lower()
    
    lista_filtrada = []
    for contato in lista:
        nome, numero, email = contato
        if (texto_pesquisa in nome.lower() or texto_pesquisa in numero.lower() or texto_pesquisa in email.lower()):
            lista_filtrada.append(contato)
    
    atualizar(lista_filtrada)

frame1 = Frame(janela, background="#FFD700")
frame1.place(relx=0.4, rely=0.045, anchor='center', relwidth=0.76, relheight=0.05)

pesquisa = Entry(frame1, font=("Georgia"), background="#DEE7E9")
pesquisa.place(relwidth=1, relheight=1)

botao_pesquisa = Button(frame1, text="Pesquisar",background="orange", command=pesquisa_func)
botao_pesquisa.place(relx=0.85, rely=0.5, anchor='center', relwidth=0.3, relheight=1)

botao_mais = Button(janela, text="+", font=("Arial", 24), bg="orange", command=comando_soma)
botao_mais.place(relx=0.9, rely=0.05, anchor='center', relwidth=0.13, relheight=0.075)

sc = customtkinter.CTkScrollableFrame(janela)
sc.place(relx=0.03, rely=0.1, relwidth=0.95, relheight=0.89)

atualizar(lista)

janela.iconphoto(0, PhotoImage(file="C:\\Users\\Júlia\\Desktop\\agenda\\transferir (1).png"))
janela.configure(background="#008B8B")
janela.geometry("400x570")
janela.resizable(0, 0)
janela.title("Agenda")

janela.mainloop()
