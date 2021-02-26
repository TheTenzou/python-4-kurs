import os

dirname = os.path.dirname(__file__)

def task1():
    file_name = os.path.join(dirname, 'input1.txt')
    with open(file_name, "r") as input_file:
        print(len(set(input_file.read().split())))


def task2():
    file_name = os.path.join(dirname, 'input2.txt')
    with open(file_name, "r") as input_file:
        for line in input_file:
            print(sum(map(lambda x: int(x), line.split())))


def task3():
    file_name = os.path.join(dirname, 'input3.txt')
    answare_file = os.path.join(dirname, 'output3.txt')
    with open(file_name, "r") as input_file:
        words = input_file.read().split()
        count_word = dict() 
        for word in words:
            count_word[word] = count_word.get(word, 0) + 1
        with open(answare_file, "w") as output_file:
            for word, count in sorted(count_word.items(), key=lambda item: (-item[1], item[0])):
                output_file.write(word + " " + str(count) + "\n")


def task4():
    file_name = os.path.join(dirname, 'input4.txt')
    with open(file_name, "r") as input_file:
        lines = reversed(input_file.readlines())
        for line in lines:
            print(line[::-1])


def task5():
    file_name = os.path.join(dirname, 'input5.txt')
    with open(file_name, "r") as input_file:
        chars = input_file.read() + " ";
        char_count = 0
        word_count = 0
        line_count = 0
        for i in range(len(chars) - 1):
            if chars[i].isalpha():
                char_count += 1
            if chars[i].isalpha() and not(chars[i+1].isalpha()):
                word_count +=1
            if chars[i] == "\n":
                line_count +=1
        print(char_count, word_count, line_count)
        

def task6():
    file_name = os.path.join(dirname, 'input6.txt')
    answare_name = os.path.join(dirname, 'output6.txt')
    with open(file_name, "r") as input_file:
        with open(answare_name, "w") as output_file:
            output_file.write(input_file.read()[::-1])

    

task5()
