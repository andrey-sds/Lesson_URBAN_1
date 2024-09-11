from pprint import pprint


class WordsFinder:
    def __init__(self, *list_file):
        self.file_names = list_file

    def get_all_words(self, *file_names):
        all_words = {}
        ss = []

        for files in self.file_names:
            with open(files, encoding='utf-8') as file:
                for line in file:
                    for i in line.split():
                        ss += self.remove_sign(i)
                all_words.update({files: ss})
            return all_words

    def remove_sign(self, line):
        sign_ = [',', '.', '=', '!', '?', ';', ':', ' - ']
        ss = ''
        str_ = []
        for char in line.lower():
            if char in sign_:
                char = char.replace(char, '')
            ss += char
        str_.append(ss)
        return str_

    def find(self, word):
        words = self.get_all_words()
        for key, value in words.items():
            setattr(self, key, value)
            for i in value:
                if i == word.lower():
                    cn = value.index(word.lower()) + 1
        return {key: cn}

    def count(self, word):
        cn = 0
        words = self.get_all_words()
        for key, value in words.items():
            setattr(self, key, value)
            for i in value:
                if i == word.lower():
                    cn += 1
        return {key: cn}


finder2 = WordsFinder('test_file.txt', 'Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder3 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder3.get_all_words())
print(finder3.find('if'))
print(finder3.count('if'))