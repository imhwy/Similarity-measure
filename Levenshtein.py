# import libraries
import numpy as np
import re


# print the matrix
def matrix_print(dis, sentence_1, sentence_2):
    print("The matrix: ")
    for i in range(sentence_1 + 1):
        for j in range(sentence_2 + 1):
            print(int(dis[i][j]), end=" ")
        print()


# levenshtein distance implementation
def levenshtein(sentence_1, sentence_2, a, b, c):
    dis = np.zeros((len(sentence_1) + 1, len(sentence_2) + 1))
    for i in range(len(sentence_1) + 1):
        dis[i][0] = i
    for i in range(len(sentence_2) + 1):
        dis[0][i] = i
    for i in range(1, len(sentence_1) + 1):
        for j in range(1, len(sentence_2) + 1):
            if sentence_1[i - 1] == sentence_2[j - 1]:
                dis[i][j] = dis[i - 1][j - 1]
            else:
                a = dis[i][j - 1]
                b = dis[i - 1][j]
                c = dis[i - 1][j - 1]
                if a <= b and a <= c:
                    dis[i][j] = a + 1
                elif b <= a and b <= c:
                    dis[i][j] = b + 1
                else:
                    dis[i][j] = c + 1
    matrix_print(dis, len(sentence_1), len(sentence_2))
    return dis[len(sentence_1)][len(sentence_2)]


# run code
def main():
    sentence_1 = input("Enter the first sentence: ")
    sentence_2 = input("Enter the second sentence: ")
    distance = levenshtein(sentence_1, sentence_2, 0, 0, 0)
    print(f"The levenshtein value: {distance}")


if __name__ == "__main__":
    main()
