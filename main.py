cook_book = {}
ingredients_list = []
from pprint import pprint
with open("res.txt", encoding="UTF-8") as f:
    a = 1
    for i in f:
        # print(a)
        if a == 1:
            dish_name = i.strip()
        if a == 2:
            ing_qty = int(i.strip())
            print(ing_qty)
            # print(ing_qty)
            b = 0
            while b != ing_qty:
                dc_1 = []
                print("hello")
                ing_qty -= 1
                ingredient_dict = {}
                item1, item2, item3 = f.readline().split("|")
                ingredient_dict["ingredient_name"] = item1.strip(' ')
                ingredient_dict['quantity'] = item2.strip('')
                ingredient_dict['measure'] = item3.strip(' \n')
                a = -1
                print(ingredient_dict)
                dc_1.append(ingredient_dict)
            ingredients_list.append(dc_1)
            cook_book[dish_name] = ingredients_list
            #подскажите пожалуйста почему смешываются ингредиенты



        a +=1


ingredients_list.append(ingredient_dict)
cook_book[dish_name] = ingredients_list
pprint(cook_book)
# print(dish_name)
# def get_shop_list_by_dishes(dishes, person_count):
#     params = {}
#     for i in cook_book:
#         if i == dishes:
#             ingrs = {}
#             print(cook_book)
#             for j in cook_book[i]:
#                 par = j
#                 par['quantity'] = int(par['quantity']) * person_count
#                 ingr = {par['ingredient_name']: {'measure': par['measure'], 'quantity': par['quantity']}}
#                 ingrs.update(ingr)
#     print(ingrs)
#     # print(ingr)
#
#
#
# get_shop_list_by_dishes("Омлет", 3)





