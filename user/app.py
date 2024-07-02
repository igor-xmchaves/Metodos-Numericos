from tkinter                 import *
from tkinter                 import ttk
from metodos.ponto_fixo      import MetodoPontoFixo
from metodos.newton_rhapson  import MetodoNewtonRhapson
from metodos.secante         import MetodoSecante


class Funcs(object):
    def style_treeview(self):
        ### Estilização customizada da tabela
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Custom.Treeview",
                                background= '#FFEBE2',
                                fieldbackground="#FFEBE2",
                                font=("Arial", 9))
                                
        self.style.configure("Custom.Treeview.Heading", 
                                background= '#FFA07A',
                                fieldbackground="#FFEBE2",
                                font=("Arial", 9, 'bold'))
    
    def scrollbar_treeview(self):
        ### Criação da scrollbar
        self.scrollTabela = ttk.Scrollbar(self.frame_2, orient= 'vertical')
        self.tabela.configure(yscroll=self.scrollTabela.set)
        self.scrollTabela.place(relx= 0.96, rely= 0.01, relwidth= 0.04, relheight= 0.98)
    
    def menu_submit(self):
        
        self.style_treeview()
        self.scrollbar_treeview()
        
        ### Condição para mudar as variáveis e a tabela conforme o método
        if self.metodo_var.get() == "Ponto Fixo" or self.metodo_var.get() == "Newton-Rhapson":
            self.hide_label()
            self.hide_entry()
            
            self.tabela = ttk.Treeview(self.frame_2, height= 3, columns= ("col1", "col2", "col3", "col4", "col5"), style= "Custom.Treeview" )
            self.tabela.heading("#0", text="")
            self.tabela.heading("col1", text="Iter")
            self.tabela.heading("col2", text="Q1")
            self.tabela.heading("col3", text="Q")
            self.tabela.heading("col4", text="Erro")
            self.tabela.heading("col5", text="f(Q1)")

            self.tabela.column("#0", width= 1)
            self.tabela.column("#1", width= 10)
            self.tabela.column("#2", width= 50)
            self.tabela.column("#3", width= 50)
            self.tabela.column("#4", width= 50)
            self.tabela.column("#5", width= 50)
            
            self.tabela.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.98)
            

        elif self.metodo_var.get() == "Secante":
            self.show_label()
            self.show_entry()

            self.tabela = ttk.Treeview(self.frame_2, height= 3, columns= ("col1", "col2", "col3", "col4", "col5", "col6"), style= "Custom.Treeview")
            self.tabela.heading("#0", text="")
            self.tabela.heading("col1", text="Iter")
            self.tabela.heading("col2", text="Q2")
            self.tabela.heading("col3", text="Q1")
            self.tabela.heading("col4", text="Q0")
            self.tabela.heading("col5", text="Erro")
            self.tabela.heading("col6", text="f(Q2)")

            self.tabela.column("#0", width= 1)
            self.tabela.column("#1", width= 10)
            self.tabela.column("#2", width= 50)
            self.tabela.column("#3", width= 50)
            self.tabela.column("#4", width= 50)
            self.tabela.column("#5", width= 50)
            self.tabela.column("#6", width= 50)

            self.tabela.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.98)

            self.scrollTabela = Scrollbar(self.frame_2, orient= 'vertical')
            self.tabela.configure(yscroll=self.scrollTabela.set)
            self.scrollTabela.place(relx= 0.96, rely= 0.01, relwidth= 0.04, relheight= 0.98)
    def hide_label(self):
            self.label_q1.place_forget()
    def show_label(self):
            self.label_q1 = Label(self.frame_3, text='Q1: ', background='#FF7F50', 
                                  font= ('Arial', '13', 'bold'))
            self.label_q1.place(relx=0.43, rely=0.59)

    def hide_entry(self):
            self.q1_entry.place_forget()
    def show_entry(self):
            self.q1_entry = Entry(self.frame_3, background='#F8DDD0', 
                                  font= ('Arial', '10'), justify= CENTER)
            self.q1_entry.place(relx=0.15, rely=0.66, relwidth= 0.70, relheight=0.07)
    def clear_treeview(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

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

            iteracoes, q1, q, erro, f_q1 = [k, q_next, metodo.q0, e, metodo.funcaoObjetivo(metodo.c, q_next)]
            self.tabela.insert("", "end", values=(iteracoes, q1, q, erro, f_q1))

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

            iteracoes, q1, q, erro, f_q1 = [k, q_next, metodo.q0, e, metodo.funcaoObjetivo(metodo.c, q_next)]
            self.tabela.insert("", "end", values=(iteracoes, q1, q, erro, f_q1))

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

            iteracoes, q2, q1, q0, erro, f_q2 = [k, q_next, metodo.q1, metodo.q0, e, metodo.funcaoObjetivo(metodo.c, q_next)]
            self.tabela.insert("", "end", values=(iteracoes, q2, q1, q0, erro, f_q2))

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
        self.clear_treeview()

        self.metodo_selecionado = self.metodo_var.get()
        if self.metodo_selecionado == "Ponto Fixo":
            c = float(self.c_entry.get())
            q0 = float(self.q0_entry.get())
            metodo = MetodoPontoFixo(c, q0)
        elif self.metodo_selecionado == "Newton-Rhapson":
            c = float(self.c_entry.get())
            q0 = float(self.q0_entry.get())
            metodo = MetodoNewtonRhapson(c, q0)
        elif self.metodo_selecionado == "Secante":
            c = float(self.c_entry.get())
            q0 = float(self.q0_entry.get())
            q1 = float(self.q1_entry.get())
            metodo = MetodoSecante(c, q0, q1)

        try:
            if self.metodo_selecionado == "Ponto Fixo":
                self.ponto_fixo(metodo)
            elif self.metodo_selecionado == "Newton-Rhapson":
                self.newton_rhapson(metodo)
            elif self.metodo_selecionado == "Secante":
                self.secante(metodo)
        
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
        self.widgets_frame4()
    def tela(self):
        self.master.title("Métodos Numéricos")
        self.master.geometry("720x480")
        self.master.configure(background='#FF7F50')
        self.master.resizable(True, True)
        self.master.maxsize(width=900, height=700)
        self.master.minsize(width=400, height=300)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.master, background='#FF7F50')
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.28, relheight=0.30)

        self.frame_2 = Frame(self.master, background='#FFEBE2', 
                             highlightbackground='#FFA07A', highlightthickness=3)
        self.frame_2.place(relx=0.32, rely=0.02, relwidth=0.66, relheight=0.96)

        self.frame_3 = Frame(self.master, background='#FF7F50')
        self.frame_3.place(relx=0.02, rely=0.22, relwidth=0.28, relheight=0.76)

        self.frame_4 = Frame(self.master, background='#FF7F50')
        self.frame_4.place(relx=0.02, rely=0.79, relwidth=0.28, relheight=0.18)

    ### Widgets ###
    def widgets_frame1(self):
        """
        Criação do menu de seleção de método
        """
        self.lista_opcoes = ["Ponto Fixo", "Newton-Rhapson", "Secante"] 

        self.metodo_var = StringVar(self.master)
        self.metodo_var.set("-- Selecione --")

        self.label_metodo = Label(self.frame_1, text= 'Escolha o método:', background='#FF7F50', 
                                  font= ('Arial', '13', 'bold'))
        self.label_metodo.place(relx=0.12, rely=0.02)

        self.metodo_menu = OptionMenu(self.frame_1, self.metodo_var, *self.lista_opcoes)
        self.metodo_menu.configure(background= '#FFA07A', 
                                   border= 0, 
                                   activebackground='#FFEBE2', 
                                   highlightthickness=1, 
                                   highlightbackground='#FFEBE2', 
                                   font=("Arial", 10), 
                                   indicatoron=0)
        self.metodo_menu['menu'].config(background= '#FFA07A', 
                                        border= 0, 
                                        activebackground='#FFEBE2', 
                                        activeforeground='black',  
                                        font=("Arial", 10))
                                    
        self.metodo_menu.place(relx=0.15, rely=0.2, relwidth=0.70, relheight=0.20)

        self.bt_submit = Button(self.frame_1, text='Submit', background='#FFEBE2', 
                                highlightbackground='#FFA07A', highlightthickness=3, 
                                border=1, command=self.menu_submit)
        self.bt_submit.place(relx=0.30, rely=0.42, relwidth=0.40, relheight=0.2)
    def widgets_frame2(self):
        """
        Cria a estrutura base da tabela que aparece antes de selecionar o método
        """

        self.style_treeview()
        self.scrollbar_treeview()

        self.tabela = ttk.Treeview(self.frame_2, height= 3, columns= ("col1", "col2", "col3", "col4", "col5", "col6"), style= "Custom.Treeview")
        self.tabela.heading("#0", text="")
        self.tabela.heading("col1", text="")
        self.tabela.heading("col2", text="")
        self.tabela.heading("col3", text="")
        self.tabela.heading("col4", text="")
        self.tabela.heading("col5", text="")
        self.tabela.heading("col6", text="")

        self.tabela.column("#0", width=1)
        self.tabela.column("col1", width=50)
        self.tabela.column("col2", width=50)
        self.tabela.column("col3", width=50)
        self.tabela.column("col4", width=50)
        self.tabela.column("col5", width=50)
        self.tabela.column("col6", width=50)

        self.tabela.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.98)

    def widgets_frame3(self):
        """
        Criação da label e entrada do código
        """
        self.label_c = Label(self.frame_3, text='C: ', background='#FF7F50', 
                             font= ('Arial', '13', 'bold'))
        self.label_c.place(relx=0.45, rely=0.15)
        self.c_entry = Entry(self.frame_3, background='#F8DDD0', 
                             font= ('Arial', '10'), justify= CENTER)
        self.c_entry.place(relx=0.15, rely=0.22, relwidth= 0.70, relheight=0.07)

        self.label_q0 = Label(self.frame_3, text='Q0: ', background='#FF7F50', 
                              font= ('Arial', '13', 'bold'))
        self.label_q0.place(relx=0.43, rely=0.37)
        self.q0_entry = Entry(self.frame_3, background='#F8DDD0', 
                              font= ('Arial', '10'), justify= CENTER)
        self.q0_entry.place(relx=0.15, rely=0.44, relwidth= 0.70, relheight=0.07)

        self.label_q1 = Label(self.frame_3, text='Q1: ', background='#FF7F50', 
                              font= ('Arial', '13', 'bold'))
        self.label_q1.place(relx=0.43, rely=0.59)
        self.q1_entry = Entry(self.frame_3, background='#F8DDD0', 
                              font= ('Arial', '10'), justify= CENTER)
        self.q1_entry.place(relx=0.15, rely=0.66, relwidth= 0.70, relheight=0.07)
    def widgets_frame4(self):
        """
        Criação botão executar
        """
        self.bt_executar = Button(self.frame_4, text='Executar', background='#FFEBE2', 
                                  highlightbackground='#FFA07A', highlightthickness=3, 
                                  border=1, command=self.executar_metodo)
        self.bt_executar.place(relx=0.30, rely=0.3, relwidth=0.40, relheight=0.36)
    
    def mainloop(self):
        self.master.mainloop()