import nltk
import string
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

file = open("Documentation-How-To-Use-Nuclear-Reactor.txt", "r")

text = file.read()

print(text) # Вивід тексту

words = nltk.casual_tokenize(text) # Токенізація
print("\tТокенізація\n", words)

stop_words = set(stopwords.words("english"))
clear_words = [x for x in words if not re.fullmatch('[' + string.punctuation + ']+', x)] # Видалення Пунктуації
clear_words = [word for word in clear_words if not word in stop_words] # Видалення стоп слів

print("\n\tВідібраний текст\n", ' '.join(clear_words))

# Стемінг
ps = PorterStemmer()
root_words = list(map(ps.stem, clear_words))

print("\n\tСтемінг відібраного тексту \n", root_words)

# Лемматизація
wl = WordNetLemmatizer()
lem_words = list(map(wl.lemmatize, clear_words))

print("\n\tЛемматизація відібраного тексту \n", lem_words)