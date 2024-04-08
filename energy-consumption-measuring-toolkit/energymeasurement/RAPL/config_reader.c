#include <stdio.h>
#include <stdlib.h>
#include <string.h>

double read_config_file(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error opening file %s\n", filename);
        return -1.0;
    }

    char line[100];
    double package_threshold = -1.0;

    while (fgets(line, sizeof(line), file)) {
        char* key = strtok(line, "=");
        char* value = strtok(NULL, "=");
        printf("while loop of read_config_file() \n"); 
        if (strcmp(key, "package_threshold") == 0) {
            package_threshold = atof(value);
             printf("if condition satisfied %f\n", package_threshold); 
            break;
        }
    }

    fclose(file);
    return package_threshold;
}

int main() {
    const char* filename = "config.txt";
    printf("Calling read_config_file()");
    double threshold = read_config_file(filename);
    printf("Package threshold after calling read_config_file(): %f\n", threshold);  
    if (threshold != -1.0) {
        printf("Package threshold: %f\n", threshold);
    }

    return 0;
}


