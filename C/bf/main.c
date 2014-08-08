#include <stdio.h>
#include <stdlib.h>

#define CODESIZE  0x1000000    // 16MB
#define MEMSIZE   3000         // Dans la spec ?
#define STACKSIZE 0x100000     // 8MB

char *load(char*);
void interp(char*);
char *next(char*);

static char mem[MEMSIZE] = {'\0'};
static char *stack[STACKSIZE] = {NULL};

int main(int argc, char *argv[])
{
    char *code = NULL;

    /* Loads the code */
    if (argc <= 1 || (code = load(argv[1])) == NULL)
        return -1;

    interp(code);

    free(code);

    return 0;
}

/* Loads the code into a string */
char *load(char *name)
{
    FILE *fd = NULL;

    if ((fd = fopen(name, "r")) == NULL) {
        perror("fopen");
        return NULL;
    }

    char *code = NULL, *nreal = NULL;
    int i = 0, ret = 0;

    code = malloc(CODESIZE);
    if (code == NULL) {
        perror("malloc");
        fclose(fd);
        return NULL;
    }

    while ( (code[i++] = fgetc(fd)) != EOF) {
        if (i >= CODESIZE) {
            fprintf(stderr, "Error : your code exceed %dMB\n. Aborting\n", CODESIZE);
            free(code);
            fclose(fd);
            return NULL;
        }
    }

    fclose(fd);

    if ( (nreal = realloc(code, i)) == NULL) {
        perror("realloc");
        free(code);
        return NULL;
    }

    code = nreal;
    code[--i] = 0;

    return code;
}

/* Interprète le code brainfuck */
void interp(char *code)
{
    char *ip = code;
    char **sp = stack;
    char *mp = mem;

    while (*ip) {

        switch (*ip) {
            case '+':
                ++(*mp);
                break;
            case '-':
                --(*mp);
                break;
            case '>':
                mp = (mp + 1 - mem) % MEMSIZE + mem;
                break;
            case '<':
                mp = (mp - 1 - mem) % MEMSIZE + mem;
                break;
            case ',':
                *mp = getchar();
                break;
            case '.':
                putchar(*mp);
                break;
            case '[':
                if (*mp) {
#ifdef DEBUG
                    printf("[: stack += %x\n", ip - code);
#endif
                    *(++sp) = ip;
                } else {
#ifdef DEBUG
                    printf("[: on passe de %x à ", ip - code);
#endif
                    ip = next(ip);
#ifdef DEBUG
                    printf("%x\n", ip - code);
#endif
                }

                break;
            case ']':
                if (*mp) {
#ifdef DEBUG
                    printf("]: on boucle  de %x à %x\n", ip - code, *sp - code);
#endif
                    ip = *sp;
                } else {
#ifdef DEBUG
                    printf("]: on sort en %x\n", ip - code);
#endif
                    --sp;
                }

                break;
        }
        ++ip;
    }
}

char *next(char *ip)
{
    int balance = 0;

    do {
        if (*ip == '[')
            ++balance;
        else if (*ip == ']')
            --balance;
        ++ip;
    } while (balance);

    return ip - 1;
}



