typedef struct {
   int row, column;
} Position;

typedef struct {
   char token[ 100 ], /* O token encontrado */
        class[ 100 ], /* A classe do token */
        value[ 100 ]; /* O valor do token na tabela de simbolos */
   Position position; /* As coordenadas de localizacao do token no codigo */
} Token;

main ()
{
   Token token;
   
   strcpy( token.token, "if" );
   strcpy( token.class, "comando de seleção" );
   strcpy( token.value, "-" );
   token.position.row = 1;
   token.position.column = 1;
   
   printf( "%s", token.token );
} /* main */
