cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
 
 
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                  shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
        else:
          shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list
 
 
def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))
 
 
def get_cook_book_with_quantity(path):
    cook_book = {}
    with open(path, encoding='utf-8') as f:
        while True:
            name = f.readline().strip()
            if not name:
                break
            count = int(f.readline().strip())
            cook_book[name] = []
            line = f.readline().strip()
            while line:
                ingredients = line.split(" | ")
                ingredients_dict = {"ingredient_name": ingredients[0],
                                    "quantity": int(ingredients[1]),
                                    "measure": ingredients[2]}
                cook_book[name].append(ingredients_dict)
                line = f.readline().strip()
 
        return cook_book
 
 
def shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = int(input('Введите блюда через запятую на одного человека : ')) \
    .lower().split(', ')
    cook_book = get_cook_book_with_quantity("cook-book.txt")
    shop_list = get_shop_list_by_dishes(dishes, person_count)
   
print(shop_list)