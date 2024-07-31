def parse_recipes(file_path):
  cook_book = {}

  with open(file_path, 'r', encoding='utf-8') as file:
      lines = file.readlines()

      i = 0
      while i < len(lines):
          dish_name = lines[i].strip()
          if not dish_name:  # Пропускаем пустые строки
              i += 1
              continue

          i += 1

          # Проверка, что следующая строка содержит число
          if i < len(lines):
              try:
                  quantity = int(lines[i].strip())
              except ValueError:
                  print(f"Ошибка: Ожидалось число, но получено '{lines[i].strip()}' вместо количества ингредиентов для '{dish_name}'.")
                  break

          i += 1

          ingredients = []
          for _ in range(quantity):
              if i < len(lines):
                  ingredient_info = lines[i].strip().split(' | ')
                  if len(ingredient_info) != 3:
                      print(f"Ошибка: Неверный формат ингредиента '{lines[i].strip()}'.")
                      break
                  ingredient_name = ingredient_info[0]
                  ingredient_quantity = int(ingredient_info[1])
                  ingredient_measure = ingredient_info[2]
                  ingredients.append({
                      'ingredient_name': ingredient_name,
                      'quantity': ingredient_quantity,
                      'measure': ingredient_measure
                  })
                  i += 1

          cook_book[dish_name] = ingredients

  return cook_book

# Укажите путь к вашему файлу
file_path = 'recipes.txt'
cook_book = parse_recipes(file_path)






def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingredient in cook_book[dish]:
      if ingredient['ingredient_name'] not in shop_list:
        shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': 0}
      shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
  return shop_list
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
