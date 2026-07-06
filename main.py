import json
import time
import random
print("^^^^^^^^^^^^^^^^^^^^ TYPING SPEED TESTER^^^^^^^^^^^^^^^^^^^^^^^")
f=open("TYPING_TESTER\para.json","r")
data=json.load(f)
f.close()
correct=0
print("TYPE THE ABOVE PARAGRAPH : ")
paragraph=random.choice(data["para"])
print(paragraph)
start_time=time.time()
print("Starting in.....")
print("3")
print("2")
print("1")
print("Go !")
user_para=input("START : ")
time_taken=time.time()-start_time
print("=================================")
print("RESULT")
print("=================================")
print("TIME TAKEN : ",round(time_taken,2),"sec")
typed_words = user_para.split()
original_words = paragraph.split()
print("WPM : ",round(len(typed_words)/time_taken,2)*60)
for i in range (min(len(typed_words),len(original_words))):
    if typed_words[i]==original_words[i]:
        correct+=1
print("ACCURACY : ",(correct/len(typed_words)*100))

