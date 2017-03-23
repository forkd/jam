/*#include <stdio.h>
#include <time.h>

void wait ( int seconds )
{
 clock_t endwait;
 endwait = clock () + seconds * CLK_TCK;
 while (clock() < endwait) {}
}

int main ()
{
 int n;
 printf ("Starting countdown...\n");
 for (n=10; n>0; n--)
 {
   printf ("%d\n",n);
   wait (1);
 }
 printf ("FIRE!!!\n");
 return 0;
}

#include "stdio.h"
#include "conio.h"

int main(int argc, char* argv[])
{
int c;
printf("Inicando a contagem regressiva: \n");

for (c=10; c>=0; c--){
      printf("%02d\n",c);
      Sleep(1000); //Valor em Milissegundos
}

printf("FIRE!!!\n");
getch();
return 0;
}*/

#include <stdio.h>

/* Formato do texto */
/* RESET,BOLD,UNDERLINE,BLINK,REVERSE */

#define RS "\033[0m"
#define OL "\033[1m"
#define UL "\033[4m"
#define LI "\033[5m"
#define RV "\033[7m"


/* Cor de texto (FOREGROUND)*/
/* BLACK, RED, GREEN, YELLOW/ORANGE, BLUE, MAGENTA, TURQUIOSE, WHITE */

#define FK "\033[30m"
#define FR "\033[31m"
#define FG "\033[32m"
#define FO "\033[33m"
#define FB "\033[34m"
#define FM "\033[35m"
#define FT "\033[36m"
#define FW "\033[37m"


/* Cor de texto (BACKGROUND)*/
/* BLACK, RED, GREEN, YELLOW/ORANGE, BLUE, MAGENTA, TURQUIOSE, WHITE */

#define BK "\033[40m"
#define BR "\033[41m"
#define BG "\033[42m"
#define BO "\033[43m"
#define BB "\033[44m"
#define BM "\033[45m"
#define BT "\033[46m"
#define BW "\033[47m"

main()
{

/* Imprime as palavras consoante o seu formato.*/
/* Alguns destes formatos so aparecem em determinados modos de ecran, */
/* como por exemplo em ambientes X-Windows.                           */

printf("%s Bold      %s\n",OL,RS);
printf("%s Underline %s\n",UL,RS);
printf("%s Blink     %s\n",LI,RS);
printf("%s Reverse   %s\n\n",RV,RS);

printf("\n\n");

/* Imprime as palavra, com a cor de fundo indicada                   */
/* BLACK, RED, GREEN, YELLOW/ORANGE, BLUE, MAGENTA, TURQUIOSE, WHITE */

printf("%s Preto    %s\n",BK,RS);
printf("%s Vermelho %s\n",BR,RS);
printf("%s Verde    %s\n",BG,RS);
printf("%s Laranja  %s\n",BO,RS);
printf("%s Azul     %s\n",BB,RS);
printf("%s Magenta  %s\n",BM,RS);
printf("%s Turquesa %s\n",BT,RS);
printf("%s%s Branco   %s\n",BW,FK,RS);

printf("\n\n");

/* Imprime as palavras com a cor de texto indicada                   */
/* Usa tambem a formatacao BOLD para mostrar as corre carregadas     */
/* BLACK, RED, GREEN, YELLOW/ORANGE, BLUE, MAGENTA, TURQUIOSE, WHITE */

printf("%s Preto    %s Preto    %s\n",FK,OL,RS);
printf("%s Vermelho %s Vermelho %s\n",FR,OL,RS);
printf("%s Verde    %s Verde    %s\n",FG,OL,RS);
printf("%s Laranja  %s Amarelo  %s\n",FO,OL,RS);
printf("%s Azul     %s Azul     %s\n",FB,OL,RS);
printf("%s Magenta  %s Magenta  %s\n",FM,OL,RS);
printf("%s Turquesa %s Turquesa %s\n",FT,OL,RS);
printf("%s Branco   %s Branco  %s\n\n",FW,OL,RS);



printf("%s%sC%so%sl%so%sr%ss%s 2.1%s - by %s%sDragon%s\n",OL,FR,FG,FO,FB,FM,FT,FW,RS,LI,UL,RS);

}
