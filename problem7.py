"""
Write a python function to remove a given word from a list and strip
it at the same time.
"""
  
def remove(l, word):
    n = []
    for i in l:
        if i!=word:
            n.append(i.strip(word))
    return n
       

word=input("enter the word: ") # "ant"
l = ["Ishant","Sushant","Prashant","ant"]

print(remove(l, word))