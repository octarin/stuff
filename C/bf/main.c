#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>

#define CODESIZE  0x1000000    // 16MB
#define MEMSIZE   3000         // The size of the memory
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

/* Loads a file into a string dynamically allocated*/
char *load(char *name)
{
    struct stat fbuf;
    int fd;
    unsigned long size;
    char *buf = NULL;

    if ((fd = open(name, O_RDONLY)) == -1) {
        perror("open");
        return NULL;
    }

    fstat(fd, &fbuf);
    size = fbuf.st_size;

    buf = (char*) malloc(size);
    read(fd, buf, size);

    return buf;
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
                if (*mp)
                    *(++sp) = ip;
                else
                    ip = next(ip);

                break;
            case ']':
                if (*mp)
                    ip = *sp;
                else
                    --sp;

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



