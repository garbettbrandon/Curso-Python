sentence = "Hey fellow warriors"


def spin_words(sentence):
    without_space = sentence.split(" ")
    result = []
    for word in without_space:
        if len(word) >= 5:
            reverse = word[::-1]
            result.append(reverse)
        else:
            result.append(word)
    return " ".join(result)


print(spin_words(sentence))
