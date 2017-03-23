/* Programa de teste para os tipos abstratos de dados Lista, Pilha e Fila,
      Através da implementação por ponteiros.
   Autor: José Lopes de Oliveira Júnior                                    */

#include "stdlib.h"

/* Definindo o tipo Pointer, que serah o apontador utilizado */
typedef struct TCell *Pointer;

/* Definindo a estrutura de coordenadas - linha x coluna */
typedef struct {
   int row, column;
} CoOrdinate;

/* Definindo a estrutura dos itens a serem armazenados */
typedef struct {
   char token[ 100 ], /* O Token lido */
        class[ 100 ]; /* A classe do token */
   long value; /* A posicao do token na tabela de simbolos */
   CoOrdinate coOrdinate; /* A posicao do token no codigo-fonte */
} Item;

/* Definindo a estrutura das celulas */
typedef struct TCell {
   Item item;
   Pointer next;
} Cell;

/* Estrutura da Fila */
typedef struct {
   Pointer begin, end;
} Row;

/* Operacoes sobre Filas */

/* Cria uma Fila vazia */
void createRow ( Row *row )
{
   /* Alocando espaco em memoria e atribuindo-o ao
         elemento do inicio da Fila.               */
   row -> begin = ( Pointer ) malloc( sizeof( Cell ) );
   
   /* Fazendo que o elemento do fim aponte para o
         mesmo local que o do inicio - Fila Vazia */
   row -> end = row -> begin;
   
   /* Fazendo com que o proximo elemento apos o
         do inicio, seja o NULO.                */
   row -> begin -> next = NULL;
} /* createRow */

/* Verifica se uma Fila estah vazia */
int emptyRow ( Row *row )
{
   return ( row -> begin == row -> end );
} /* emptyRow */

/* Enfileira um elemento no fim da Fila */
int placeInRow ( Row *row, Item i )
{
   /* Atribuindo ao proximo elemento, apos o ultimo,
         o endereco de memoria alocado.              */
   row -> end -> next = ( Pointer ) malloc( sizeof( Cell ) );
   
   /* Fazendo com que o novo fim da Fila seja o
         elemento recem criado.                 */
   row -> end = row -> end -> next;
   
   /* Atribuindo ao novo elemento,
         o item a ser inserido.    */
   row -> end -> item = i;
   
   /* Fazendo com que o proximo elemento apos o
         do fim, seja o NULO.                   */
   row -> end -> next = NULL;
   
   /* Operacao realizada com exito */
   return 0;
} /* placeInRow */

/* Desenfileira um elemento da Fila */
int placeOutRow ( Row *row, Item *item )
{
   /* Verificando se a Fila estah vazia */
   if ( emptyRow( row ) )
      return 1; /* Fila vazia */
   
   else {
      /* A Fila nao estah vazia */
      
      /* Definindo um ponteiro auxiliar e apontando-o
            para o inicio da Fila.                    */
      Pointer aux = row -> begin;
      
      /* Fazendo com que o elemento do inicio da Fila
            seja o segundo elemento da Fila.          */
      row -> begin = row -> begin -> next;
      
      /* Atribuindo a item, o item que serah
            excluido.                        */
      *item = row -> begin -> item;
      
      /* Liberando espaco em memoria - excluindo */
      free( aux );
   } /* else */
   
   /* Operacao realizada com exito */
   return 0;
} /* placeOutRow */

/* Imprime na tela a Fila */
int printRow ( Row *row )
{
   /* Verificando se a Fila estah vazia */
   if ( emptyRow( row ) )
      return 1; /* Fila vazia */
   
   else {
      /* A Fila nao estah vazia */
      
      /* Um ponteiro auxiliar para varrer a Fila */
      Pointer aux = row -> begin -> next;
      
      /* Imprime enquanto nao chegar ao fim da Fila */
      while ( aux != NULL ) {
         /* Imprimindo... */
         printf( "%2d%10s\n", aux -> item.value, aux -> item.token );
         
         /* Atualizando a variavel aux */
         aux = aux -> next;
      } /* while */
   } /* else */
   
   /* Operacao realizada com exito */
   return 0;
} /* printList */

/*****************************************************************************************************/

/* Interfaces para teste... */

/* O que quer fazer? */
int menuAcoes ()
{
   int op = 0;
      
   do {
      printf( "\n\nPrograma-teste do tipo abstrato de dados Fila.\n" );
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
   
   Row row;;
   
   do {
      op = menuAcoes();
      
      switch ( op ) {
         case 1:
            createRow( &row );
            printf( "\nFila criada!" );
            break;
         
         case 2:
            if ( emptyRow( &row ) )
               printf("\033[;34;1m\n\nFila VAZIA.\n\n\033[m");
            else
               printf("\033[;34;1m\n\nFila NÃO vazia.\n\n\033[m");
            break;
            
         case 3:
            i = entrada();
            placeInRow( &row, i );
            break;
         
         case 4:
            placeOutRow( &row, &i );
            
            break;
         
         case 5:
            printf("\033[;34;1m\nInício da impressão.\n\033[m");
            
            if ( printRow( &row ) )
               printf( "\nERRO: Fila vazia.\n" );
            
            printf("\033[;34;1m\nFim da impressão.\n\033[m");
            break;
         
         case 6:
            break;
         
         default:
            break;
      } /* switch */
   } while ( op != 6);
} /* main */
