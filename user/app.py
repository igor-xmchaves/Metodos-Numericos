from tkinter                 import *
from metodos.ponto_fixo      import MetodoPontoFixo
from metodos.newton_rhapson  import MetodoNewtonRhapson
from metodos.secante         import MetodoSecante


class Funcs(object):
    def menu_submit(self):
        if self.metodo_var.get() == "Ponto Fixo" or self.metodo_var.get() == "Newton-Rhapson":
            self.hide_label()
            self.hide_entry()

        elif self.metodo_var.get() == "Secante":
            self.show_label()
            self.show_entry()
    
    def hide_label(self):
            self.label_q1.place_forget()
    def show_label(self):
            self.label_q1 = Label(self.frame_3, text='Q1: ', background='#FF7F50', font= ('Arial', '13', 'bold'))
            self.label_q1.place(relx=0.43, rely=0.59)

    def hide_entry(self):
            self.q1_entry.place_forget()
    def show_entry(self):
            self.q1_entry = Entry(self.frame_3, background='#F8DDD0', font= ('Arial', '10'), justify= CENTER)
            self.q1_entry.place(self.q1_entry.place(relx=0.15, rely=0.66, relwidth= 0.70, relheight=0.07))

    def executar_metodo(self):
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
            metodo.executar()
        except Exception as e:
            print(f"An error occurred: {e}")


class Application(Funcs):
    """
    A class for creating a GUI interface.
    """

    def __init__(self, master):
        """
        Initialize the GUI interface.
        """
        self.master = master
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.widgets_frame3()
        self.widgets_frame4()

    def tela(self):
        self.master.title("Métodos Numéricos")
        self.master.geometry("720x480")  # Set the window size
        self.master.configure(background='#FF7F50')
        self.master.resizable(True, True)
        self.master.maxsize(width=900, height=700)
        self.master.minsize(width=400, height=300)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.master, background='#FF7F50')
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.28, relheight=0.30)

        self.frame_2 = Frame(self.master, background='#FFEBE2', highlightbackground='#FFA07A', highlightthickness=3)
        self.frame_2.place(relx=0.32, rely=0.02, relwidth=0.66, relheight=0.96)

        self.frame_3 = Frame(self.master, background='#FF7F50')
        self.frame_3.place(relx=0.02, rely=0.22, relwidth=0.28, relheight=0.76)

        self.frame_4 = Frame(self.master, background='#FF7F50')
        self.frame_4.place(relx=0.02, rely=0.79, relwidth=0.28, relheight=0.18)

    def widgets_frame1(self):
        self.lista_opcoes = ["Ponto Fixo", "Newton-Rhapson", "Secante"] 

        self.metodo_var = StringVar(self.master)
        self.metodo_var.set("--Selecione--")

        self.label_metodo = Label(self.frame_1, text= 'Escolha o método:', background='#FF7F50', font= ('Arial', '13', 'bold'))
        self.label_metodo.place(relx=0.12, rely=0.02)

        self.metodo_menu = OptionMenu(self.frame_1, self.metodo_var, *self.lista_opcoes)
        self.metodo_menu.place(relx=0.15, rely=0.2, relwidth=0.70, relheight=0.20)

        self.bt_submit = Button(self.frame_1, text='Submit', background='#FFEBE2', highlightbackground='#FFA07A', highlightthickness=3, command=self.menu_submit)
        self.bt_submit.place(relx=0.30, rely=0.42, relwidth=0.40, relheight=0.2)
    
    def widgets_frame3(self):

        ### Criação da label e entrada do código
        self.label_c = Label(self.frame_3, text='C: ', background='#FF7F50', font= ('Arial', '13', 'bold'))
        self.label_c.place(relx=0.45, rely=0.15)
        self.c_entry = Entry(self.frame_3, background='#F8DDD0', font= ('Arial', '10'), justify= CENTER)
        self.c_entry.place(relx=0.15, rely=0.22, relwidth= 0.70, relheight=0.07)

        self.label_q0 = Label(self.frame_3, text='Q0: ', background='#FF7F50', font= ('Arial', '13', 'bold'))
        self.label_q0.place(relx=0.43, rely=0.37)
        self.q0_entry = Entry(self.frame_3, background='#F8DDD0', font= ('Arial', '10'), justify= CENTER)
        self.q0_entry.place(relx=0.15, rely=0.44, relwidth= 0.70, relheight=0.07)

        self.label_q1 = Label(self.frame_3, text='Q1: ', background='#FF7F50', font= ('Arial', '13', 'bold'))
        self.label_q1.place(relx=0.43, rely=0.59)
        self.q1_entry = Entry(self.frame_3, background='#F8DDD0', font= ('Arial', '10'), justify= CENTER)
        self.q1_entry.place(relx=0.15, rely=0.66, relwidth= 0.70, relheight=0.07)

    def widgets_frame4(self):
        ### Criação botão executar
        self.bt_executar = Button(self.frame_4, text='Executar', background='#FFEBE2', highlightbackground='#FFA07A', highlightthickness=3, command=self.executar_metodo)
        self.bt_executar.place(relx=0.30, rely=0.3, relwidth=0.40, relheight=0.36)

    def mainloop(self):
        self.master.mainloop()