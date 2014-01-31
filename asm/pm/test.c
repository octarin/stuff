#include <stdio.h>

int main(void)
{
    int mystery, usr;

    mystery = 42;
    usr = 0;

    while (usr != mystery) {
        printf("Entrez un nombre : ");
        scanf("%d", &usr);

        if (usr < mystery) {
            puts("Trop petit !");
        } else if (usr > mystery) {
            puts("Trop grand !");
        } else {
            puts("Bravo ! Vous avez gagné !");
        }
    }
    return 0;
}
