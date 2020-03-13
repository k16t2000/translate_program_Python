
global est, rus, word #globalnaja perem-ja, kot mozno ispolzovat v drugih funkzijah
from gtts import *
import sys
import os
import string
import re

def read_from_files(f):#obshij massiv
    file=open(f, encoding="utf-8")
    mas=[]
    for row in file:
        mas.append(row.strip())#kazdaja stroka budet v massive
    file.close()
    return mas

def speak(word,lang):
    from os import system
    tts=gTTS(text=word,lang=lang)
    tts.save('voice.mp3')
    system('start voice.mp3')
    #remove('voice.mp3')

def perevod(eng,rus):#spiski uznaem iz slovara
    word=input("Write word").lower()
    if word in rus:
        index=rus.index(word)
        result=(rus[index]+ '-'+eng[index]+ '\n')
        speak(word,'ru')
        speak(eng[index],'en')
    elif word in eng:
        index=eng.index(word)
        result=(eng[index]+ '-'+rus[index]+ '\n')
        speak(word,'en')
        speak(rus[index],'ru')
    else:
        result=('There is not such word')
        speak(result,'en')
    return result,word

def save_in_file(f,word):
    file=open(f,'a',encoding='utf-8')
    file.write(word+'\n')
    file.close()

def dobavit_slovo(word,eng,rus):
    # from langdetect import detect, detect_langs, DetectFactory
    # DetectFactory.seed=0
    # print(detect(word))
    # list_of_langs=detect_langs(word)
    # for l in list_of_langs:
    #     print(l.lang,'-',l.prob)

    t=False
    rus_alt=read_from_files('abc_rus.txt')
    for a in word:
        if a in rus_alt:
            t=True
            break
        if t==True:
            word_eng=input("input english word: ").lower()
            rus.append(word)
            eng.append(word_eng)#dobavili v spiski
            save_in_file("rus.txt",word)
            save_in_file("eng.txt",word_eng)
        else:
            word_rus=input("input russian word: ").lower()
            eng.append(word)
            rus.append(word_rus)#dobavili spiski
            save_in_file("eng.txt",word)
            save_in_file("rus.txt",word_rus)
        for i in range (len(eng)):
            print(eng[i], '-',rus[i])
    return eng,rus

def update():
    eng=read_from_files('eng.txt')
    rus=read_from_files('rus.txt')
    tupled_list=list(zip(eng,rus))
    #print(type(tupled_list))
    my_dic=dict(tupled_list)
    print(type(my_dic))
    print(my_dic)
    answer=input("Would you like to change word? 1-eng, 2-russian, 0-no")
    while True:
        if answer=="1":
            w=input('Write english word, that needed to be changed ')
            if w in my_dic.keys():
                print("found key")
                word=input("New english word is... ")
                my_dic[word]=my_dic[w]
                del my_dic[w]
                print(str(my_dic))
                f = open("new_slovar.txt","w",encoding='utf-8')
                f.write(str(my_dic))
                fail=open('eng.txt','w')#
                fail.write('')
                for key in my_dic:
                    eng.append(str(key))
                    fail=open('eng.txt','a')
                    fail.write('\n'+key)
                    fail.close()
                print(eng)

            else:
                print("not found")
        elif answer=="2":
            w=input('search by english word for changing russian word ')
            if w in my_dic.keys():
                print("found")
                slovo=input("new russian word is... ")
                my_dic[w]=slovo
                print(str(my_dic))
                f = open("new_slovar.txt","w",encoding='utf-8')
                f.write(str(my_dic))
                f2=open('rus.txt','w',encoding='utf-8')#
                f2.write('')
                for key,value in my_dic.items():
                    #print(value)
                    rus.append(str(value))
                    f2=open('rus.txt','a',encoding='utf-8')
                    f2.write('\n'+value)
                    f2.close()
                print(rus)

            else:
                print("not found")

        elif answer=="0":
            sys.exit()

        else:
            print("false")
        return eng,rus, my_dic







# def perezapis_slovara(eng,rus,word_replace):
#     if word_replace.lower() in rus:
#         index_rus=rus.index(word_replace)
#         rus.remove(rus[index_rus])
#         eng.remove(eng[index_rus])
#     elif word_replace.lower() in eng:
#         index_eng=eng.index(word_replace)
#         rus.remove(rus[index_eng])
#         eng.remove(eng[index_eng])
# #perezapis v fail
# new_rus=open("rus.txt", "w", encoding="utf8")
# new_eng=open("eng.txt", "w", encoding="utf8")
# for list in rus:
#     new_rus.write(list+"\n")
# new_rus.close()
#
# for list in eng:
#     new_eng_write(list+"\n")
# new_eng.close()
# word1=input("pravilnoe slovo ")
# #dobavlenie
# dobavit_slovo(word1,eng,rus)



def slovar():#massiv dlja anglijskogo
    eng=read_from_files('eng.txt')
    rus=read_from_files('rus.txt')
    s,word=perevod(eng,rus)
    print(s)
    # if s=='There is not such word':
    #     soov=input('Would you like to add word in a dictionary? 1-yes, 0-no')
    #     if soov=='1':
    #         eng,rus=dobavit_slovo(word,eng,rus)
    #     elif soov=='0':
    #         sys.exit(0)
    return eng,rus




def check_knowledge():
    from random import randrange
    rus=read_from_files('rus.txt')
    eng=read_from_files('eng.txt')
    correct=0
    incorrect=0
    count_questions=0
    while True:
        q=input('choose 1-english check, 2-russian')
        if q=='1':
            random_index = randrange(len(eng))
            item = eng[random_index]
            #print ("Randomly selected item and its index is - ", item, "Index - ", random_index)
            print(item)
            count_questions+=1
            word=input('write description ')
            index=rus.index(word)
            if word==rus[index]:
                print("good")
                correct+=1
            else:
                print("bad")
                incorrect+=1
                break
        elif q=='2':
            random_index = randrange(len(rus))
            item= rus[random_index]
            #print ("Randomly selected item and its index is - ", item, "Index - ", random_index)
            print(item)
            count_questions+=1
            word=input('write description ')
            index=eng.index(word)
            if word==eng[index]:
                print("good")
                correct+=1
            else:
                print("bad")
                incorrect+=1
                break


        if len(eng)>5:
            if count_questions==5:
                break
        else:
            if count_questions==len(eng):
                break

    rezult=int((correct * 100)/ (correct+incorrect))
    print(rezult,'%')
    return eng,rus



def menu():
    eng=read_from_files('eng.txt')
    rus=read_from_files('rus.txt')
    while True:
        p=input("Choose 1-translate word, 2-add word, 3-check your knowledge, 4-update dictionary") #5-izmenenie slovara
        if p=="1":
            eng,rus=slovar()
        elif p=="2":
            word=input('write a word for adding in a dictionary ')
            if word in rus or word in eng:
                print("The word already exists")
            # elif word in eng:
            #     print("The word already exists in english")
            else:
                dobavit_slovo(word,eng,rus)
                break
        elif p=="3":
            check_knowledge()
        elif p=="4":
            update()
        # elif p=="5":
        #     prep_record()
        #     a=input("Slovo dla izmenenija ")
        #     if (a in rus) or (a in eng):
        #         perezapis_slovara(eng,rus,a)
        #     else:
        #         print("Takogo slovo net")

    return eng,rus



while True:
    eng,rus=menu()
