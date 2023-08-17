# import libraries
import numpy as np
import pandas as pd
import math
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


# implement TF
def TF(bow_element, processed_sentence):
    tfDict = {}
    bow_counting = len(processed_sentence)
    for word, count in bow_element.items():
        tfDict[word] = count / float(bow_counting)
    return tfDict


# implement IDF
def IDF(bow_list):
    length = len(bow_list)
    idfDict = dict.fromkeys(bow_list[0].keys(), 0)
    for i in bow_list:
        for word, value in i.items():
            if value > 0:
                idfDict[word] += 1
    for word, value in idfDict.items():
        idfDict[word] = math.log(length / float(value))
    return idfDict


# combine both IF IDF by multiplying
def TF_IDF(tf_value, idf_value):
    tf_idf = {}
    for word, value in tf_value.items():
        tf_idf[word] = value * idf_value[word]
    return tf_idf


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
    bef_sentences = []
    bef_sentences.append(first_sentence)
    bef_sentences.append(second_sentence)
    processed_first_sentence = sentence_processing(first_sentence)
    processed_second_sentence = sentence_processing(second_sentence)
    sentences = []
    sentences.append(processed_first_sentence)
    sentences.append(processed_second_sentence)
    wordset = creating_wordset(sentences)
    bow_list = []
    for i in sentences:
        bow_list.append(bag_of_words(wordset, i))
    tf_values = []
    tf_values.append(TF(bow_list[0], processed_first_sentence))
    tf_values.append(TF(bow_list[1], processed_second_sentence))
    idf_values = IDF(bow_list)
    tf_idf_values = []
    tf_idf_values.append(TF_IDF(tf_values[0], idf_values))
    tf_idf_values.append(TF_IDF(tf_values[1], idf_values))
    df = pd.DataFrame(tf_idf_values)
    print(f"Visualize: \n{df}\n")
    for i in range(0, 2):
        print(bef_sentences[i])
        for key, value in tf_idf_values[i].items():
            if key in sentences[i]:
                print(key, ":", value)
        print("\n")


if __name__ == "__main__":
    main()
