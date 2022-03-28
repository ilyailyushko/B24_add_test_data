
import func
import random

# создем на портале рандомные контакты
for i in range(50):
     func.add_random_contact()


# получаем список ID всех контактов на портале
contacts_id = func.get_contacts()


# Получаем список стадий сделок
crm_stage_list = func.crm_deal_stage_list()
print(crm_stage_list)


# Для каждого контакта создаем от 1 до 4 сделок в рандомной стадии.
for i in contacts_id:
    
    d_amount = random.randint(1, 4)

    for d in range(d_amount):
        stage = random.choice(crm_stage_list)
        title = random.choice(['Покупка товара', 'Покупка услуги', 'Покупка товара и услуги', 'Доп. услуги'])
        func.add_deal(title, i, stage, random.randint(1000, 15000))

