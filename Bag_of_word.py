# import libraries
import numpy as np
import pandas as pd
import re


# preprocessing sentences
def sentence_processing(sentence):
    return re.sub(r"[^a-zA-Z0-9]", " ", sentence.lower()).split()


# creating a wordset contain different words
def creating_wordset(sentences):
    wordset = sentences[0]
    for i in sentences:
        wordset = np.union1d(wordset, i)
    return wordset


# implement BOW
def bag_of_words(wordset, l_doc):
    tf_diz = dict.fromkeys(wordset, 0)
    for word in l_doc:
        tf_diz[word] = l_doc.count(word)
    return tf_diz


# run code
def main():
    print(
        "There are two ways to implement:\n1. Using 2 available sentences.\n2. Input 2 sentences from keyboard."
    )
    option = int(input("Option: "))
    while option not in [1, 2]:
        option = input("Enter option: again: ")
    if option == 1:
        first_sentence = "UIT is one of the top universities in Vietnam for information technology education."
        second_sentence = "UIT has a team of highly qualified and experienced faculty members who are experts in their fields."
    else:
        first_sentence = input("Enter the first sentence: ")
        second_sentence = input("Enter the second sentence: ")
    processed_first_sentence = sentence_processing(first_sentence)
    processed_second_sentence = sentence_processing(second_sentence)
    sentences = []
    sentences.append(processed_first_sentence)
    sentences.append(processed_second_sentence)
    wordset = creating_wordset(sentences)
    bow_list = []
    for i in sentences:
        bow_list.append(bag_of_words(wordset, i))
    df = pd.DataFrame(bow_list)
    print(df)


if __name__ == "__main__":
    main()
