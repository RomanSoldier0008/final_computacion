class Menu:
    def __init__(self):
        self.__OpcMenu = ""

    def setOpcMenu(self, opc):
        self.__OpcMenu = opc

    def GetOpcMenu(self):
        return self.__OpcMenu

    def show(self):
        while True:
            self.SetOpcMenu(str(input(MAIN_MENU_INPUT)))
            if self.GetOpcMenu() == "1":
                # ACA VA EL LLAMADO DE METODOS
            elif self.GetOpcMenu() == "2":
                break

menu = Menu()
menu.show()