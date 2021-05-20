# Через Python у себя на рабочем 
# столе создайте директорию, а 
# внутри дериктории создайте 5 РАНДОМНЫХ файлов.
import os, random
os.mkdir('/home/nurs/Рабочий стол/some_dir/')
for i in range(5):
    with open(f'/home/nurs/Рабочий стол/some_dir/text_file' + str(random.randint(1, 1234)) + '.txt','w') as file:
        file.write(str(i))