def set_task1():
    first_child_cubes = set()
    second_child_cubes = set()
    cubes_count_first_child = int(input('First child cubes count: '))
    cubes_count_second_child = int(input('Second child cubes count: '))

    print('First child:')
    for _ in range(cubes_count_first_child):
        first_child_cubes.add(input('Cube: '))

    print('Second child:')
    for _ in range(cubes_count_second_child):
        second_child_cubes.add(input('Cube: '))

    print('Union: ', first_child_cubes.union(second_child_cubes))
    print('Intersection: ', first_child_cubes.intersection(second_child_cubes))
    print('Difference: ', first_child_cubes.difference(second_child_cubes))


def set_task2():
    child_count = int(input('Child count: '))
    lang = list()
    for i in range(child_count):
        child_lang_count = int(input('Child lang cont: '))
        lang.append(set())
        for _ in range(child_lang_count):
            lang[i].add(input('Lang: '))

    tmp = lang[0]
    for langs in lang[1:]:
        tmp.update(langs)
    print('one ', tmp)

    tmp = lang[0]
    for langs in lang[1:]:
        tmp.intersection_update(langs)
    print('Every one ', tmp)


def set_task3():
    days_count = int(input('Days: ')) + 1
    days = set(range(1, days_count)).difference(set(range(6, days_count, 7))).difference(set(range(7, days_count, 7)))
    for _ in range(int(input('Parties: '))):
        days.difference_update(set(range(int(input('Fist day: ')),days_count, int(input('Interval: ')))))
    print(len(days))


def dict_task1():
    words = dict()
    for _ in range(int(input('count: '))):
        word1 = input('word1: ')
        word2 = input('word2: ')
        words[word1] = word2
    word_to_find = input('word: ')
    for word, synonym in words.values():
        if word == word_to_find:
            print(synonym)
        if synonym == word_to_find:
            print(word)


def dict_task2():
    words = input().split()
    words_count = dict.fromkeys(set(words), 0)
    for word in words:
        words_count[word] += 1
        print(words_count[word], end=' ')


def dict_task4():
    cities = dict()
    for _ in range(int(input('count: '))):
        cities[input('Country: ')] = input('City: ')
    for country, city in sorted(cities.items(), key=lambda item: item[0]):
        print(city, country)


def dict_task5():
    cities = dict()
    answer = list()
    for _ in range(int(input())):
        lines = input().split()
        for city in lines[1:]:
            cities[city] = lines[0]
    for _ in range(int(input())):
        answer.append(cities.get(input()))
    for a in answer:
        print(a)


dict_task5()
