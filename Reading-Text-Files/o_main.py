#openfile = open("./story.txt","r")
def readfile(filename):
    with open("./story.txt","r") as file:
        read_file = file.read()
    return read_file
        #content_file = file.read()
        #print(content_file)
        #print("This file exists")


def count_words():
    text = readfile("./story.txt")
    text_file = text.split()
    #print(text_file)
    count = {}
    for i in text_file:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


print(count_words())

