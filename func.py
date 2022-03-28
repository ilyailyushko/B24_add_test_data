from fast_bitrix24 import Bitrix
import requests

# замените на ваш вебхук для доступа к Bitrix24
webhook = "https://b24-rfzucy.bitrix24.ru/rest/1/tk6h8ntighkqlp8d/"
b = Bitrix(webhook)



# создать сделку
def add_deal(TITLE, CONTACT_ID, STAGE_ID, OPPORTUNITY):
    if ':' in STAGE_ID:

        split_string = STAGE_ID.split(":", 1)
        substring = split_string[0]
        cat = substring.strip('C')

    else:

        cat = 0

    deal = b.call(
        'crm.deal.add',
        {
        'fields':
        { 
            "TITLE": TITLE, 
            "TYPE_ID": "GOODS", 
            "STAGE_ID": STAGE_ID, 					
            "COMPANY_ID": 3,
            "CONTACT_ID": CONTACT_ID,
            "OPENED": "Y", 
            "CURRENCY_ID": "RUB", 
            "OPPORTUNITY": OPPORTUNITY,
            "CATEGORY_ID": cat,
        },
        'params': { "REGISTER_SONET_EVENT": "Y" }	
    }
    )
    print(deal)


# создать контакт
def add_contact(NAME, SECOND_NAME,  PHONE):
    b.call('crm.contact.add',{
        'fields': {
            "NAME": NAME, 
            "LAST_NAME": SECOND_NAME, 
            "OPENED": "Y", 
            "ASSIGNED_BY_ID": 1, 
            "TYPE_ID": "CLIENT",
            "SOURCE_ID": "SELF",
            "PHONE": [ { "VALUE": f"{PHONE}", "VALUE_TYPE": "WORK" }] 
        }
    })

# удалить контакт
def kill_contact(ID):
    b.call('crm.contact.delete',{ 'id': ID})

# удалить сделку
def kill_deal(ID):
    b.call('crm.deal.delete',{ 'id': ID})


#  Получаем рандомные данные в randomdatatools, запихиваем их на портал
def add_random_contact():
    random_contact = requests.get('https://api.randomdatatools.ru')
    random_contact = random_contact.json()
    
    NAME = random_contact['FirstName']
    SECOND_NAME = random_contact['LastName']
    PHONE = random_contact['Phone']

    add_contact(NAME, SECOND_NAME, PHONE)

# Получаем список контактов на портале
def get_contacts():
    k = b.get_all(
        'crm.contact.list',
        params={
        'select': [ "ID"]})
    list_id = []
    for i in k:
        list_id.append(i['ID'])
    return list_id


# Получаем список сделок на портале
def get_deals():
    k = b.get_all(
        'crm.deal.list',
        params={
        'select': [ "ID"]})
    list_id = []
    for i in k:
        list_id.append(i['ID'])
    return list_id


# Получаем список стадий сделок на портале
def crm_deal_stage_list():
    DEAL_STAGE_LIST = []
    m = b.get_all('crm.status.list')
    for i in m:
        if  'DEAL_STAGE' in i['ENTITY_ID']:
            DEAL_STAGE_LIST.append(i['STATUS_ID'])
    return DEAL_STAGE_LIST
   

# Удаляем все контакты и сделки
def kill_all():
   deals = get_deals()
   contacts = get_contacts()
   for i in contacts:
       kill_contact(i)
   for i in deals:
       kill_deal(i)
