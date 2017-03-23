/* Programa de teste para os tipos abstratos de dados Lista, Pilha e Fila,
      Através da implementação por ponteiros.
   Autor: José Lopes de Oliveira Júnior                                    */

#include "stdio.h"
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

/* Definindo as estruturas Lista, Pilha e Fila */
/* Estrutura da Lista */
typedef struct {
   Pointer first, last;
} List;

/* Estrutura da Pilha */
typedef struct {
   Pointer bottom, top;
} Stack;

/* Estrutura da Fila */
typedef struct {
   Pointer begin, end;
} Row;

/* Operacoes que podem ser realizadas com as estruturas */

/* Operacoes sobre Listas */

/* Cria uma Lista vazia */
void createList ( List *list )
{
   /* Alocando espaco em memoria e atribuindo-o ao
         primeiro elemento da Lista.               */
   list -> first = ( Pointer ) malloc( sizeof( Cell ) );
   
   /* Fazendo que o ultimo elemento aponte para o
         mesmo local que o primeiro - Lista Vazia */
   list -> last = list -> first;
   
   /* Fazendo com que o proximo elemento apos o
         primeiro, seja o NULO.                 */
   list -> first -> next = NULL;
} /* createList */

/* Verifica se uma Lista estah vazia */
int emptyList ( List list )
{
   return ( list.first == list.last );
} /* emptyList */

/* Insere um elemento ao final da Lista */
int insert ( List *list, Item i )
{
   /* Alocando espaco em memoria e atribuindo-o ao
         proximo elemento apos o ultimo da Lista.  */
   list -> last -> next = ( Pointer ) malloc( sizeof( Cell ) );
   
   /* O ultimo item passa a ser aquele que foi criado */
   list -> last = list -> last -> next;
   
   /* O campo item da ultima celula recebe o
         item passado como parametro.        */
   list -> last -> item = i;
   
   /* O proximo elemento apos o ultimo eh NULO */
   list -> last -> next = NULL;
   
   /* Operacao realizada com exito */
   return 0;
} /* insert */

/* Remove um elemento da Lista - O item a ser removido
      eh o seguinte ao apontado pelo ponteiro p.       */
int delete ( List *list, Item *item, Pointer p )
{
   /* Verificando se a Lista estah vazia */
   if ( ( emptyList( *list ) ) || ( p == NULL ) ||
      ( p -> next == NULL ) )
      return 1; /* Lista vazia */
   
   else {
      /* A Lista nao estah vazia */
      
      /* Um ponteiro auxiliar que aponta para o
            proximo elemento a p.               */
      Pointer aux = p -> next;
      
      /* Pegando o item do elemento a ser excluido */
      *item = aux -> item;
      
      /* Ajustando o ponteiro da celula que p aponta */
      p -> next = aux -> next;
      
      /* Verificando se o elemento a ser excluido
            eh o ultimo da lista.                 */
      if ( p -> next == NULL )
         list -> last = p;
      
      /* Liberando espaco em memoria 
            - excluindo o item       */
      free( aux );
   } /* else */
   
   /* Operacao realizada com exito */
   return 0;
} /* remove */

/* Imprime na tela a Lista */
int printList ( List list )
{
   /* Verificando se a Lista estah vazia */
   if ( emptyList( list ) )
      return 1; /* Lista vazia */
   
   else {
      /* A Lista nao estah vazia */
      
      /* Um ponteiro auxiliar para varrer a Lista */
      Pointer aux = list.first -> next;
      
      /* Imprime enquanto nao chegar ao fim da Lista */
      while ( aux != NULL ) {
         /* Imprimindo... */
         printf( "%12d\n", aux -> item.value );
         
         /* Atualizando a variavel aux */
         aux = aux -> next;
      } /* while */
   } /* else */
   
   /* Operacao realizada com exito */
   return 0;
} /* printList */

/* Operacoes sobre Pilhas */

/* Cria uma Pilha vazia */
void createStack ( Stack *stack )
{
   /* Alocando espaco em memoria e atribuindo-o ao
         elemento do topo da Pilha.                */
   stack -> top = ( Pointer ) malloc( sizeof( Cell ) );
   
   /* Fazendo que o elemento do fundo aponte para o
         mesmo local que o do topo - Pilha Vazia    */
   stack -> bottom = stack -> top;
   
   /* Fazendo com que o proximo elemento apos o
         do topo, seja o NULO.                  */
   stack -> top -> next = NULL;
} /* createStack */

/* Verifica se uma pilha estah vazia */
int emptyStack ( Stack stack )
{
   return ( stack.top == stack.bottom );
} /* emptyStack */

/* Empilha um elemento no topo da pilha */
int pillUp ( Stack *stack, Item i )
{
   /* Definindo um ponteiro auxiliar e atribuindo
         a ele o endereco de memoria alocado.     */
   Pointer aux = ( Pointer ) malloc( sizeof( Cell ) );
   
   /* Adicionando o elemento no topo da pilha */
   stack -> top -> item = i;
   
   /* Fazendo com que o proximo elemento de aux
         aponte para o mesmo lugar que o topo.  */
   aux -> next = stack -> top;
   
   /* Fazendo com que aux seja o novo
         topo da pilha.               */
   stack -> top = aux;
   
   /* Operacao realizada com exito */
   return 0;
} /* pillUp */

/* Desempilha um elemento do topo da pilha */
int pillDown ( Stack *stack, Item *item )
{
   /* Verificando se a pilha estah vazia */
   if ( emptyStack( *stack ) )
      return 1; /* Pilha vazia */
   
   else {
      /* A pilha nao estah vazia */
      
      /* Definindo um ponteiro auxiliar e
            fazendo com que ele aponte
             para o topo da pilha.        */
      Pointer aux = stack -> top;
      
      /* Fazendo com que o topo da pilha seja
            o proximo item a aux.             */
      stack -> top = aux -> next;
      
      /* Atribuindo a item, o item que serah
            excluido.                        */
      *item = aux -> next -> item;
      
      /* Liberando espaco em memoria - excluindo */
      free( aux );
   } /* else */
   
   /* Operacao realizada com exito */
   return 0;
} /* pillDown */

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
int emptyRow ( Row row )
{
   return ( row.begin == row.end );
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
   if ( emptyRow( *row ) )
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


/*****************************************************************************************************/

/* Interfaces para teste... */

/* Lista, Pilha ou Fila??? */
int menuEstruturas ()
{
   int op = 0;
   
   do {
      printf( "\n\nEscolha a estrutura que deseja testar.\n" );
      printf( "1. Lista\n2. Pilha\n3. Fila\n4. Sair\n\n" );
      printf( "Escolha uma opção e tecle <ENTER>: " );
      scanf( "%d", &op );
      
      if ( ( op < 1 ) || ( op > 4 ) ) {
         printf( "\n\nERRO: Opção inválida. Tente novamente.%d", op );
         op = 0;
      }
   } while ( ( op < 1 ) || ( op > 4 ) );
   
   return op;
} /* menuEstruturas */

/* O que quer fazer? */
int menuAcoes ( int tipo )
{
   char est[ 30 ];
   int op = 0;
      
   switch ( tipo ) {
      case 1: strcpy( est, "Lista" );
              break;
      case 2: strcpy( est, "Pilha" );
              break;
      case 3: strcpy( est, "Fila" );
              break;
      default : strcpy( est, "" );
              break;
   } /* switch */
   
   do {
      printf( "\n\nPrograma-teste do tipo abstrato de dados %s.\n", est );
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

   int opcao = menuEstruturas(),
       op =0;
   
   List lista;
   Stack pilha;
   Row fila;
   
   /* Deseja sair? */
   if ( opcao == 4 ) exit( 0 );
   
   do {
      op = menuAcoes( opcao );
      
      switch ( op ) {
         case 1:
            switch ( opcao ) {
               case 1: createList( &lista );
                       break;
               case 2: createStack( &pilha );
                       break;
               case 3: createRow( &fila );
                       break;
               default: break;
            }
            break;
         case 2:
            switch ( opcao ) {
               case 1: if ( emptyList( lista ) )
                          printf( "\n\n\nLista VAZIA.\n\n\n" );
                       else
                          printf( "\n\n\nLista NÃO vazia.\n\n\n" );
                       break;
               case 2: if ( emptyStack( pilha ) )
                          printf( "\n\n\nPilha VAZIA.\n\n\n" );
                       else
                          printf( "\n\n\nPilha NÃO vazia.\n\n\n" );
                       break;
               case 3: if ( emptyRow( fila ) )
                          printf( "\n\n\nFila VAZIA.\n\n\n" );
                       else
                          printf( "\n\n\nFila NÃO vazia.\n\n\n" );
                       break;
               default: break;
            }
            break;
         case 3:
            i = entrada();
            insert( &lista, i );
            break;
         case 4:
            break;
         case 5:
            if ( printList( lista ) )
               printf( "\nERRO: Lista vazia.\n" );
            else
               printf( "\nFim da impressão.\n" );
            break;
         case 6:
            break;
         default:
            break;
      } /* switch */
   } while ( op != 6);
} /* main */
