# Требования к программной реализации:
# При запуске приложения из консоли пользователь должен получать строку ввода для команды. Ему должны быть доступны следующие команды:
# 1) load filename.txt — загрузить слова из файла filename.txt;
# 2) wordcount червяк — отобразить число раз, которое программа встретила слово «червяк» в загруженных файлах;
# 3) clear-memory — очистить все данные о прочитанных словах из памяти.

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))



class WordCounter():
    def __init__(self):
      self.counter = {}
      self.text = []
      self.progress = True

    def load_file(self, filename):
        with open(os.path.join(__location__, filename), encoding="utf-8") as text:
            self.text = text.read().lower().split(' ')

    def wordcount(self, search_word: str):
        __counter = 0
        for word in self.text:
            if search_word.lower() == word:
                __counter += 1
        
        self.counter[search_word] = __counter

    def clear_memory(self):
        self.counter = {}
        self.text = []

    def show_counter(self):
        for key, value in self.counter.items():
            print (key,':',value)
    
    
    def start(self):
        print('Список команд: load (загрузить файл), wordcount (посчитать слова), clear-memory (очистить память от слов), exit (Завершить)')
        try:
            while self.progress:
                _in = input()
                if _in == 'load':
                    print('Введите имя файла: filename.txt')
                    _file = input()
                    self.load_file(_file)
                    if(self.text):
                        print('можете сосчитать слова wordcount')
                    else:
                        print('файл некорректен')

                if _in == 'wordcount':
                    if self.text == ['']:
                        print('Сначала загрузите файл load')
                    else:
                        print('Введите слово файла: червяк')
                        _word = input()
                        self.wordcount(_word)
                        print('теперь введите show')

                if _in == 'clear-memory':
                    print('Счетчик сброшен')
                    self.load_file(input())

                if _in == 'show':
                    self.show_counter()

                if _in == 'exit':
                    print('Удачи')
                    self.progress = False

        except:
                print('Что то пошло не так, попробуйте снова')
        finally:
                print('Спасибо за то что воспользовались нашей программой')
        
a = WordCounter()
a.start()
