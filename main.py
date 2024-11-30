import json #импорт json

with open('dump.json', 'r', encoding='utf-8') as file:
    data = json.load(file)#чтение данных из файла в формате JSON и преобразование их в объекты Python

#запрос для поиска
numb=input("Введите номер квалификации")

print("\n=============== Результат поиска ===============")
for item in data:
    if item['model'] == 'data.skill' and item['fields']['code'].startswith(numb):#startswith проверяет, начинается ли строка на указанную подстроку
        print(f"{item['fields']['code']} >> {item['fields']['title']}")
        found = True
#startswith(numb) проверка начинается ли строка на подстроку
if not found: #если после прохода цикла значение не верно
    print("============== Не найдено ===============")