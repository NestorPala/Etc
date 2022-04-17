#include <stdio.h>
#include "generador.h"


void probar_numeros(size_t cant) {
    int** numeros = arreglo_numeros_crear(cant);

    for (size_t i = 0; i < cant; i++) {
        printf("%d\t", *numeros[i]);
    }
    
    arreglo_numeros_destruir(numeros, cant);
}


void probar_cadenas(size_t cant) {
    char** palabras = arreglo_cadenas_crear(cant);

    for (size_t i = 0; i < cant; i++) {
        printf("%s\t", palabras[i]);
    }
    
    arreglo_cadenas_destruir(palabras, cant);
}


int main(void) {
    size_t cant = 100;

    printf("\n");
    probar_cadenas(cant);
    printf("\n");
    printf("\n");
    probar_numeros(cant);
    printf("\n");
    printf("\n");

    return 0;
}
