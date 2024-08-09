from tkinter                 import *
from tkinter                 import ttk
from timeit                  import *
from metodos.ponto_fixo      import MetodoPontoFixo
from metodos.newton_rhapson  import MetodoNewtonRhapson
from metodos.secante         import MetodoSecante
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot     as plt
import numpy                 as np


COLOR_BG_1 = '#FF7F50'
COLOR_BG_2 = '#FFEBE2'
COLOR_BG_3 = '#FFA07A'
COLOR_BG_4 = 'BLACK'

class Funcs(object):
    def style_treeview(self):
        ### Estilização customizada da tabela 1 e 2
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Custom.Treeview", 
                             background= COLOR_BG_2, 
                             fieldbackground=COLOR_BG_2, 
                             font=("Arial", 9))
                                
        self.style.configure("Custom.Treeview.Heading", 
                             background= COLOR_BG_1, 
                             fieldbackground=COLOR_BG_2,
                             font=("Arial", 9, 'bold'))
    
    def menu_submit(self):
        """
        Função que muda as colunas da tabela 1 e as entradas de variáveis,
        conforme o método selecionado pelo botão Submit
        """
        self.style_treeview()
        
        ### Condição para mudar as variáveis e a tabela1 conforme o método
        if self.metodo_var.get() == "Ponto Fixo" or self.metodo_var.get() == "Newton-Rhapson":
            
            ### Esconde a label e a entrada de q1 e coloca a de Tol no lugar
            self.hide_label()
            self.hide_entry()
            
            ### Criação da Tabela1
            self.tabela1 = ttk.Treeview(self.frame_2, height= 3, columns= ("col1", "col2", "col3", "col4", "col5"), style= "Custom.Treeview" )
            self.tabela1.heading("#0", text="")
            self.tabela1.heading("col1", text="Iter")
            self.tabela1.heading("col2", text="Q1")
            self.tabela1.heading("col3", text="Q")
            self.tabela1.heading("col4", text="Erro")
            self.tabela1.heading("col5", text="f(Q1)")

            self.tabela1.column("#0", width= 0)
            self.tabela1.column("#1", width= 10, anchor= CENTER)
            self.tabela1.column("#2", width= 80)
            self.tabela1.column("#3", width= 80)
            self.tabela1.column("#4", width= 80)
            self.tabela1.column("#5", width= 80)
            
            self.tabela1.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.77)

            ### Criação da Tabela2
            self.tabela2 = ttk.Treeview(self.frame_2, height= 3, columns= ("col1", "col2"), style= "Custom.Treeview")

            self.tabela2.heading("#0", text="")
            self.tabela2.heading("col1", text="Raiz")
            self.tabela2.heading("col2", text="Tempo")

            self.tabela2.column("#0", width=0)
            self.tabela2.column("col1", width=250, anchor= CENTER)
            self.tabela2.column("col2", width=200, anchor= CENTER)

            self.tabela2.place(relx=0.01, rely=0.80, relwidth=0.95, relheight=0.10)
            
            ### Criação da scrollbar
            self.scrollTabela = ttk.Scrollbar(self.frame_2, orient= 'vertical')
            self.tabela1.configure(yscroll=self.scrollTabela.set)
            self.scrollTabela.place(relx= 0.96, rely= 0.01, relwidth= 0.04, relheight= 0.77)
    

        elif self.metodo_var.get() == "Secante":
            ### Coloca a label e a entrada de q1 e muda de posição as de Tol 
            self.show_label()
            self.show_entry()

            ### Criação	da Tabela1
            self.tabela1 = ttk.Treeview(self.frame_2, height= 3, columns= ("col1", "col2", "col3", "col4", "col5", "col6"), style= "Custom.Treeview")
            self.tabela1.heading("#0", text="")
            self.tabela1.heading("col1", text="Iter")
            self.tabela1.heading("col2", text="Q2")
            self.tabela1.heading("col3", text="Q1")
            self.tabela1.heading("col4", text="Q0")
            self.tabela1.heading("col5", text="Erro")
            self.tabela1.heading("col6", text="f(Q2)")

            self.tabela1.column("#0", width= 0)
            self.tabela1.column("#1", width= 10, anchor= CENTER)
            self.tabela1.column("#2", width= 60)
            self.tabela1.column("#3", width= 60)
            self.tabela1.column("#4", width= 60)
            self.tabela1.column("#5", width= 60)
            self.tabela1.column("#6", width= 60)

            self.tabela1.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.77)
            
            ### Criação da Tabela2
            self.tabela2 = ttk.Treeview(self.frame_2, height= 3, columns= ("col1", "col2"), style= "Custom.Treeview")

            self.tabela2.heading("#0", text="")
            self.tabela2.heading("col1", text="Raiz")
            self.tabela2.heading("col2", text="Tempo")

            self.tabela2.column("#0", width=0)
            self.tabela2.column("col1", width=250, anchor= CENTER)
            self.tabela2.column("col2", width=200, anchor= CENTER)

            self.tabela2.place(relx=0.01, rely=0.80, relwidth=0.95, relheight=0.10)

            ### Scrollbar
            self.scrollTabela = ttk.Scrollbar(self.frame_2, orient= 'vertical')
            self.tabela1.configure(yscroll=self.scrollTabela.set)
            self.scrollTabela.place(relx= 0.96, rely= 0.01, relwidth= 0.04, relheight= 0.77)
        
    
    def hide_label(self):
            self.label_q1.place_forget()
            self.label_tol.place_forget()
            self.label_tol = Label(self.frame_3, text='Tol: ', background=COLOR_BG_3, 
                              font= ('Arial', '13', 'bold'))
            self.label_tol.place(relx=0.43, rely=0.39)
    def show_label(self):
            self.label_q0 = Label(self.frame_3, text='Q0 ', background=COLOR_BG_3, 
                              font= ('Arial', '13', 'bold'))
            self.label_q0.place(relx=0.43, rely=0.20)
            self.label_q1 = Label(self.frame_3, text='Q1 ', background=COLOR_BG_3, 
                                  font= ('Arial', '13', 'bold'))
            self.label_q1.place(relx=0.43, rely=0.39)

            self.label_tol = Label(self.frame_3, text='Tol ', background=COLOR_BG_3, 
                              font= ('Arial', '13', 'bold'))
            self.label_tol.place(relx=0.43, rely=0.58)
    def hide_entry(self):
            self.q1_entry.place_forget()
            self.tol_entry.place_forget()
            self.tol_entry = Entry(self.frame_3, background=COLOR_BG_2, 
                              font= ('Arial', '10'), justify= CENTER)
            self.tol_entry.place(relx=0.15, rely=0.46, relwidth= 0.70, relheight=0.07)
    def show_entry(self):
            self.q1_entry = Entry(self.frame_3, background=COLOR_BG_2, 
                                  font= ('Arial', '10'), justify= CENTER)
            self.q1_entry.place(relx=0.15, rely=0.46, relwidth= 0.70, relheight=0.07)

            self.tol_entry = Entry(self.frame_3, background=COLOR_BG_2, 
                              font= ('Arial', '10'), justify= CENTER)
            self.tol_entry.place(relx=0.15, rely=0.65, relwidth= 0.70, relheight=0.07)
            
    def clear_tabela1(self):
        for item in self.tabela1.get_children():
            self.tabela1.delete(item)
    def clear_tabela2(self):
        for item in self.tabela2.get_children():
            self.tabela2.delete(item)
        
    
### Funções de execução dos métodos
    def ponto_fixo(self, metodo):
        """
        Executa o método de ponto fixo até que o critério de parada seja atingido.
        """
        if abs(metodo.funcaoObjetivo(metodo.c, metodo.q0)) < metodo.tol:
            return metodo.q0

        for k in range(metodo.max_iter):
            q_next = metodo.funcaoIteracao(metodo.c, metodo.q0)
            e = q_next - metodo.q0

            ### printa na tabela1 os valores de cada iteração 
            iteracoes, q1, q, erro, f_q1 = [k, q_next, metodo.q0, e, metodo.funcaoObjetivo(metodo.c, q_next)]
            self.tabela1.insert("", "end", values=(f"{iteracoes}", f"{q1:.10f}", f"{q:.10f}", f"{erro:.10f}", f"{f_q1:.10f}"))

            if (
                abs(metodo.funcaoObjetivo(metodo.c, q_next)) < metodo.tol
                or abs(e) < metodo.tol
                or k >= metodo.max_iter
            ): 
                return q_next
                
            metodo.q0 = q_next
        raise ValueError("O método de ponto fixo não convergiu após o número máximo de iterações.")
    def newton_rhapson(self, metodo):
        """
        Executa o método de ponto fixo até que o critério de parada seja atingido.
        """
        if abs(metodo.funcaoObjetivo(metodo.c, metodo.q0)) < metodo.tol:
            return metodo.q0

        for k in range(metodo.max_iter):
            q_next = metodo.funcaoIteracao(metodo.c, metodo.q0)
            e = q_next - metodo.q0

            ### printa na tabela1 os valores de cada iteração 
            iteracoes, q1, q, erro, f_q1 = [k, q_next, metodo.q0, e, metodo.funcaoObjetivo(metodo.c, q_next)]
            self.tabela1.insert("", "end", values=(f"{iteracoes}", f"{q1:.10f}", f"{q:.10f}", f"{erro:.10f}", f"{f_q1:.10f}"))

            if (
                abs(metodo.funcaoObjetivo(metodo.c, q_next)) < metodo.tol
                or abs(e) < metodo.tol
                or k >= metodo.max_iter
            ):
                return q_next
                
            metodo.q0 = q_next

        raise ValueError("O método de ponto fixo não convergiu após o número máximo de iterações.")
    def secante(self, metodo):
        """
        Executa o método de ponto fixo até que o critério de parada seja atingido.
        """
        if abs(metodo.funcaoObjetivo(metodo.c, metodo.q0)) < metodo.tol:
            return metodo.q0
        if (
            abs(metodo.funcaoObjetivo(metodo.c, metodo.q1)) < metodo.tol 
            or abs(metodo.q1-metodo.q0) < metodo.tol
        ):
            return metodo.q1
            


        for k in range(metodo.max_iter):
            q_next = metodo.funcaoIteracao(metodo.c, metodo.q0, metodo.q1)
            e = q_next - metodo.q1

            ### printa na tabela1 os valores de cada iteração 
            iteracoes, q2, q1, q0, erro, f_q2 = [k, q_next, metodo.q1, metodo.q0, e, metodo.funcaoObjetivo(metodo.c, q_next)]
            self.tabela1.insert("", "end", values=(f"{iteracoes}", f"{q2:.10f}", f"{q1:.10f}", f"{q0:.10f}", f"{erro:.10f}", f"{f_q2:.10f}"))

            if (
                abs(metodo.funcaoObjetivo(metodo.c, q_next)) < metodo.tol
                or abs(e) < metodo.tol
                or k >= metodo.max_iter
            ):
                return q_next
                
            metodo.q0 = metodo.q1
            metodo.q1 = q_next

        raise ValueError("O método de ponto fixo não convergiu após o número máximo de iterações.")
    def executar_metodo(self):
        """
        Executa o método de ponto fixo, Newton-Raphson ou Secante
        dependendo do método escolhido pelo usuário.
        """

        ### Limpa as tabelas para os novos valores serem inseridos a seguir
        self.clear_tabela1()
        self.clear_tabela2()

        self.metodo_selecionado = self.metodo_var.get()
        if self.metodo_selecionado == "Ponto Fixo":
            c = float(self.c_entry.get())
            q0 = float(self.q0_entry.get())
            tol = float(self.tol_entry.get())
            metodo = MetodoPontoFixo(c, q0, tol)
        elif self.metodo_selecionado == "Newton-Rhapson":
            c = float(self.c_entry.get())
            q0 = float(self.q0_entry.get())
            tol = float(self.tol_entry.get())
            metodo = MetodoNewtonRhapson(c, q0, tol)
        elif self.metodo_selecionado == "Secante":
            c = float(self.c_entry.get())
            q0 = float(self.q0_entry.get())
            q1 = float(self.q1_entry.get())
            tol = float(self.tol_entry.get())
            metodo = MetodoSecante(c, q0, q1, tol)

        try:
            if self.metodo_selecionado == "Ponto Fixo":
                raiz = self.ponto_fixo(metodo)
                tempo = timeit(str(raiz), globals=globals(), number=1)
                ### printa na tabela 2 a raiz e tempo de execução
                self.tabela2.insert("", "end", values= (f"{raiz:.10f}", f"{tempo:.10f}"))
            elif self.metodo_selecionado == "Newton-Rhapson":
                raiz = self.newton_rhapson(metodo)
                tempo = timeit(str(raiz), globals=globals(), number=1)
                ### printa na tabela 2 a raiz e tempo de execução
                self.tabela2.insert("", "end", values= (f"{raiz:.10f}", f"{tempo:.10f}"))
            elif self.metodo_selecionado == "Secante":
                raiz = self.secante(metodo)
                tempo = timeit(str(raiz), globals=globals(), number=1)
                ### printa na tabela 2 a raiz e tempo de execução
                self.tabela2.insert("", "end", values= (f"{raiz:.10f}", f"{tempo:.10f}"))
        
        except Exception as e:
            print(f"An error occurred: {e}")

class Application(Funcs):
    """
    Classe de criação da GUI.
    """

    def __init__(self, master):
        """
        Inicializa a GUI.
        """
        self.master = master
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.widgets_frame2()
        self.widgets_frame3()    
    def tela(self):
        """
        Configuração da tela principal
        """
        self.master.title("Métodos Numéricos")
        self.master.geometry("720x480")
        self.master.configure(background= COLOR_BG_3)
        self.master.resizable(True, True)
        self.master.maxsize(width=900, height=700)
        self.master.minsize(width=400, height=300)
    def frames_da_tela(self):
        """
        Criação dos frames
        """
        ### Frame1
        self.frame_1 = Frame(self.master, background= COLOR_BG_3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.28, relheight=0.30)

        ### Frame2
        self.frame_2 = Frame(self.master, background=COLOR_BG_3)
        self.frame_2.place(relx=0.32, rely=0.02, relwidth=0.66, relheight=0.96)

        ### Frame3
        self.frame_3 = Frame(self.master, background= COLOR_BG_3)
        self.frame_3.place(relx=0.02, rely=0.22, relwidth=0.28, relheight=0.76)

    ### Widgets ###
    def widgets_frame1(self):
        """
        Criação do menu de seleção de método
        """
        self.lista_opcoes = ["Ponto Fixo", "Newton-Rhapson", "Secante"] 

        self.metodo_var = StringVar(self.master)
        self.metodo_var.set("Selecione o método")

        self.metodo_menu = OptionMenu(self.frame_1, self.metodo_var, *self.lista_opcoes)
        self.metodo_menu.configure(background= COLOR_BG_1, 
                                   border= 1, 
                                   activebackground=COLOR_BG_3, 
                                    highlightthickness=0, 
                                #    highlightbackground=COLOR_BG_2, 
                                   font=("Arial", 10, "bold"), 
                                   indicatoron=0)
        self.metodo_menu['menu'].config(background= COLOR_BG_1, 
                                        # border= 0, 
                                        activebackground=COLOR_BG_2, 
                                        activeforeground=COLOR_BG_4,  
                                        font=("Arial", 9, "bold"))
                                    
        self.metodo_menu.place(relx=0.15, rely=0.04, relwidth=0.70, relheight=0.20)

        ### Botão Submit
        self.bt_submit = Button(self.frame_1, text='Submit', background=COLOR_BG_2, 
                                highlightbackground=COLOR_BG_1, highlightthickness=3, 
                                border=1, activebackground=COLOR_BG_2,
                                command=self.menu_submit)
        self.bt_submit.place(relx=0.30, rely=0.26, relwidth=0.40, relheight=0.2)
    def widgets_frame2(self):
        """
        Criação a estrutura base da tabela1 e tabela2 que aparecem na tela inicial
        """
        ### Estilização das tabelas
        self.style_treeview()

        ### Criação da Tabela1
        self.tabela1 = ttk.Treeview(self.frame_2, height= 3, columns= ("col1", "col2", "col3", "col4", "col5", "col6"), style= "Custom.Treeview")
        self.tabela1.heading("#0", text="")
        self.tabela1.heading("col1", text="")
        self.tabela1.heading("col2", text="")
        self.tabela1.heading("col3", text="")
        self.tabela1.heading("col4", text="")
        self.tabela1.heading("col5", text="")
        self.tabela1.heading("col6", text="")

        self.tabela1.column("#0", width=0)
        self.tabela1.column("col1", width=50)
        self.tabela1.column("col2", width=50)
        self.tabela1.column("col3", width=50)
        self.tabela1.column("col4", width=50)
        self.tabela1.column("col5", width=50)
        self.tabela1.column("col6", width=50)

        self.tabela1.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.77)

        
        ### Criação da Tabela2
        self.tabela2 = ttk.Treeview(self.frame_2, height= 3, columns= ("col1", "col2"), style= "Custom.Treeview")

        self.tabela2.heading("#0", text="")
        self.tabela2.heading("col1", text="Raiz")
        self.tabela2.heading("col2", text="Tempo")

        self.tabela2.column("#0", width=0)
        self.tabela2.column("col1", width=250, anchor= CENTER)
        self.tabela2.column("col2", width=200, anchor= CENTER)

        self.tabela2.place(relx=0.01, rely=0.80, relwidth=0.95, relheight=0.10)

        ### Criação da scrollbar
        self.scrollTabela = ttk.Scrollbar(self.frame_2, orient= 'vertical')
        self.tabela1.configure(yscroll=self.scrollTabela.set)
        self.scrollTabela.place(relx= 0.96, rely= 0.01, relwidth= 0.04, relheight= 0.77)

    def widgets_frame3(self):
        """
        Criação das labels e entradas do código
        """
        ### Label C
        self.label_c = Label(self.frame_3, text='C ', background=COLOR_BG_3, 
                             font= ('Arial', '13', 'bold'))
        self.label_c.place(relx=0.45, rely=0.01)
        self.c_entry = Entry(self.frame_3, background=COLOR_BG_2, 
                             font= ('Arial', '10'), justify= CENTER)
        self.c_entry.place(relx=0.15, rely=0.08, relwidth= 0.70, relheight=0.07)

        ### Label q0
        self.label_q0 = Label(self.frame_3, text='Q ', background=COLOR_BG_3, 
                              font= ('Arial', '13', 'bold'))
        self.label_q0.place(relx=0.45, rely=0.20)
        self.q0_entry = Entry(self.frame_3, background=COLOR_BG_2, 
                              font= ('Arial', '10'), justify= CENTER)
        self.q0_entry.place(relx=0.15, rely=0.27, relwidth= 0.70, relheight=0.07)

        ### Label q1
        self.label_q1 = Label(self.frame_3, text='Q1 ', background=COLOR_BG_3, 
                              font= ('Arial', '13', 'bold'))
        self.label_q1.place(relx=0.43, rely=0.39)
        self.q1_entry = Entry(self.frame_3, background=COLOR_BG_2, 
                              font= ('Arial', '10'), justify= CENTER)
        self.q1_entry.place(relx=0.15, rely=0.46, relwidth= 0.70, relheight=0.07)

        ### Label Tol (erro absoluto)
        self.label_tol = Label(self.frame_3, text='Tol ', background=COLOR_BG_3, 
                              font= ('Arial', '13', 'bold'))
        self.label_tol.place(relx=0.43, rely=0.58)
        self.tol_entry = Entry(self.frame_3, background=COLOR_BG_2, 
                              font= ('Arial', '10'), justify= CENTER)
        self.tol_entry.place(relx=0.15, rely=0.65, relwidth= 0.70, relheight=0.07)


        ### Botão Executar
        self.bt_executar = Button(self.frame_3, text='Executar', background=COLOR_BG_2, 
                                  highlightbackground=COLOR_BG_3, highlightthickness=3,
                                  activebackground= COLOR_BG_2,
                                  border=1, command=self.executar_metodo)
        self.bt_executar.place(relx=0.30, rely=0.79, relwidth=0.40, relheight=0.08)
    
    def mainloop(self):
        self.master.mainloop()