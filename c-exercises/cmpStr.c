int cmpStr ( char *str1, char *str2 )
{
   int resultado = strcmp( str1, str2 );
   
   if ( ! resultado )
      return 0; /* str1 == str2 */
   
   else if ( resultado < 0 ) {
      int i = 0; /* Para varrer a string */
      
      for (; i < strlen( str1 ); i++ ) {
         if ( *( str1 + i ) < *( str2 + i ) )
            return -1; /* str1 < str2 */
         else if ( *( str1 + i ) > *( str2 + i ) )
            return 1; /* str1 > str2 */
      }
      
      return -1; /* str1 < str2 */
   }
   
   else {
      int i = 0; /* Para varrer a string */
      
      for (; i < strlen( str2 ); i++ ) {
         if ( *( str1 + i ) < *( str2 + i ) )
            return -1; /* str1 < str2 */
         else if ( *( str1 + i ) > *( str2 + i ) )
            return 1; /* str1 > str2 */
      }
      
      return 1; /* str1 < str2 */
   }
} /* cmpStr */

main ( int argc, char *argv[] )
{
   int ver = cmpStr( *( argv + 1 ), *( argv + 2 ) );
   
   if ( ver < 0 ) {
      printf( "\n\nO parâmetro 1 vem antes do 2: %s, %s.\n\n", *( argv + 1 ), *( argv + 2 ) );
   }
   else if ( ver > 0 ) {
      printf( "\n\nO parâmetro 2 vem antes do 1: %s, %s.\n\n", *( argv + 2 ), *( argv + 1 ) );
   }
   else {
      printf( "\n\nO parâmetro 1 é igual ao 2: %s, %s.\n\n", *( argv + 1 ), *( argv + 2 ) );
   }
   
   exit( 0 );
} /* main */
