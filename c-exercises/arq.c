#include "stdio.h"
#include "stdlib.h"

main ( int argc, char *argv[] ) {
   FILE *fp;
   char ch;
   
   if ( argc != 2 ) {
      printf( "Num. param. inv.\n" );
      exit( 1 );
   }
   
   if ( ( fp = fopen( argv[ 1 ], "w" ) ) == NULL ) {
      printf( "O arquivo nao pode ser aberto.\n" );
      exit( 1 );
   }
   
   do {
      ch = getchar();
      fputc( ch, fp );
   } while ( ch != '$' );
   
   fclose( fp );
}
