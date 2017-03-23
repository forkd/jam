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

/* Estrutura da Pilha */
typedef struct {
   Pointer bottom, top;
} Stack;

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
int emptyStack ( Stack *stack )
{
   return ( stack -> top == stack -> bottom );
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
   if ( emptyStack( stack ) )
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

/* Imprime na tela a Pilha */
int printStack ( Stack *stack )
{
   /* Verificando se a Pilha estah vazia */
   if ( emptyStack( stack ) )
      return 1; /* Pilha vazia */
   
   else {
      /* A Pilha nao estah vazia */
      
      /* Um ponteiro auxiliar para varrer a Pilha */
      Pointer aux = stack -> top -> next;
      
      /* Imprime enquanto nao chegar ao fim da Pilha */
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
      printf( "\n\nPrograma-teste do tipo abstrato de dados Pilha.\n" );
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
   
   Stack pilha;
   
   do {
      op = menuAcoes();
      
      switch ( op ) {
         case 1:
            createStack( &pilha );
            printf( "\nPilha criada!" );
            break;
         
         case 2:
            if ( emptyStack( &pilha ) )
               printf("\033[;34;1m\n\nPilha VAZIA.\n\n\033[m");
            else
               printf("\033[;34;1m\n\nPilha NÃO vazia.\n\n\033[m");
            break;
            
         case 3:
            i = entrada();
            pillUp( &pilha, i );
            break;
         
         case 4:
            pillDown( &pilha, &i );
            
            break;
         
         case 5:
            printf("\033[;34;1m\nInício da impressão.\n\033[m");
            
            if ( printStack( &pilha ) )
               printf( "\nERRO: Pilha vazia.\n" );
            
            printf("\033[;34;1m\nFim da impressão.\n\033[m");
            break;
         
         case 6:
            break;
         
         default:
            break;
      } /* switch */
   } while ( op != 6);
} /* main */
