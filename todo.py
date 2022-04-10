
#1.1 Задайте переменную todo, в которую занесите список из семи дел
todo=['Finish work','Cook lunch','Walk a dog','Buy a jacket','Watch youtube video','Go shopping','Finish homework']


#1.2 Распечатайте первый, третий, четвертый, и последний элементы списка.

todo1=todo[0:3]
todo1.append(todo[-1])
print('The new todo list is:','\n'.join(todo1),sep='\n')

#1.3 Разбейте с помощью срезов список на две части - в первой части три элемента, во второй - четыре.

todo_part1=todo[0:3]
todo_part2=todo[4:8]
print(todo_part1)
print(todo_part2)

#1.4  Добавьте к списку дел еще одно или два (через append).
todo.append('Learn Python')
print(todo)

#1.5 Поменяйте местами первое и последнее дело в списке.

todo[-1], todo[-2] = todo[-2], todo[-1]
print(todo)

#1.6 Спросите пользователя про следующее дело и добавьте его в список.

new_task=input('Please, print here the next task in todo list:')
todo.append(new_task)
print(todo)

#1.7 Скопируйте список todo в четыре других списка, так, 
#    чтобы todo2 - был просто еще одним названием для списка todo (указателем на список), а todo3, todo4, todo5 - отдельными объектами. 
#    Создайте todo3, todo4, todo5 с помощью пустого среза, оператора list() и функции .copy(). 
#    С помощью оператора id() убедитесь в том, что все сделали правильно.

todo2=todo
todo3=todo[:]
todo4=list(todo)
todo5=todo.copy()

print('The id of todo is:' + str(id(todo)))
print('The id of todo2 is:' + str(id(todo2)))
print('The id of todo3 is:' + str(id(todo3)))
print('The id of todo4 is:' + str(id(todo4)))
print('The id of todo5 is:' + str(id(todo5)))




