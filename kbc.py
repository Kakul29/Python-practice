print("welcome to kbc. you will be asked 4 questions, for every correct answer you receive a cashprize of 10000 rupees. if it goes wrong, game gets terminated. all the best")
ques=["what is india's capital\n delhi\nchandigarh\njaipur\nmumbai", "what is largest state in india\nuttar pradesh\nmaharashtra\nkerala\nrajasthan","who is father of nation\njawaharlal nehru\nmodi\nmahatma gandhi\njinnah","which prime number comes after 11\n12\n13\n17\nnone"]
correct=["delhi","rajasthan","mahatma gandhi","13"]
count=0
for i in range(0,4):
    print(ques[i])
    ans=input("enter your answer")
    if ans==correct[i]:
        print("congratulations, correct answer")
        count=count+10000
    else:
        print("wrong answer. game lost") 
        break   
print("hope you enjoyed playing, you have won rupees:" ,count)