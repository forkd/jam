void toLowerCase ( char *str1, char *str2 )
{
   int i = 0;
   
   *( str2 + 0 ) = '\0';
   
   for (; i < strlen( str1 ); i++ )
      *( str2 + i ) = tolower( *( str1 + i ) );
   
   *( str2 + i ) = '\0';
} /* toLowerCase */

main ( int argc, char *argv[] )
{
   char s2[ 100 ] = "\0";
   
   toLowerCase( *( argv + 1 ), s2 );
   printf( "\n\n%s == %s\n\n", *( argv + 1 ), s2 );
   
   exit( 0 );
} /* main */
