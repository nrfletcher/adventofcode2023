#include <stdio.h>
#include <string.h>

int function(char *str) {
        return 0;
}

int main(int argc, char *argv[]) {
        FILE *file;
		file = fopen("input.txt", "r");
        int total = 0;

        for(int i = 1; i < argc; i++) {
                char *line = argv[i];
                char num[3];
                char last;
                char first;
                int currentTotal = 0;
                int totalInts = 0;

                for(int j = 0; j < strlen(argv[i]); j++) {
                        if(argv[i][j] >= '0' && argv[i][j] <= '9') {  
                                if(currentTotal == 0) {
                                        first = argv[i][j];
                                }
                                last = argv[i][j];

                                currentTotal++;
                        }
                }
                num[0] = first;
                num[1] = last;
                num[2] = '\0';

                total += atoi(num);
                printf("%s \n", num);
        }

        printf("%d \n", total);

        return 0;
}
