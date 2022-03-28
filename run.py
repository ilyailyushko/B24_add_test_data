from fast_bitrix24 import Bitrix

# замените на ваш вебхук для доступа к Bitrix24
webhook = "https://b24-rfzucy.bitrix24.ru/rest/1/tk6h8ntighkqlp8d/"
b = Bitrix(webhook)


# список сделок в работе, включая пользовательские поля
deals = b.get_all(
    'crm.deal.list',
    params={
        'select': ['*', 'UF_*'],
        'filter': {'CLOSED': 'N'}
})

print(deals)