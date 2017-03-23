/* verNumero ****************************************************************/
/* DESCRICAO                                                                */
/*    Funcao que verifica a validade de um numero mediante a sua base.      */
/*                                                                          */
/* ENTRADA                                                                  */
/*  > char *numero : O numero a ser avalidado.                              */
/*  > char base : A base em que o numero deve estar.                        */
/*                                                                          */
/* RETORNO                                                                  */
/*    Retorna 1 caso o numero esteja dentro do padrao esperado ou 0 em caso */
/* contrario.                                                               */
/****************************************************************************/
char verNumero ( char *numero, char base ) {
   register char i; /* Variavel de controle da iteracao */
   
   for ( i = 0; i < strlen( numero ); i++ ) {
      if ( isalpha( *( numero + i ) ) ) { /* Tratando letras */
         if ( ( *( numero + i ) - 55 ) >= base )
	    return 0;
      }
      else if ( isdigit( *( numero + i ) ) ) { /* Tratando digitos */
         if ( ( *( numero + i ) - 48 >= base ) )
	    return 0;
      }
      else /* Nao eh digito nem letra. */
         return 0;
   } /* for */
   
   return 1;
}

/* ctoi *********************************************************************/
/* DESCRICAO                                                                */
/*    Funcao que retorna o valor inteiro de um digito a partir de sua repre-*/
/* sentacao em caracter.                                                    */
/*                                                                          */
/* ENTRADA                                                                  */
/*  > char ch : Caracter que sera convertido.                               */
/*                                                                          */
/* RETORNO                                                                  */
/*    Retorna a representacao em inteiro do caracter. Caso o parametro pas- */
/* sado nao seja um digito, o valor retornado eh indefinido.                */
/****************************************************************************/
char ctoi ( char ch ) {
   return ( ch - 48 );
}

/* potencia *****************************************************************/
/* DESCRICAO                                                                */
/*    Funcao que retorna a potencia de um numero.                           */
/*                                                                          */
/* ENTRADA                                                                  */
/*  > unsigned char base : O numero que representa a base na exponenciacao. */
/*  > unsigned int expoente : O expoente da operacao.                       */
/*                                                                          */
/* RETORNO                                                                  */
/*    Retorna o numero que representa "BASE elevadada ao EXPOENTE".         */
/****************************************************************************/
unsigned long int potencia ( unsigned char base, unsigned int expoente ) {
   register unsigned long int aux = 1;

   if ( ! expoente )
      return 1;
   else
      for ( ; expoente > 0; expoente-- )
         aux *= base;

   return aux;
}

/* decPara ******************************************************************/
/* DESCRICAO                                                                */
/*    Funcao que converte um numero na base 10 para sua representacao numa  */
/* base qualquer definida por base.                                         */
/*                                                                          */
/* ENTRADA                                                                  */
/*  > const char *num : O numero a ser convertido.                          */
/*  > char *res : O numero final (convertido).                              */
/*  > const unsigned char base : A base em que o numero final deve estar.   */
/*                                                                          */
/* RETORNO                                                                  */
/*    Retorna em *res o numero na base desejada.                            */
/****************************************************************************/
void decPara ( const char *num, char *res, const unsigned char base ) {
   register unsigned long int n = atol( num );

   char aux[ 256 ];

   strcpy( res, "\0" ); /* Limpando o resultado */

   while ( n >= base ) {
      strcpy( aux, res );
      
      if ( ( n % base ) > 9 )
         sprintf( res, "%c" "%s", ( 55 + ( n % base ) ), aux );
      else
         sprintf( res, "%d" "%s", ( n % base ), aux );

      n /= base;
   }

   strcpy( aux, res );
   
   if ( ( n % base ) > 9 )
      sprintf( res, "%c" "%s", ( 55 + ( n % base ) ), aux );
   else
      sprintf( res, "%d" "%s", ( n % base ), aux );
}

/* paraDec ******************************************************************/
/* DESCRICAO                                                                */
/*    Funcao que converte um numero numa base qualquer definida em base pa- */
/* ra sua representacao na base 10.                                         */
/*                                                                          */
/* ENTRADA                                                                  */
/*  > const char *num : O numero a ser convertido.                          */
/*  > char *res : O numero final (convertido).                              */
/*  > const unsigned char base : A base em que o numero se encontra.        */
/*                                                                          */
/* RETORNO                                                                  */
/*    Retorna em *res o numero na base decimal.                             */
/****************************************************************************/
void paraDec ( const char *num, char *res, const unsigned char base ) {
   register char pos, exp;
   register unsigned long int n = 0;

   strcpy( res, "\0" ); /* Limpando o resultado */

   for ( pos = strlen( num ) - 1, exp = 0; pos >= 0; pos--, exp++ )
      if ( ! isdigit( *( num + pos ) ) )
         n += potencia( base, exp ) * ( *( num + pos ) - 55 );
      else
         n += potencia( base, exp ) * ctoi( *( num + pos ) );

   sprintf( res, "%d", n );
}
