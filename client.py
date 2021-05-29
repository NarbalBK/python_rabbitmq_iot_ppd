import tkinter as tk
import tkmacosx as tkm
import threading
from mainInfoReceivier import MainInfoReceivier

class MainInterface:
    def __init__(self):
        #ROOT
        root = tk.Tk()
        root.title("Monitor de Sensores")
        w, h = 800, 600
        root.geometry('{}x{}'.format(w, h))
        root.config(bg="black")

        #TITLE
        lbl_title = tk.Label(root, text="Monitor de Sensores", font=('Helvatical bold',40), bg="black", fg="white")
        lbl_title.pack(pady=15)

        #MENU LABEL
        lbl_menu = tk.Label(root, text="Escolha um sensor que deseja monitorar", font=('Helvatical bold',18), bg="black", fg="white")
        lbl_menu.pack()
        lbl_info = tk.Label(root, text="Click (+) para adcionar", font=('Helvatical bold',12), bg="black", fg="white")
        lbl_info.pack()

        #MENU OPTIONS
        OPTIONS = ["Temperatura","Umidade","Velocidade"] 

        #DROPDOWN MENU DEFAULT
        option_value = tk.StringVar(root)
        option_value.set(OPTIONS[0])
        self.selection = OPTIONS[0]

        #ICONS
        img_add = tk.PhotoImage(file="./img/add.gif")
        self.img_all = {"Temperatura": tk.PhotoImage(file="./img/temperatura.gif"),
                    "Umidade": tk.PhotoImage(file="./img/umidade.gif"), 
                    "Velocidade": tk.PhotoImage(file="./img/velocidade.gif")}

        #SELECTOR MENU
        frm_add_menu = tk.Frame(root, pady=20, bg="black") # ADD MENU - FRAME START
        
        opt_sensor_type = tk.OptionMenu(frm_add_menu, option_value, *OPTIONS, command=self.get_option)
        opt_sensor_type.config(bg="black")
        opt_sensor_type.pack(side=tk.LEFT, fill=tk.BOTH)
        self.opt_sensor_type = opt_sensor_type

        btn_add_sensor = tkm.Button(frm_add_menu, image=img_add, 
            bg="black", fg="black", command=self.create_monitor,
            highlightthickness = 0, bd = 0)

        btn_add_sensor.pack(side=tk.LEFT)
        self.btn_add_sensor = btn_add_sensor                                          

        frm_add_menu.pack() # ADD MENU - FRAME END    

        frm_sensors = tk.Frame(root, bg="black") # SENSORS - FRAME START
        frm_sensors.pack()
        self.frm_sensors = frm_sensors   # SENSORS - FRAME END            

        self.root = root

    def start_root(self):
        self.root.mainloop()

    def get_option(self, value):
        self.selection = value
        self.btn_add_sensor["state"] = "normal"

    def create_monitor(self):
        frm_generic = tk.Frame(self.frm_sensors, bg="black") # FRAME MONITOR - START

        cvs = tk.Canvas(frm_generic, width = 200, height = 200, bg="black", bd=0, highlightthickness=0)  
        cvs.create_image(100, 100, image=self.img_all[self.selection])
        cvs.pack()
         
        lbl_value = tk.Label(frm_generic, text="0.0 {}".format(self.get_metric()), font=('Helvatical bold',20), bg="black", fg="white")
        lbl_value.pack(pady=8)

        frm_lbox = tk.Frame(frm_generic) # FRAME LIST BOX - START

        scrollbar = tk.Scrollbar(frm_lbox)
        lbox_value_list = tk.Listbox(frm_lbox, width=25, height=8, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        lbox_value_list.pack(side=tk.LEFT, fill=tk.BOTH)

        frm_lbox.pack() # FRAME LIST BOX - END

        frm_generic.pack(side=tk.LEFT, fill=tk.BOTH, pady=5) # FRAME MONITOR - END

        #DISABLE ITEM OPTION AND BUTTON
        self.opt_sensor_type['menu'].entryconfigure(self.selection, state = "disabled") 
        self.btn_add_sensor["state"] = "disabled"


        # TODO PEGAR REFERNCIA DE LISTBOX PARA INSERIR A MSG NO MONITOR CERTO
        # print(self.frm_sensors.winfo_children())

        # TODO INCLUIR MENSAGEM DO RABBIT NA TELA
        # lbox_value_list.insert(tk.END, "ABEL")
        # lbox_value_list.insert(tk.END, "GIRAFA DE FOGO")

    def get_metric(self):
        if self.selection == "Umidade":
            return "%"
        elif self.selection == "Velocidade":
            return "m/s"
        return "ºC"

def main():
    mainInterface = MainInterface()
    mainInfoReceiverThread = threading.Thread(target=buildMainInfoReceiver, daemon=True)
    mainInfoReceiverThread.start()
    mainInterface.start_root()

def buildMainInfoReceiver():
    mainInfoReceivier = MainInfoReceivier()

if __name__ == "__main__":
    main()
    




     


