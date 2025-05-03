// 2023.12.02

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int* out = (int*) malloc(numsSize * 2 * sizeof(int));

    memcpy(out, nums, numsSize * sizeof(int));
    memcpy(out + numsSize, nums, numsSize * sizeof(int));

    *returnSize = numsSize * 2;
    return out;
}