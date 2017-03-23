#include <stdio.h>

int main ( int argc, char *argv[] )
{
   FILE *arquivo;
	
   if ( ( arquivo = fopen( *( argv + 1 ), "r" ) ) == NULL ) {
      printf("ERRO: O arquivo não pôde ser aberto.\n");
      exit( 1 );
   } /* if */
   else {
      char linha[ 200 ];
      int i;
      
      while ( ! feof( arquivo ) ) {
         fgets( linha, 190, arquivo );
   
         for ( i = strlen( linha ); i >= 0; i-- ) {
	    if ( *( linha + i ) )
            printf( "%c", *( linha + i ) );
         } /* for */
      } /* while */
   } /* else */
   
   exit ( 0 );
   
} /* main() */
