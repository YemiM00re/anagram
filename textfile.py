def read_file_content(filename):
    with open(filename,'r') as m:
        my_file=m.read()
    return my_file
  
def count_words():
    text = read_file_content("./story.txt")
  
    my_word=text.split()

    counts=dict(enumerate(my_word,start=1))
    counts={v:k for k, v in counts.items()}
    unique=set(my_word)

    return counts
print(count_words())