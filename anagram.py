def find_anagram(string1, string2):

    if(sorted(string1)== sorted(string2)):
        answer=True
    else:
        answer=False
    return answer
string1=input("My first word: ")
string2=input("My Second word: ")
answer=find_anagram(string1,string2)
print(answer)
print(find_anagram("hello","check"))
print(find_anagram("below","elbow"))