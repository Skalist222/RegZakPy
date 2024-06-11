class const:
    # Основное меню
    createRequest = "Создать заявку" # текст на кнопе

    # Форма "Требуемые позиции"
    PackedPVDWithLogo           = "Пакет ПВД с логотипом"
    PaperAndKraftPackedWithLogo = "Бумажные и крафт пакет с логотипом"
    PaperPoligraf               = "Бумажная полиграфия"
    SouvenirProduction          = "Сувенирная продукция"
    WantMorePosition            = "Хочу выбрать несколько позиций"
    # данные Кнопок
    PackedPVDWithLogoBTN            = "PACKEDLOGO"
    PaperAndKraftPackedWithLogoBTN  = "PAPERKRAFT"
    PaperPoligrafBTN                = "POLIGRAF"
    SouvenirProductionBTN           = "SOUVENIR"
    WantMorePositionBTN             = "MOREPOSITION"
    #ключи для получения нужного параметра основываясь на данные полученные с кнопки
    dictBut_TextPositions = {
        PackedPVDWithLogoBTN:PackedPVDWithLogo,
        PaperAndKraftPackedWithLogoBTN:PaperAndKraftPackedWithLogo,
        PaperPoligrafBTN:PaperPoligraf,
        SouvenirProductionBTN:SouvenirProduction,
        WantMorePositionBTN:WantMorePosition
                    }

    #Форма выбора лица
    UriFace = "Юридическое лицо" #//=) да юр лицо... я знаю что это не правильно
    FizFace = "Частное лицо"
    #данные Кнопок
    UriFaceBTN = "UriFace"
    FizFaceBTN = "FizFace"
    #ключи для получения нужного параметра основываясь на данные полученные с кнопки
    dictBut_TextFaces = {
        UriFaceBTN:UriFace,
        FizFaceBTN:FizFace
                    }    
