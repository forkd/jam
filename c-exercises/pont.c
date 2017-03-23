struct tItem {
   char nomeItem[ 40 ];
   unsigned int posicao;
}

struct tCelula {
   struct tItem valor;
   struct tCelula *proximo;
}

struct tLista {
   struct tCelula *primeiro;
   struct tCelula *ultimo;
}

void criaLista ( struct tLista l ) {
   if ( ! ( l.primeiro = malloc( sizeof( struct tCelula ) ) ) ) {
      printf( "ERRO na alocacao de memoria.\n" );
      exit( 1 );
   }

   l.*primeiro.*proximo = '\0';
   l.*primeiro.valor.nome = "\0";
   l.*primeiro.valor.posicao = 0;

   l.ultimo = l.primeiro;
}

main {
   struct tLista lista;

   criaLista( lista );
}
