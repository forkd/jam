#include <stdio.h>

 main ( int argc, char *argv[] ) {
   char op;

   if ( argc !=2 ) {
      printf( "ERRO : Falta um parametro." );
      exit( 1 );
   }

   printf( "\nDeseja apagar o arquivo \'%s\' [S/N]?", *( argv + 1 ) );
   op = getch();

   if ( toupper( op ) == 'S' ) {                          
      if ( remove( *( argv +1 ) ) ) {
            printf( "\nERRO : O arquivo nao pode ser apagado.\n" );
            exit( 1 );
      }

      printf( "\nArquivo apagado com sucesso.\n" );
      exit( 0 );
   }

   printf( "Arquivo nao apagado.\n" );
   exit( 0 );
}
