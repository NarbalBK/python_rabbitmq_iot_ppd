import tkinter as tk
import tkmacosx as tkm
from infoReceiver import InfoReceiver
import threading

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
        lbl_menu = tk.Label(root, text="Escolha o nome do sensor que deseja monitorar", font=('Helvatical bold',18), bg="black", fg="white")
        lbl_menu.pack()
        lbl_info = tk.Label(root, text="Click (+) para adcionar", font=('Helvatical bold',12), bg="black", fg="white")
        lbl_info.pack()

        #MENU OPTIONS
        OPTIONS = [""] 
        self.options = OPTIONS   

        #MENU NAMETYPE
        NAMETYPE = {}
        self.nametype = NAMETYPE

        #DROPDOWN MENU OPTIONS
        option_value = tk.StringVar(root)
        self.option_value = option_value
        option_value.set(OPTIONS[0])
        self.selection = OPTIONS[0]
       
        #ICONS
        img_add = tk.PhotoImage(file="./img/add.gif")
        self.img_all = {"Temperatura": tk.PhotoImage(file="./img/temperatura.gif"),
                    "Umidade": tk.PhotoImage(file="./img/umidade.gif"), 
                    "Velocidade": tk.PhotoImage(file="./img/velocidade.gif")}

        #SELECTOR MENU
        frm_add_menu = tk.Frame(root, pady=20, bg="black") # ADD MENU - FRAME START

        lbl_nome = tk.Label(frm_add_menu, text="nome: ", font=('Helvatical bold',12), bg="black", fg="white")
        lbl_nome.pack(side=tk.LEFT, fill=tk.BOTH)
       
        opt_sensor_name = tk.OptionMenu(frm_add_menu, option_value, *OPTIONS, command=self.get_option)
        opt_sensor_name.config(bg="black")
        opt_sensor_name.pack(side=tk.LEFT, fill=tk.BOTH)
        self.opt_sensor_name = opt_sensor_name

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

    def get_receiver(self, receiver):
        self.mainInfoReceiver = receiver

    def start_root(self):
        self.root.mainloop()

    def get_option(self, value):
        self.option_value.set(value)
        self.selection = value
        # self.btn_add_sensor["state"] = "normal"

    def update_option_menu(self):
        menu = self.opt_sensor_name["menu"]
        deleteClone = set(self.options)
        self.options = list(deleteClone)
        if self.options[0] == "":
            self.options.pop(0)  
        menu.delete(0, "end")
        
        for options in self.options:
            menu.add_command(label=options, 
                             command=lambda value=options: self.get_option(value))

    def create_monitor(self):
        if self.selection == "":
            return
            
        frm_generic = tk.Frame(self.frm_sensors, bg="black") # FRAME MONITOR - START

        name = self.selection.split(sep=" - ")

        lbl_sensor_name = tk.Label(frm_generic, text="{}".format(name[0]), font=('Helvatical bold',20), bg="black", fg="white")
        lbl_sensor_name.pack(pady=8)

        cvs = tk.Canvas(frm_generic, width = 100, height = 100, bg="black", bd=0, highlightthickness=0)  
        cvs.create_image(50, 50, image=self.img_all[self.nametype[self.selection]])
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

        infoReceiverThread = threading.Thread(target=self.build_info_receiver, args=("main_x", self.selection, lbl_value, lbox_value_list), daemon=True)
        infoReceiverThread.start()

        # #DISABLE ITEM OPTION AND BUTTON
        # self.opt_sensor_name['menu'].entryconfigure(self.selection, state = "disabled") 
        # self.btn_add_sensor["state"] = "disabled"

    def build_info_receiver(self, exchange, routing_key, sensor_value, msg_box):
        receiver = InfoReceiver(exchange, routing_key, sensor_value, msg_box)

    def get_metric(self):
        if self.selection == "Umidade":
            return "%"
        elif self.selection == "Velocidade":
            return "m/s"
        return "ºC"