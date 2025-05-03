// 2023.12.02

int substr(char ch, char* words) {
    while (*words) {
        if (ch == *words)
            return 1;
        words++;
    }

    return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) {
    int* out = (int *) malloc(wordsSize * sizeof(int));
    int len = 0;

    for (int i = 0; i < wordsSize; i++) {
        if (substr(x, words[i])) {
            out[len] = i;
            len++;
        }
    }

    *returnSize = len;
    return out;
}