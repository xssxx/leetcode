// 2023.12.03

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* convertTemperature(double celsius, int* returnSize) {
    double* out = (double*) malloc(2 * sizeof(double));

    out[0] = celsius + 273.15;
    out[1] = celsius * 1.8 + 32.0;

    *returnSize = 2;
    return out;
}