/* 
 * Brainfuck interpreter implementation
 * (C) Pierre Bonnet 2013
 * This program is free software.
 * Read the GNU General Public License for more informations
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CAR 1024 * 1024     // 1 MB symbols max (including the comments)
#define MEMSIZE 500             // Memory size

void print_usage(void)
{
    puts("Brainfuck interpreter (C) Pierre Bonnet 2013");
    puts("Version 1.0");
    puts("This program reads the brainfuck symbols\nfrom the standard input and execute the brainfuck");
}

int parse(char* string)
{
    int i, nd, nf;

    for (i = nd = nf = 0; string[i]; i++) {
        if (string[i] == '[')
            nd++;
        else if (string[i] == ']')
            nf++;
    }

    return nd - nf;
}

int main(int argc, char* argv[])
{
    FILE* fichier = stdin;
    char *code = (char*) malloc(MAX_CAR);
    char mem[MEMSIZE];
    char **stack = NULL;
    char *ip = code;
    char *mp = mem;
    int i = 0, nloop = 0;

    (void*) memset(mem, 0, MEMSIZE);

    if (argc > 1) { 
        if (!strcmp(argv[1], "--help")) {
            print_usage();
            return 0;
        } else {
            if (!(fichier = fopen(argv[1], "r"))) {
                fprintf(stderr, "Could'nt open file\n");
                return 1;
            }
        }
    }


    /* Fill the code string with stdin */
    do {
        code[i] = fgetc(fichier);
    } while (code[i++] != EOF);
    code = realloc(code, i);
    code[i - 1] = 0;

    if (parse(code) < 0) {
        perror("Error : more ']' than '['. Stopping.");
        return 1;
    } else if (parse(code) > 0) {
        perror("Error : more '[' than ']'. Stopping.");
        return 1;
    }

    /* Begin the executing */
    while (*ip) {
        switch (*ip) {
            case '+':
                ++*mp;
                break;
            case '-':
                --*mp;
                break;
            case '>':
                if (mp + 1 != mem + MEMSIZE) {
                    ++mp;
                } else {
                    mp = mem;
                }
                break;
            case '<':
                if (mp - 1 >= mem) {
                    --mp;
                } else {
                    mp = mem + MEMSIZE - 1;
                }
                break;
            case '[':
                if (*mp) {
                    stack = realloc(stack, ++nloop);
                    stack[nloop - 1] = ip;
                } else {
                    ip = strchr(ip, ']');
                }
                break;
            case ']':
                if (*mp) {
                    ip = stack[nloop - 1];
                } else {
                    stack = realloc(stack, --nloop);
                }
                break;
            case '.':
                putchar(*mp);
                break;
            case ',':
                *mp = getchar();
                break;
        }
        ++ip;
    }

    free(code);
    return 0;
}

