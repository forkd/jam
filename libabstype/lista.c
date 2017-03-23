/* Programa de teste para os tipos abstratos de dados Lista, Pilha e Fila,
      Através da implementação por ponteiros.
   Autor: José Lopes de Oliveira Júnior                                    */

#include <stdlib.h>

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
int emptyList ( List *list )
{
   return ( list -> first == list -> last );
} /* emptyList */

Pointer first ( List *list, Item *item )
{
   /* Verificando se a lista estah vazia */
   if ( emptyList( list ) )
      /* Lista vazia - retorna um ponteiro nulo */
      return NULL;
   
   /* A lista NAO estah vazia */
   else {
      *item = list -> first -> next -> item; /* Pegando o conteudo do item */
      return ( list -> first -> next ); /* Retornando o ponteiro */
   } /* else */
   /* Pegando o conteudo do item */
} /* first */

/* Insere um elemento ao final da Lista */
int insert ( List *list, Item *i )
{
   /* Alocando espaco em memoria e atribuindo-o ao
         proximo elemento apos o ultimo da Lista.  */
   list -> last -> next = ( Pointer ) malloc( sizeof( Cell ) );
   
   /* O ultimo item passa a ser aquele que foi criado */
   list -> last = list -> last -> next;
   
   /* O campo item da ultima celula recebe o
         item passado como parametro.        */
   list -> last -> item = *i;
   
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
   if ( ( emptyList( list ) ) || ( p == NULL ) ||
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
int printList ( List *list )
{
   /* Verificando se a Lista estah vazia */
   if ( emptyList( list ) )
      return 1; /* Lista vazia */
   
   else {
      /* A Lista nao estah vazia */
      
      /* Um ponteiro auxiliar para varrer a Lista */
      Pointer aux = list -> first -> next;
      
      /* Imprime enquanto nao chegar ao fim da Lista */
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
   
   Pointer aux;
   
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
            insert( &lista, &i );
            
            aux = first( &lista, &i );
            
            printf( "\n\nPrimeiro elemento: %s\n\n", aux -> item.token );
            
            printf( "\n\nPrimeiro item: %s\n\n", i.token );
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
