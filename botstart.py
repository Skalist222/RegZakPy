import asyncio
import telegram
import requests


from itertools import count



# мои модули
from userIn import UserIn
from amoCrmApi import Amo

import logging
from html import escape
from uuid import uuid4

from cnst import const
from pprint import pprint

from telegram import ReplyKeyboardMarkup,KeyboardButton, InlineQueryResultArticle, InputTextMessageContent,InlineKeyboardButton, InlineKeyboardMarkup,ForceReply, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CallbackQueryHandler,CommandHandler, ContextTypes, MessageHandler, InlineQueryHandler,filters

listUsers:list[UserIn] = []
application = Application.builder().token("7467329508:AAFH8AbYFiEz0tY2PMaW2c7Mir18mHlH-qY").build()
amoCrm:Amo = Amo()





PositionsMenu = [
        [
            InlineKeyboardButton(const.PackedPVDWithLogo, callback_data=const.PackedPVDWithLogoBTN),
            InlineKeyboardButton(const.PaperAndKraftPackedWithLogo, callback_data=const.PaperAndKraftPackedWithLogoBTN),
        ],
        [
            InlineKeyboardButton(const.PaperPoligraf, callback_data=const.PaperPoligrafBTN),
            InlineKeyboardButton(const.SouvenirProduction, callback_data=const.SouvenirProductionBTN),
        ],
        [
            InlineKeyboardButton(const.WantMorePosition, callback_data=const.WantMorePositionBTN),
        ],
    ]
FaceMenu = [
        [
            InlineKeyboardButton(const.FizFace, callback_data=const.FizFaceBTN),
            InlineKeyboardButton(const.UriFace, callback_data=const.UriFaceBTN),
        ],
    ]
async def SendInlineMenu(update:Update,keyboard,textMessage:str)->None:
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(textMessage, reply_markup=reply_markup)


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    userTg = update.message.from_user
    selected = False
    for us in listUsers:
        if us.defUser.id == userTg.id:
            selected = True
            break
    if selected == False:
        listUsers.append(UserIn(userTg))
        startMenu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=const.createRequest)],])
        await update.message.reply_text("Здравствуйте",reply_markup=startMenu)

async def responce(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        text = update.message.text
        userTg = update.message.from_user
        selected = False
        userMy:UserIn = None
        for us in listUsers:
            if us.defUser.id == userTg.id:
                selected = True
                userMy = us
                break
        if selected == False:
            listUsers.append(UserIn(userTg))
            for us in listUsers:
                if us.defUser.id == userTg.id:
                    userMy = us
                    break
        if text == "custComp":
            await update.effective_message.reply_text(amoCrm.GetCustComp())
            
        if text == const.createRequest:# П
            await SendMessageSetVariants(update,userMy)
        
        if userMy.ptintsMorePosition == True:#когда бот ожидает от пользователя Описание нужных параметров
            userMy.morePos = text
            await SendMessageGetName(update,userMy)
        elif userMy.printsUserName == True:#когда бот ожидает от пользователя Имя 
            userMy.setAllFalse()
            userMy.name = text
            await SendMessageGetPhone(update,userMy)   
        elif userMy.printsPhone == True:#когда бот ожидает от пользователя номер телефона
            userMy.setAllFalse()
            userMy.phone = text
            await SendMessageFace(update,userMy)
        elif userMy.printsTir == True:#когда бот ожидает от пользователя тираж
            userMy.setAllFalse()
            userMy.tir = text
            await SendMessageGetName(update,userMy)  
        elif userMy.printsINN == True:
            userMy.setAllFalse()
            userMy.INN = text
            await SendMessageThanks(update,userMy)

async def SendMessageSetVariants(update,userMy:UserIn):
        await SendInlineMenu(update,PositionsMenu,"Выберите требуемые позиции")

async def SendMessageGetName(update,userMy:UserIn):
        userMy.setAllFalse()
        userMy.printsUserName = True # переходим в ожидание имени
        await update.message.reply_text("Введите ваше имя")

async def SendMessageGetPhone(update,userMy:UserIn):
        userMy.setAllFalse()
        userMy.printsPhone = True # переходим в ожидание Телефона
        await update.message.reply_text("Введите номер телефона")

async def SendMessageFace(update,userMy:UserIn):
        userMy.setAllFalse()
        await SendInlineMenu(update,FaceMenu,"Вы пишете от имени:") #отправляем две кнопки(юр лицо, физ лицо)


async def SendMessageTir(update:Update,userMy:UserIn):
        userMy.setAllFalse()
        userMy.printsTir = True # переходим в ожидание тиража
        await update.effective_message.reply_text("Укажите желаемый тираж")

async def SendMessageINN(update:Update,userMy:UserIn):
        userMy.setAllFalse()
        userMy.printsINN = True # переходим в ожидание тиража
        await update.effective_message.reply_text("Введите ваш ИНН")

async def SaveInformation(userMy:UserIn):
        amoCrm.postLead(userMy)

async def SendMessageThanks(update:Update,userMy:UserIn):
        userMy.setAllFalse()
        print(userMy.toString())
        await SaveInformation(userMy)
        await update.effective_message.reply_text("Спасибо за заявку, в ближайшее время ")


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    userTg = update.callback_query.from_user
    userMy = None

    for userInList in listUsers:
        if userTg.id == userInList.defUser.id:
            userMy = userInList
    if userMy == None:
        listUsers.append(UserIn(userTg))
        for userInList in listUsers:
            if userTg.id == userInList.defUser.id:
                userMy = userInList
    
    text = update.callback_query.data
    if text in const.dictBut_TextPositions.keys():
        print("Выбрана одна из кнопок позиций:"+const.dictBut_TextPositions[text])
        userMy.selectPos = const.dictBut_TextPositions[text]
        print(userMy)
        if(text == const.WantMorePositionBTN):
            userMy.setAllFalse()
            userMy.ptintsMorePosition = True
            await update.effective_message.reply_text("Опишите заказ, который Вам требуется(позиции, тираж, сроки)")
        else:
            await SendMessageTir(update,userMy)         
            #await application.bot.send_message(userTg.id,"Введите пожалуйста что-то там типа")
    if text in const.dictBut_TextFaces.keys():
        if text == const.FizFaceBTN:
            await SendMessageThanks(update,userMy)
        elif text == const.UriFaceBTN:
            await SendMessageINN(update,userMy)



    



def main() -> None:
    application.add_handler(CommandHandler("start", start))#команда старт
    application.add_handler(MessageHandler(filters.ALL, responce))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    

if __name__ == "__main__":
    main()
