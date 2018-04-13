# Работа на лекции
# # #Пельмени тесто 200 гр, фарш 200 гр, лук 10грЮ специи 10гр
# # #Грибной суп бульон 200мл, грибы 50гр, картошка 50гр,лук 10гр,
# # #хворост яёца 2шт, сахар 50гр, мука 125гр, соль 5гр

# cook_book = {
#   'Пельмени': [
#   {'ingridient_name': 'тесто', 'quantity': 200, 'measure': 'гр'},
#   {'ingridient_name': 'фарш', 'quantity': 200, 'measure': 'гр'},
#   {'ingridient_name': 'лук', 'quantity': 10, 'measure': 'гр'},
#   {'ingridient_name': 'специи', 'quantity': 10, 'measure': 'гр'}
#   ],
#   'Грибной суп': [
#   {'ingridient_name': 'бульон', 'quantity': 200, 'measure': 'мл'},
#   {'ingridient_name': 'грибы', 'quantity': 50, 'measure': 'гр'},
#   {'ingridient_name': 'картошка', 'quantity': 50, 'measure': 'гр'},
#   {'ingridient_name': 'лук', 'quantity': 10, 'measure': 'гр'},
#   {'ingridient_name': 'соль', 'quantity': 5, 'measure': 'гр'}
#   ],
#   'Хворост': [
#   {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт'},
#   {'ingridient_name': 'сахар', 'quantity': 200, 'measure': 'гр'},
#   {'ingridient_name': 'мука', 'quantity': 200, 'measure': 'гр'},
#   {'ingridient_name': 'соль', 'quantity': 200, 'measure': 'гр'}
#   ]
# }
  



# person_count = 3
# dishes = ['Пельмени', 'Грибной суп', 'Хворост']

# shop_list = {}

# for dish in dishes:
#   for ingridient in cook_book[dish]:   #dict[key]=value 
#       new_shop_list_item = dict(ingridient)
#       new_shop_list_item['quantity'] *= person_count
#       #shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item 
#       if new_shop_list_item['ingridient_name'] not in shop_list:
#         shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
#       else:
#         shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']   
 
# # print(shop_list ) для проверки , правильно ли написано


# #для примера и пояснения Тебе Женя! Прочти внимательней
# # for key, value in shop_list.items():   #.keys(): метод этирируется исключительно по ключам словаря/ 
# #   print(key, value)                          #.values():/по значениям /.items одновременно и по ключам и по значениям 


# for new_shop_list_item in shop_list.values():
#   print('{} {} {}'.format(new_shop_list_item['ingridient_name'], new_shop_list_item['quantity'], new_shop_list_item['measure']))

# # либо пишем как большие дяди с  аргами args* и кварги kwargs** Арги всё сворачивается в tuple Кортежи, Кварги сворачивает в Словарь   
# # for new_shop_list_item in shop_list.values():
# #     print('{ingridient_name} {quantity} {measure}'.format(**new_shop_list_item))  


# # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Задачу решили теперь делаем декомпозицию кода , применим функции. Выделим блоки кода который отвечают за одну задачу и обернем в функцию 

# def get_shop_list_by_dishes(person_count, dishes): # Функция Получить список покупок из блюд Аргументы(к-во людей и dishes)
#   shop_list = {} #Словарь этот помещаем внутрь функции
#   for dish in dishes:
#     for ingridient in cook_book[dish]:   #dict[key]=value 
#         new_shop_list_item = dict(ingridient)
#         new_shop_list_item['quantity'] *= person_count
#         #shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item 
#         if new_shop_list_item['ingridient_name'] not in shop_list:
#           shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
#         else:
#           shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']  
#   return shop_list #Возвращает данная функция заполненный shop_list      Запоминает результат который функция Нам возвращает, чтобы потом работать с Ним
  
# def print_shop_list(shop_list):
#   for new_shop_list_item in shop_list.values():
#     print('{} {} {}'.format(new_shop_list_item['ingridient_name'], new_shop_list_item['quantity'], new_shop_list_item['measure']))


# #Вопрос почему в первой функцииdef get_shop_list_by_dishes(person_count, dishes) return нужен а во второйdef print_shop_list(shop_list): нет?
# # return shop_list Мы ещё будем работать далее и Она Нам нужна
# # А вторая функция нужна только для того чтобы показать Нам , дальше работать Мы с Ней не будем. Поэтому return не нужен.

# Теперь у Нас в глобальном контексте осталось ТРИ глобальных переменных cook_book person_count dishes По возможности глобальные переменные лучше избегать
# cook_book - не трогаем это типа база данных и в жизни на практике , так информацию в коде никто не хранит. Скорее всего это будет какой-то
#  файл для данных. Либо такую инфу будем получать через какую-нибудь API

# Остальные две переменне Мы завернём в функцию, делаем третью Резульативищую  функцию  main
# def main():          #создаём функцию Функция точка входа в программу. Обьявляем в Ней две глобальные переменные
#   person_count = 3  #
#   dishes = ['Пельмени', 'Грибной суп', 'Хворост']
#   shop_list = get_shop_list_by_dishes(person_count, dishes)
#   print_shop_list(shop_list)

# main()     


# Итак как должно выглядеть идеальныое решение данной задачи в формате кода

cook_book = {
  'пельмени': [
  {'ingridient_name': 'тесто', 'quantity': 200, 'measure': 'гр'},
  {'ingridient_name': 'фарш', 'quantity': 200, 'measure': 'гр'},
  {'ingridient_name': 'лук', 'quantity': 10, 'measure': 'гр'},
  {'ingridient_name': 'специи', 'quantity': 10, 'measure': 'гр'}
  ],
  'грибной суп': [
  {'ingridient_name': 'бульон', 'quantity': 200, 'measure': 'мл'},
  {'ingridient_name': 'грибы', 'quantity': 50, 'measure': 'гр'},
  {'ingridient_name': 'картошка', 'quantity': 50, 'measure': 'гр'},
  {'ingridient_name': 'лук', 'quantity': 10, 'measure': 'гр'},
  {'ingridient_name': 'соль', 'quantity': 5, 'measure': 'гр'}
  ],
  'хворост': [
  {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт'},
  {'ingridient_name': 'сахар', 'quantity': 200, 'measure': 'гр'},
  {'ingridient_name': 'мука', 'quantity': 200, 'measure': 'гр'},
  {'ingridient_name': 'соль', 'quantity': 200, 'measure': 'гр'}
  ]
}
  

def get_shop_list_by_dishes(person_count, dishes): # Функция Получить список покупок из блюд Аргументы(к-во людей и dishes)
  shop_list = {} #Словарь этот помещаем внутрь функции
  for dish in dishes:
    for ingridient in cook_book[dish]:   #dict[key]=value 
        new_shop_list_item = dict(ingridient)
        new_shop_list_item['quantity'] *= person_count
        #shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item 
        if new_shop_list_item['ingridient_name'] not in shop_list:
          shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
        else:
          shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']  
  return shop_list #Возвращает данная функция заполненный shop_list      Запоминает результат который функция Нам возвращает, чтобы потом работать с Ним
  
def print_shop_list(shop_list):
  for new_shop_list_item in shop_list.values():
    print('{} {} {}'.format(new_shop_list_item['ingridient_name'], new_shop_list_item['quantity'], new_shop_list_item['measure']))


def main():          #создаём функцию Функция точка входа в программу. Обьявляем в Ней две глобальные переменные
  person_count = int(input('Ввести кол-во человек: '))  #Для удобства пользователя совершеним код. команда input. Вводим кол-во персон
  dishes = input('Введите блюдо в расчёте на одного человека через запятую: ').lower().split(',')  #split это метод строк , который прменяется к строке и по разделителю, разбивает эту строку по элементам и эти элименты помещает в словарь      #Для того чтобы записать каждое блюдо на человека ,используем метод split
  shop_list = get_shop_list_by_dishes(person_count, dishes)                    #Так же применяем метод lower который все вводимые буквы будет делать маленькими. Противоположенный ему метод upper     
  print_shop_list(shop_list)

main()        





///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////



# ДОМАШНЕЕ ЗАДАНИЕ








# Имеется группа студентов, у каждого из которых есть следующие характеристики: имя, фамилия, пол, предыдущий опыт в программировании (бинарная переменная), 5 оцененных по 10-бальной шкале домашних работ, оценка за экзамен по 10-балльной шкале. Необходимо написать программу, которая в зависимости от запроса пользователя будет выводить:

# среднюю оценку за домашние задания и за экзамен по всем группе в следующем виде:
#         Средняя оценка за домашние задания по группе: X
#         Средняя оценка за экзамен: Y
# где X и Y - вычисляемые значения;
# среднеюю оценку за домашние задания и за экзамен по группе в разрезе: а)пола б)наличия опыта в виде:
#         Средняя оценка за домашние задания у мужчин: A
#         Средняя оценка за экзамен у мужчин: B
#         Средняя оценка за домашние задания у женщин: C
#         Средняя оценка за экзамен у женщин: D
        
#         Средняя оценка за домашние задания у студентов с опытом: E
#         Средняя оценка за экзамен у студентов с опытом: F        
#         Средняя оценка за домашние задания у студентов без опыта: G
#         Средняя оценка за экзамен у студентов без опыта: H
# где A, B, C, D, E, F, G, H - вычисляемые значения;
# определять лучшего студента, у которого будет максимальный балл по формуле 0.6 * его средняя оценка за домашние задания + 0.4 * оценка за экзамен в виде:
# Лучший студент: S с интегральной оценкой Z
# если студент один или:
# Лучшие студенты: S... с интегральной оценкой Z
# если студентов несколько, где S - имя/имена студентов, Z - вычисляемое значение.
# Студентов должно быть не менее 6. 
# Код должен быть грамотно декомпозирован (максимально используйте функции).

group_of_students = [
  {"firs_name": "Полина", "last_name": "Чапаева", "gender": "female", "experience": True, "homework": [8, 6, 8, 10, 9], "exam": 10},
  {"firs_name": "Дарт", "last_name": "Вейдер", "gender": "male", "experience": False, "homework": [3, 5, 8, 10, 10], "exam": 8},
  {"firs_name": "Принцесса", "last_name": "Лея", "gender": "female", "experience": True, "homework": [6, 8, 10, 10, 8], "exam": 9},
  {"firs_name": "Робин", "last_name": "Гуд", "gender": "male", "experience": True, "homework": [9, 8, 10, 10, 9], "exam": 9},
  {"firs_name": "Люк", "last_name": "Скайвокер", "gender": "male", "experience": True, "homework": [10, 10, 10, 10, 10], "exam": 10},
  {"firs_name": "Брюс", "last_name": "Уилис", "gender": "male", "experience": False, "homework": [10, 10, 10, 10, 10], "exam": 10}
]

# get_my_average = lambda *my_average: sum(my_average)//len(my_average)
def print_average_grade_homework():
  average_grade_homework = 0
  for student in group_of_students:
    average_grade_homework += sum(student["homework"])/len(student["homework"])
  print('Средняя оценка за домашние задания в группе: {:03.1f}'.format(average_grade_homework/len(group_of_students)))
  
def print_average_grade_exam():
  average_grade_exam = 0
  for student in group_of_students:
    average_grade_exam += student["exam"]
  print('Средняя оценка за экзамен в группе: {:03.1f}'.format(average_grade_exam/len(group_of_students)))
  
def print_average_gender(gender):
  average_grade_homework_male = 0
  average_grade_exam_male = 0
  male_count = 0
  average_grade_homework_female = 0
  average_grade_exam_female = 0
  female_count = 0
  for student in group_of_students:
    if student["gender"] == "male":
      average_grade_homework_male += sum(student["homework"])/len(student["homework"])
      average_grade_exam_male += student["exam"]
      male_count += 1
    else:
      average_grade_homework_female += sum(student["homework"])/len(student["homework"])
      female_count += 1
      average_grade_exam_female += student["exam"]
  if (gender == 'a'):
    print('Средняя оценка за домашние задания у мужчин в группе: {:03.1f}'.format(average_grade_homework_male/male_count))
  elif (gender == 'b'):
    print('Средняя оценка за экзамен у мужчин в группе: {:03.1f}'.format(average_grade_exam_male/male_count))
  elif (gender == 'c'):
    print('Средняя оценка за домашние задания у женщин в группе: {:03.1f}'.format(average_grade_homework_female/female_count))
  elif (gender == 'd'):
    print('Средняя оценка за экзамен у женщин в группе: {:03.1f}'.format(average_grade_exam_female/female_count))
  else:
    print('Такая операция еще не поддерживается, но возможно', gender, 'уже находится в разработке')
  
def print_average_grade_exp(exp):
  average_grade_homework_true = 0
  average_grade_exam_true = 0
  true_count = 0
  average_grade_homework_false = 0
  average_grade_exam_false = 0
  false_count = 0
  for student in group_of_students:
    if student["previous_programming_experience"] == True:
      average_grade_homework_true += sum(student["homework"])/len(student["homework"])
      average_grade_exam_true += student["exam"]
      true_count += 1
    else:
      average_grade_homework_false += sum(student["homework"])/len(student["homework"])
      average_grade_exam_false += student["exam"]
      false_count += 1
  if (exp == 'e'):
    print('Средняя оценка за домашние задания с опытом программирования в группе: {:03.1f}'.format(average_grade_homework_true/true_count))
  elif (exp == 'f'):
    print('Средняя оценка за экзамен с опытом программирования в группе: {:03.1f}'.format(average_grade_exam_true/true_count))
  elif (exp == 'g'):
    print('Средняя оценка за домашние задания без опыта программирования в группе: {:03.1f}'.format(average_grade_homework_false/false_count))
  elif (exp == 'h'):
    print('Средняя оценка за экзамен без опыта программирования в группе: {:03.1f}'.format(average_grade_exam_false/false_count))
  else:
    print('Такая операция еще не поддерживается, но возможно', exp, 'уже находится в разработке')
  
def print_best_student():
  average_best_value = 0
  list_best_student = []
  for student in group_of_students:
    student['best'] = False
    student['best-value'] = int(round(((sum(student["homework"])/len(student["homework"]) * 0.6 + student["exam"] * 0.4)), 2))
    if average_best_value < student['best-value']:
      average_best_value = student['best-value']
  number_best_students = 0
  for student in group_of_students:
    if student['best-value'] == average_best_value:
      student['best'] = True
      number_best_students += 1
      list_best_student.append(student["last_name"])
    else:
      student['best'] = False
  if number_best_students == 1:
    print('Лучший студент:', list_best_student, 'с интегральной оценкой', average_best_value)
  else:
    print('Лучшие студенты:', list_best_student, 'с интегральной оценкой', average_best_value)
  
def main():
  print('Выберите одну из следущих команд:')
  print('x – Средняя оценка за домашние задания по группе')
  print('y – Средняя оценка за экзамен')
  print('a – Средняя оценка за домашние задания у мужчин')
  print('b – Средняя оценка за экзамен у мужчин')
  print('c – Средняя оценка за домашние задания у женщин')
  print('d – Средняя оценка за экзамен у женщин')
  print('e – Средняя оценка за домашние задания у студентов с опытом')
  print('f – Средняя оценка за экзамен у студентов с опытом')
  print('g – Средняя оценка за домашние задания у студентов без опыта')
  print('h – Средняя оценка за экзамен у студентов без опыта')
  print('s – Определить лучшего студента (или лучших студентов) с интегральной оценкой по формуле')
  print('q - если хотите завершить программу')
  user_choice = input()
  if user_choice == 'q':
    print('Программа завершена')
  elif user_choice == 'x':
    print_average_grade_homework()
  elif user_choice == 'y':
    print_average_grade_exam()
  elif user_choice == 'a':
    print_average_gender('a')
  elif user_choice == 'b':
    print_average_gender('b')
  elif user_choice == 'c':
    print_average_gender('c')
  elif user_choice == 'd':
    print_average_gender('d')
  elif user_choice == 'e':
    print_average_grade_exp('e')
  elif user_choice == 'f':
    print_average_grade_exp('f')
  elif user_choice == 'g':
    print_average_grade_exp('g')
  elif user_choice == 'h':
    print_average_grade_exp('h')
  elif user_choice == 's':
    print_best_student()
  else:
    print('Такая операция еще не поддерживается, но возможно', user_choice, 'уже находится в разработке')

main() 
  
# #КОМЕНТАРИЙ ОТ ПРЕПОДОВАТЕЛЯ!!!!
# Спасибо за работу, в целом все хорошо, зачет, но все же пару замечаний:

# в данной версии кода у вас программа падает на функциях, которые считают статистики по студентам с опытом/без (забыли поменять/перепутали ключ);
# функции print_average_gender(gender) и print_average_grade_exp(exp) можно еще сократить вдвое. Вы инициируете отдельные переменные для срезов: average_grade_homework_male = 0 average_grade_exam_male = 0 male_count = 0 average_grade_homework_female = 0 average_grade_exam_female = 0 female_count = 0
# и делаете одинаковые расчеты в условной конструкции по критерию. Но вы можете инициировать общие переменные:

# average_grade_homework = 0 average_grade_exam = 0 count = 0

# и все расчеты прописать только один раз. При этом в условии у вас будет: if student["gender"] == gender (то есть аргумент функции будет использоваться в качестве критерия, а функцию вы потом будете вызывать с разными критериями).

# В остальном все ок.  






Домашнее задание к лекции 2.1 «Открытие и чтение файла, запись в файл»
Задача №1
Воспроизведите код с лекции 1.5 и дополните его следующим образом:

Список рецептов должен храниться в отдельном файле в следующем формате:
Название блюда
Kоличество ингредиентов
Название ингредиента | Количество | Единица измерения
Пример:
Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт
В одном файле может быть произвольное количество блюд.
Читать список рецептов из этого файла.
Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных.
Код выглядел следующим образом:

cook_book = {
  'яйчница': [
    {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
    ],
  'стейк': [
    {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
    {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
    ],
  'салат': [
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
    {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
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
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=
          new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()
    
Задача №2
Напишите, для чего используются типы данных: json, xml, yaml.