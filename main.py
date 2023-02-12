from minedit import minDistance,load_words
from multiprocessing import Pool,cpu_count,freeze_support
from functools import partial
from itertools import repeat
import msvcrt
import os

def spellcheck(s):
    no_cores = cpu_count()
    words = load_words('words.txt')
    wordss=words[:5]
    with Pool(no_cores) as pool:
        results = pool.starmap(minDistance,zip(words,repeat(s)))
    x = min(results, key = lambda t: t[1])
    print(x[0])

if __name__=="__main__":
    freeze_support()
    string = ''
    print("Begun")
    while True:
        c = msvcrt.getch()
        char = c.decode("utf-8")
        if char=='\n':
            break
        if char=='\b':
            if len(string)>0 and len(string)!=1:
                k = len(string)-1
                string = string[k]
                continue
            if len(string)==1:
                string=''
                continue
        else:
            string = string+char
        os.system('cls')
        print("Word suggestions")
        if len(string)>1:
            spellcheck(string)



