void concat ( char *str, char ch ) {
   register int i = strlen( str ); /* Armazena o tamanho atual da String */
   
   *( str + i ) = ch; /* Adicionando o caractere no fim da String */
   *( str + ( i + 1 ) ) = '\0'; /* Marcando o novo final da String */
} /* concat */

main ( int argc, char *argv[] )
{
   char str[ 50 ], c;
   
   strcpy( str, "Teste" );
   
   concat( str, '1' );
   concat( str, '2' );
   concat( str, '3' );
   concat( str, '.' );
   concat( str, '.' );
   concat( str, '.' );
   
   printf( "\n\nSTRING: %s\n\n", str );
} /* main */
