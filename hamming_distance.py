import numpy as np


def hamming_distance(sentence_1, sentence_2):
    hamming = np.zeros(len(sentence_1))
    for i in range(len(sentence_1)):
        if sentence_1[i] != sentence_2[i]:
            hamming[i] = 1
    diff = len([x for x in hamming if x == 1])
    return diff, diff / len(hamming)


def main():
    print("There sentences must have the same length:")
    sentence_1 = input("Enter the first sentence: ")
    sentence_2 = input("Enter the second sentence: ")
    if len(sentence_1) != len(sentence_2):
        print("Those sentences do not have the same length!")
    else:
        diff_value, hamming = hamming_distance(sentence_1, sentence_2)
        print(f"The hamming distance: {diff_value}")
        print(f"The distance percentage: {hamming}")


if __name__ == "__main__":
    main()
