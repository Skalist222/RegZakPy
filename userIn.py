import telegram 

class UserIn:
    def __init__(self, user:telegram.User) -> None:
        self.defUser = user
    # 
    lastMessage:telegram.Message
    defUser:telegram.User 


    name:str=""       #Имя
    phone:str=""      #Телефон
    INN:str=""        #ИНН
    morePos:str=""    #введенные вручную: позиции, тираж, сроки
    selectPos:str=""  #выбранная позиция
    tir:str=""

    # ожидания ответов на определенные запросы 
    ptintsMorePosition:bool=False # Если человек нажал кнопку "Хочу больше позиций"
    printsProduсed:bool=False # Тираж
    printsUserName:bool=False # Имя 
    printsPhone:bool=False # Номер телефона
    printsINN:bool=False # ИНН
    printsTir:bool =False

    def toString(self)->str:
        retStr = f"Имя:{self.name}\nТелефон:{self.phone}\n"
        if(self.INN !=""): retStr +=f"ИНН Юр.:{self.INN}\n"
        if(self.morePos != ""): retStr +=f"Описание заказа:{self.morePos}\n"
        else:
            retStr+= f"Позиция:{self.selectPos}\nТираж:{self.tir}"
        return retStr
    
    def setAllFalse(self):
        self.ptintsMorePosition = False
        self.printsProduсed = False
        self.printsUserName = False
        self.printsPhone = False
        self.printsINN = False
        self.printsTir = False
    