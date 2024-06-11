from amocrm.v2 import tokens
from amocrm_api import AmoOAuthClient # for oauth
from datetime import datetime
import arrow
from userIn import UserIn

class Amo:
    subdomain:str = "valvor222" # Поддомен
    amo_domain:str = f"https://{subdomain}.amocrm.ru"
    #долгосрочный токен eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImQwZjFkNjFjZjIzMDE0MDIwMGFlNzM4ZmZiM2FmMzJmYTEzZTQ5YTJmMTY1MDgwNzBjMTUzZGExNWZhNDY5M2QwMTBhNzZlYjU3N2QxYjFmIn0.eyJhdWQiOiJkOGViYWZlMS0zNzM5LTRkOTItYTU0Ni1lMzNjNGVjZjM1MTMiLCJqdGkiOiJkMGYxZDYxY2YyMzAxNDAyMDBhZTczOGZmYjNhZjMyZmExM2U0OWEyZjE2NTA4MDcwYzE1M2RhMTVmYTQ2OTNkMDEwYTc2ZWI1NzdkMWIxZiIsImlhdCI6MTcxNzU4NjUzMSwibmJmIjoxNzE3NTg2NTMxLCJleHAiOjE4MTY5OTIwMDAsInN1YiI6IjExMTE4NTg2IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMxNzgyMzAyLCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJjcm0iLCJmaWxlcyIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiLCJwdXNoX25vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiNjgxYTgzYjktNGRlYi00MGM0LWExMDMtOGQ2ODczY2ZhMjg2In0.eCcd-E6gKrAAvpf3mTokGzIsl1Ez_WZj1PO2sSbpSM-IEirdTqpbzonWCg4C6apfDwAXIo0Ufi0AkDPCtp0OOkh0pvmGA_amZd2ZplS59iHzmrIihW68JGASEtwTOZxJgg2lX8ocOc_FtSv4Tb1c9WPts7CRyNptnAn_ViF9QOUSM3-lqItUg1GdZJ-lZcHLaLQjyXyMDeB3ErU5D5ySGm_zrHG-vME9kc80RJJlwYTmoqICay-_F2v-cwCi1RMYzFrjUqY0P4_304vy2dzI6JbRk3AF1gnkCF_zCEqooe9sBKLGpY8Rtdka37yGckGIRZznPAzn2kU6DPu-RULppg  
    client_id:str="d8ebafe1-3739-4d92-a546-e33c4ecf3513" # ID интеграции 
    client_secret:str="yFc03gZYu0flpYmPjW1mFNJdovZYbv4Oxa2dbUmDGUakMBOaFA6wLH5RYwiuPuBt" # Секретный ключ
    redirect_url:str="https://ya.ru" # URL, который указан в интеграции (в нашем примере https://app.jaycopilot.com/)
    refresh_token:str = "def50200fce3c80e20d5a82c36c66d8cb037f9b0afd11d65e24f2f6da5bc32bf18195035d303b42b1ab8749a727e81cde244098c1af65387d632fc94dc84c21da1974a5335cccea389d7d8b174184ac824c3f421727daf7b63988387f319e1357fa612b8ac230f3b28fd193c652d75b6d0206dcf4cbe7252d72185b2ca215e25abda1395c7f462c55fa258bbfd8684da8d21be65109280b6e55239c2ea14db3f52d4628640856769284d7ba02a7e8171c17bef624e4c0ee7f971ffdc31f1aa5a73f402a7b32076adc54a946acdfb1fac109e45ce4af861acb6e2455cd4feb47633852c31e07346a923fdf25a0e7808cba370488a90ebc6540c37de972b77855fe9a8bbba3c10c33621588eca7456c167604d7727629e7994bd4fd7f32adde70449385c55bf17554f6313890b353c96371208fc57efde9182e7d5757563261d451a94948450abf6cd1ee4e90394270852bb804ac7bd1cb4fca89e171228e8c987bbc581fe99775dc181e50092d4fae767460fb39c1f627808d68bc3a87f1d49aa91d83ff829730cc5b7f86702a4fd0ec5a5b77804564b6d1682d36afa30b408439e0f7fefb1aae3fba49462acb08221df8aff4444592ce57dc7fc2ba51c70b70335211648d7e1d62405f81c6288cf5c4d5e6ab6fbd0b13d847e6dcab2a1d4" # Длинный код авторизации (действительный 20 мин.)
    today:str = arrow.now().format('YYYY-MM-DD')
    state = {'cookies': None}
    client:AmoOAuthClient = None # клиент амосрм

    def __init__(self) -> None:
        self.startApiAMOCRM()

    

    def startApiAMOCRM(self) -> None:
        tokens.default_token_manager(
            client_id=self.client_id,
            client_secret=self.client_secret,
            subdomain=self.subdomain,
            redirect_url=self.redirect_url,
            storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
        )
        #генерация файлов ключей
        #tokens.default_token_manager.init(code=refresh_token, skip_error=False)

       
        self.client = AmoOAuthClient(tokens.default_token_manager.get_access_token(),self.refresh_token,f"https://{self.subdomain}.amocrm.ru",self.client_id,self.client_secret,self.redirect_url)
        dt = datetime.today().strftime("%a, %d %b %Y %H-%m-%d")
        date_time = f"{dt} UTC"

        # for Legacy client
        headers = {
            "IF-MODIFIED-SINCE": f"{date_time}",
            "Content-Type": "application/json"
        }
        self.client.update_session_params(headers)
        self.createCustomFields()
    #__________________________________________
    def createContact(self,Name:str,Number:str,CompanyInn:str=None)->str:
        newContact = [
        {
            "first_name": Name,
            "custom_fields_values": [
                {
                    "field_code": "PHONE",
                    "values": [
                        {
                            "value": Number
                        }
                    ]
                }
            ]
        },
        ]
        resAddContact = self.client.create_contacts(newContact)
        return str(resAddContact)
    #__________________________________________
    def postLead(self,user:UserIn):
        #329141-EMAIL in company
        if(user.INN != ""):# если человек указал INN то мы ищем компанию в амо и если не нашли то создаем новую
            selCompany = self.client.get_companies(limit=10, page=1,filters={'name': user.INN})
            print(selCompany)
            if(selCompany == {}):
                resultCreate = self.client.create_companies(#создаем компанию
                    [
                        {
                            "name": "От: "+user.name,
                            "custom_fields_values": 
                            [
                                {
                                    "field_id": 329141,
                                    "values": [{"value": user.INN}]
                                }
                            ]
                        }
                    ])
                idNewCompanie = str(resultCreate["_embedded"]["companies"][0]["id"])
    #__________________________________________
    def createCustomFields(self):
        companiesCF = self.client.get_companies_custom_fields()
        print("Кастомные поля компаний:\n",companiesCF)
        #PHONE-329139,Email-329141,ADDRESS-31782302
        if not self.findCF("INN",companiesCF):
            self.createCFCompany("ИНН","INN")

        contactsCF = self.client.get_contacts_custom_fields()
        print("Кастомные поля контактов:\n",contactsCF)
        #Должность-329137,PHONE-329139,EMAIL-329141,Пол.Согл-329233

        leadsCF = self.client.get_leads_custom_fields()
        print("Кастомные поля сделок:\n",leadsCF)
        #тут проверка на наличие всех нужных полей в сделках
    #__________________________________________
    def findCF(self,code,arr:dict):
       if any(field['code']==code for field in arr):
           return True
       else: 
           return False
    def createCFCompany(self,name,code):
        self.client.create_companies_custom_fields([{"name":name,"code":code,"type":"text","sort": 510}])
    def createCFContact(self,name,code):
        self.client.create_contacts_custom_fields([{"name":name,"code":code,"type":"text", "sort": 510}])
    #__________________________________________