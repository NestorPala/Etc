#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "generador.h"


void arreglo_numeros_destruir(int** numeros, size_t n) {
    for (size_t i=0; i<n; i++) free(numeros[i]);
    free(numeros);
}


void arreglo_cadenas_destruir(char** str, size_t n) {
    for (size_t i=0; i<n; i++) free(str[i]);
    free(str);
}


int** arreglo_numeros_crear(size_t n) {
    int** numeros = malloc(n * sizeof(int*));

    for (size_t i=0; i<n; i++) {
        numeros[i] = malloc(sizeof(int));
        *numeros[i] = rand() % 1000 + 1;
    }

    return numeros;
}


char** arreglo_cadenas_crear(size_t cant) {
    char** palabras = malloc(cant * sizeof(char*));   // 1-d array of pointers to char
    int j = 0;

    // generate 100 strings or random sizes between 3 and 10 letters
    for (size_t i=0; i<cant; i++) {

        int largo = 3 + rand() % 8;  // get random word size in 3..10
        palabras[i] = malloc((size_t)(largo + 1)); // allocated space for word

        for (j=0; j<largo; j++) {
            palabras[i][j] = (char)(97 + rand() % 26);
        }

        palabras[i][j] = '\0';
    }

    return palabras;
}
