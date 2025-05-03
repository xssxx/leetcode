// 2023.12.23

int maxArea(int* height, int heightSize) {
    int l = 0, r = heightSize - 1;
    int maxArea = 0, area = 0;

    while (l < r) {
        area = fmin(height[l], height[r]) * (r - l);
        maxArea = fmax(maxArea, area);
        height[l] < height[r] ? ++l : --r;
    }
    
    return maxArea;
}