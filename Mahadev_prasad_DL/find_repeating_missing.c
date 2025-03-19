#include <stdio.h>

void find_missing_and_repeating(int arr[], int n, int *repeating, int *missing) {
    int sum_n = n * (n + 1) / 2;
    int sum_n_sq = n * (n + 1) * (2 * n + 1) / 6;

    int sum_arr = 0, sum_arr_sq = 0;

    for (int i = 0; i < n; i++) {
        sum_arr += arr[i];
        sum_arr_sq += arr[i] * arr[i];
    }

    int diff = sum_n - sum_arr;
    int diff_sq = sum_n_sq - sum_arr_sq;
    
    int sum_xy = diff_sq / diff;

    *missing = (diff + sum_xy) / 2;
    *repeating = sum_xy - *missing;
}

int main() {
    int arr[] = {4, 3, 6, 2, 1, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    int repeating, missing;
    find_missing_and_repeating(arr, n, &repeating, &missing);

    printf("Repeating number: %d\n", repeating);
    printf("Missing number: %d\n", missing);

    return 0;
}
