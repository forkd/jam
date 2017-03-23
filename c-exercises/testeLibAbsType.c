/* Programa de teste para os tipos abstratos de dados Lista, Pilha e Fila,
      Através da implementação por ponteiros.
   Autor: José Lopes de Oliveira Júnior                                    */

#include "libabstype.h"

/* Interfaces para teste... */

/* O que quer fazer? */
int menuAcoes ()
{
   int op = 0;
      
   do {
      printf( "\n\nPrograma-teste do tipo abstrato de dados Lista.\n" );
      printf( "1. Criar estrutura\n2. Verificar se está vazia\n3. Inserir item\n4. Remover item\n5. Imprimir na tela\n6. Sair\n" );
      printf( "Escolha uma opção e tecle <ENTER>: " );
      scanf( "%d", &op );
      
      if ( ( op < 1 ) || ( op > 6 ) )
         printf( "\n\nERRO: Opção inválida. Tente de novo.\n" );
   } while ( ( op < 1 ) || ( op > 6 ) );
   
   return op;
} /* menuAcoes */

Item entrada ()
{
   Item i;
   
   printf( "\nEntre com o token: " );
   scanf( "%s", &i.token );
   
   printf( "\nEntre com a classe do token: " );
   scanf( "%s", &i.class );
   
   printf( "\nEntre com o valor do token: " );
   scanf( "%d", &i.value );
   
   printf( "\nEntre com a linha do token: " );
   scanf( "%d", &i.coOrdinate.row );
   
   printf( "\nEntre com a coluna do token: " );
   scanf( "%d", &i.coOrdinate.column );
   
   return i;
} /* entrada */

/* A funcao principal... */
main ()
{
   Item i;

   int op =0;
   
   List lista;
   
   do {
      op = menuAcoes();
      
      switch ( op ) {
         case 1:
            createList( &lista );
            printf( "\nLista criada!" );
            break;
         
         case 2:
            if ( emptyList( &lista ) )
               printf("\033[;34;1m\n\nLista VAZIA.\n\n\033[m");
            else
               printf("\033[;34;1m\n\nLista NÃO vazia.\n\n\033[m");
            break;
            
         case 3:
            i = entrada();
            insert( &lista, i );
            break;
         
         case 4:
            printf("\033[;34;1m Azul com fundo preto. \033[m");
            break;
         
         case 5:
            printf("\033[;34;1m\nInício da impressão.\n\033[m");
            
            if ( printList( &lista ) )
               printf( "\nERRO: Lista vazia.\n" );
            
            printf("\033[;34;1m\nFim da impressão.\n\033[m");
            break;
         
         case 6:
            break;
         
         default:
            break;
      } /* switch */
   } while ( op != 6);
} /* main */
