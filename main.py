# текстовые , бинарные

# чтение r
# запись w
# дозапись a

# чтение rb
# запись wb

# open(путь до файлов, режим_работы,кодировка='utf-8') - открывет файл на указанный режим
# путь до файла
#абсолютный
#относительный


file = open("byron.txt",mode = "r",encoding="utf-8")
# .read () - считывает весь текст из файла
# .readlines() - считает каждую строку сформировав список
# .readline() - считает каждую строку по очереди

#text = file.read()
#text = file.readline()
#print(text)
file.close()

#запись данных в файл

#file2 = open('new_file.txt', mode='w', encoding='utf-8')
# .write()- записывает текст в одну строку
# .writelines(список строк) - принимает список строку и записывает в файл

#file2.write('Hello world\n')
#file2.write('Привет мир')

#ines = [f'{i} строка\n' for i in range (1,101)]
#file2.writelines(lines)

#file2.close()


# Работа с бинарными файлами

#img= open('nature.jpg', mode='rb')
#content = img.read()
#print(content)
#img.close()

# with - контекстный менеджер , позволяюзий не закрывать соединение

#with open('nature.jpg', mode ='rb') as img:
#    content = img.read()
#    for i in range (1,11):
#        new_img=open(f'{i}.jpg', mode='wb')
#        new_img.write(content)
#        new_img.close()
#   print(img.closed)


file2 = open('new_file.txt', mode='a', encoding='utf-8')

lines = [f'{i} строка\n' for i in range (1, 101)]
file2.writelines(lines)

file2.close()