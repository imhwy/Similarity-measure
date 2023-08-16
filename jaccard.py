import numpy as np
import string


def jaccard(sentence_1, sentence_2):
    A = set(sentence_1)
    B = set(sentence_2)
    inter = A.intersection(B)
    uni = A.union(B)
    return len(inter) / len(uni)


def main():
    sentence_1 = input("Enter the first sentence: ")
    sentence_2 = input("Enter the second sentence: ")
    print(f"Jaccard similarity: {jaccard(sentence_1, sentence_2)}")
    print(f"Jaccard distances: {1 - jaccard(sentence_1, sentence_2)}")


if __name__ == "__main__":
    main()
