void ntohex(int nb, char* out);
char* stradd(char* buf, char* to_append);

int main(void)
{
    int a = 0xdeadbeef, b = 0x1337;
    char buf[12];

    ntohex(a, buf);
    write(1, buf, 11);
    ntohex(b, buf);
    write(1, buf, 11);

    return 0;
}

void ntohex(int nb, char* out)
{
    unsigned int i;
    char sym[] = "0123456789ABCDEF";

    out = stradd(out, "0x");
    for (i = 0; i < 8; i++) {
        *(out++) = sym[(nb >> ((7 - i) << 2 )) & 0xf];
    }

    *out = 0xa;
}

char* stradd(char* buf, char* to_append)
{
    while (*to_append) {
        *(buf++) = *(to_append++);
    }
    *buf = '\0';
    return buf;
}

