class Automotive:
    # brand es marca
    def __init__(self, id_automotive, brand, model, year, file):
        self.__id_automotive = id_automotive
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__file = file

    def get_id(self):
        return self.__id_automotive

    def set_id(self, id_automotive):
        self.__id_automotive = id_automotive

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model


    def generate_automotive(self):