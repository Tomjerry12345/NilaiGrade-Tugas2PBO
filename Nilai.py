class Nilai :
    __name = ""
    __nilai = 0
    def __init__(self , name , nilai):
        self.__name = name
        self.__nilai = nilai

    def tampilNama(self):
        __name = self.__name
        return __name

    def tampilNilai(self):
        __nilai = self.__nilai
        return __nilai

    def cariNilai(self):
        if (self.__nilai >= 80 and self.__nilai <= 100) :
            __grade = "A"
        elif (self.__nilai >= 65 and self.__nilai <= 79) :
            __grade = "B"
        elif (self.__nilai >= 55 and self.__nilai <= 64) :
            __grade = "C"
        elif (self.__nilai >= 45 and self.__nilai <= 54) :
            __grade = "D"
        else :
            __grade = "E"

        return __grade


