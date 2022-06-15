#include <stdio.h>
#include <stdlib.h>


typedef void (*function_t)(void* current, void* accumulator);


void sum(void* current, void* accumulator) {
    *(int*)accumulator += *(int*)current;
}


int reduce(void **arr, size_t n, function_t foo) {
    int accumulator = 0;
    for (size_t i=0; i<n; i++) {
        foo(arr[i], &accumulator);
    }
    return accumulator;
}


int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    size_t n = sizeof(numbers) / sizeof(numbers[0]);

    void** numbers_ = malloc(n * sizeof(int*));

    for (size_t i=0; i<n; i++) { 
        numbers_[i] = &numbers[i]; 
    }

    printf("The total sum of all elements of the array is: %d\n", reduce(numbers_, n, sum));

    free(numbers_);
    return 0;
}
