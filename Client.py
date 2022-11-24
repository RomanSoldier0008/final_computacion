from constants import *
class Client:
    lastId = 0
    def __init__(self, name, last_name, automotive):
        self.clients = []
        self.__id = self.lastId
        self.__name = name
        self.__lastName = last_name
        self.__automotive = automotive
        self.lastId += 1

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_lastname(self):
        return self.__lastName

    def set_lastname(self, lastname):
        self.__lastName = lastname

    def get_automotive(self):
        return self.__automotive

    def set_automotive(self, automotive):
        self.__automotive = automotive

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id


    def generate_client(self):
        count = 0
        numbers_of_customer = int(input(NUMBER_OF_CUSTOMERS_INPUT))
        while count != numbers_of_customer:
            name = str(input(NAME_CLIENT_INPUT).strip().lower().capitalize())
            lastname = str(input(LASTNAME_CLIENT_INPUT).strip().lower().capitalize())
            self.set_id(len(self.clients) + 1)
            client = Client(name, lastname)
            self.clients.append(client)
            count += 1

    def remove_client(self):
        if len(self.clients) > 0:
            name_client = str(input(NAME_CLIENT_REMOVE.strip().lower().capitalize()))
            for i in range(0, len(self.clients)):
                if name_client in self.clients[i].get_name():
                    index = self.clients.index(name_client)
                    print(CLIENT_HAVE_BEEN_REMOVE.format(self.clients[index].get_name()))
                    self.clients.pop(index)
                else:
                    break
        else:
            print(ERROR_NO_CLIENTS)

    def print_cient(self):
        if len(self.clients) > 0:
            name_client = str(input(NAME_CLIENT_REMOVE.strip().lower().capitalize()))
            for i in range(0, len(self.clients)):
                if name_client in self.clients[i].get_name():
                    index = self.clients.index(name_client)
                    print(PRINT_CLIENT.format(self.clients[index].get_name(),
                                              self.clients[index].get_lastname()))
                else:
                    break
        else:
            print(ERROR_NO_CLIENTS)