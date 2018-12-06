import re

source_file = open("./word_source.txt", 'r')

file_contexts = source_file.read()
file_context = re.split(' |\n', file_contexts)

source_file.close()

word_list = dict()

for word_all in file_context:
    words = word_all.translate(str.maketrans('', '', ',\t\n“”‘’?•①')).lower()
    #①\/"()“”•;_?‘’\t\n.\\!:
    if str(words) not in word_list:
        word_list[words] = 1
    elif str(words) in word_list:
        word_list[words] = word_list[words] + 1
    else:
        pass

txtFile = open("./word_list.txt", 'w')

wordstr = str(sorted(word_list.items(), key = lambda item:item[1], reverse = True)).translate(str.maketrans('', '', "[]() '"))

while wordstr :
    real_word = wordstr.split(",", 2)[0] + ',' + wordstr.split(",", 2)[1] + "\n"
    if  "http" not in real_word:
        txtFile.write(real_word)
    wordstr = wordstr.split(",", 2)[2]
    if wordstr.count(',') == 1:
        txtFile.write(wordstr.split(",", 2)[0] + ',' + wordstr.split(",", 2)[1] + "\n")
        break


txtFile.close()