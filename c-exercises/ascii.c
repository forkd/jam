#include "stdio.h"

main () {
   register unsigned char c;

   for ( c = 1; c <= 254; c++ )
      printf( "%6d - %c", c, c );

   exit( 0 );
}
