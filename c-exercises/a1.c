#include "stdio.h"
#include "stdlib.h"

main ( int argc, char *argv[] ) {
   FILE *fp;
   char ch;
   
   if ( argc != 2 ) {
      printf( "Falta um parametro.\n" );
      exit( 1 );
   }
   
   if ( ( fp = fopen( *( argv + 1 ), "r" ) ) == NULL ) {
      printf( "O arquivo nao pode ser aberto.\n" );
      exit( 1 );
   }
   
   ch = getc( fp );
   
   while ( ch != 13 ) {
      putchar( ch );
      ch = getc( fp );
   }
}
