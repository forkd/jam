#include "stdio.h"
#include "stdlib.h"
#include "string.h"

main ( int argc, char *argv[] ) {
   char str[80];
   FILE *fp;
   
   if ( argc != 2 ) {
      printf( "Num. Param. Inv." );
      exit( 1 );
   }
   
   if ( ( fp = fopen( *( argv + 1 ), "r" ) ) == NULL ) {
      printf( "O arquivo nao pode ser aberto." );
      exit( 1 );
   }
   
   while ( ! feof( fp ) ) {
      fgets( str, 79, fp );
      printf( str );
      getch();
   }
}   
