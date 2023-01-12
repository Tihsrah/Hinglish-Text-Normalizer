key_error_dict = {
    # "a" = [up,down,left,right]
    'q': [0, "a", 0, "w"],
    'w': [0, "s", "q", "e"],
    'e': [0, 'd', 'w', 'r'],
    'r': [0, 'f', 'e', 't'],
    't': [0, 'g', 'r', 'y'],
    'y': [0, 'h', 't', 'u'],
    'u': [0, 'j', 'y', 'i'],
    'i': [0, 'k', 'u', 'o'],
    'o': [0, 'l', 'i', 'p'],
    'p': [0, 0, 'o', 0],
    'a': ['q', 'z', 0, 's'],
    's': ['w', 'x', 'a', 'd'],
    'd': ['e', 'c', 's', 'f'],
    'f': ['r', 'v', 'd', 'g'],
    'g': ['t', 'b', 'f', 'h'],
    'h': ['y', 'n', 'g', 'j'],
    'j': ['u', 'm', 'h', 'k'],
    'k': ['i', 'm', 'j', 'l'],
    'l': ['o', 0, 'k', 0],
    'z': ['a', 0, 0, 'x'],
    'x': ['s', 0, 'z', 'c'],
    'c': ['d', 0, 'x', 'v'],
    'v': ['f', 0, 'c', 'b'],
    'b': ['g', 0, 'v', 'n'],
    'n': ['h', 0, 'b', 'm'],
    'm': ['j', 0, 'n', 0]

}
word = "doing"


def typing_error(word):
    length = len(word)
    error_list = []
    for i in range(1, length):
        letter_to_check = word[i]
        list_of_possible_error = key_error_dict[letter_to_check]
        print(list_of_possible_error)
        for j in range(4):
            if list_of_possible_error[j] == 0:
                continue
            new_word = word[:i]+list_of_possible_error[j]+word[i+1:]
            error_list.append(new_word)
            # print(i, j, list_of_possible_error[j])
    return error_list


test = typing_error(word)
print(test)
