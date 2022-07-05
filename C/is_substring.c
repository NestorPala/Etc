#include <stdio.h>
#include <stdbool.h>
#include <string.h>


bool is_substring(char* string1, char* string2) {
    size_t len1 = strlen(string1);
    size_t len2 = strlen(string2);

    if (len2 > len1) {
        return false;
    }
    
    int matches = 0;
    
    for (size_t i=0; i<(len1-len2+1); i++) {
        matches = 0; 

        for (size_t j=0; j<len2; j++) {

            // Show the process:
            // printf("char1: %c, char2: %c\n", string1[i+j], string2[j]);

            if (string1[i+j] == string2[j]) {
                matches++;

                if (matches == len2) {
                    return true;
                }
            }
        }
    }
    
    return false;
}


int main() { 
    char* string1 = "Academias";

    char* string2[] = {
        // Substrings
        "A", "Ac", "Aca", "d", "de", "dem", "demias", "Academias", "s",

        // Not susbtrings
        "", " ", "AcademiasABC", "Academias ", " Academias", "Aca demias", "ACADEMIAS", "academias"
    };

    printf("String: '%s'\n\n", string1);
    
    for (size_t i=0; i<17; i++) {
        if (is_substring(string1, string2[i])) {
            printf("'%s' Is substring\n", string2[i]);
        } else {
            printf("'%s' Is not substring\n", string2[i]);
        }
    }

    return 0;
}
