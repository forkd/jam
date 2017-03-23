/* Metodos de ordenacao interna */

typedef struct {
   Chave chave;
   /* outros componentes */
} Item;

typedef Item Vetor[ n + 1 ];

Vetor a;

void selectionSort ( Vetor a )
{
   Indice i, j, min;
   Item x;
   
   for ( i = 1; i < n; i++ ) {
      min = i;
      
      for ( j = i + 1; j <= n; j++ )
         if ( a[ j ].chave < a[ min ].chave )
            min = j;
      
      x = a[ min ];
      a[ min ] = a[ i ];
      a[ i ] = x;
   }
} /* selectionSort */

void insertionSort ( Vetor a )
{
   Indice i, j;
   Item x;
   
   for ( i = 2; i <= n; i++ ) {
      x = a[ i ];
      j = i - 1;
      a[ 0 ] = x; /* sentinela */
      
      while ( x.chave < a[ j ]. chave ) {
         a[ j + 1 ] = a[ j ];
         j--;
      }
      
      a[ j + 1 ] = x;
   }
} /* insertionSort */

void shellSort ( Vetor a )
{
   int i, j, h;
   Item x;
   h = 1;
   
   do {
      h = h * 3 + 1;
   } while( h <= n );
   
   do {
      h /= 3;
      
      for ( i = h + 1; i <= n; i++ ) {
         x = a[ i ];
         j = i;
         
         while ( a[ j - h ].chave > x.chave ) {
            a[ j ] = a[ j - h ];
            j -= h;
            
            if ( j <= h )
               goto LABEL;
         }
         
         LABEL:
            a[ j ] = x;
      }
   } while( h != 1 );
} /* shellSort */

/* QUICKSORT */
void particao ( Vetor a, Indice esq, Indice dir, Indice *i, Indice *j )
{
   Item x, w;
   
   *i = esq;
   *j = dir;
   
   x = a[ ( *i + *j ) / 2 ]; /* obtem o pivo x */
   
   do {
      while ( a[ *i ].chave < x.chave )
         ( *i )++;
      
      while ( a[ *j ].chave < x.chave )
         ( *j )--;
      
      if ( *i <= *j ) {
         w = a[ *i ];
         a[ *i ] = a[ *j ];
         a[ *j ] = w;
         ( *i )++;
         ( *j )--;
      }
   } while ( *i <= *j );
} /* particao */

void ordena ( Vetor a, Indice esq, Indice dir )
{
   Indice i, j;
   
   particao( a, esq, dir, &i, &j );
   
   if ( esq < j )
      ordena( a, esq, j );
   
   if ( i < dir )
      ordena( a, i, dir );
} /* ordena */

void quickSort ( Vetor a )
{
   ordena( a, 1, n );
} /* quickSort */

/* HEAPSORT */
void refaz ( Indice esq, Indice dir, Vetor a )
{
   Indice i;
   int j;
   Item x;
   
   i = esq;
   j = i * 2;
   x = a[ i ];
   
   while ( j <= dir ) {
      if ( j < dir )
         if ( a[ j ].chave < a[ j + 1 ].chave )
            j++;
      
      if ( x.chave >= a[ j ].chave )
         goto LABEL;
      
      a[ i ] = a[ j ];
      i = j;
      j = i * 2;
   } /* while */
   
   LABEL:
      a[ i ] = x;
} /* refaz */

void constroi ( Vetor a )
{
   Indice esq;
   
   esq = n / 2 + 1;
   
   while ( esq > 1 ) {
      esq--;
      refaz( esq, n, a );
   }
} /* constroi */

void heapSort ( Vetor a )
{
   Indice esq, dir;
   Item x;
   
   /* Constroi o heap */
   esq = n / 2 + 1;
   dir = n;
   
   while ( esq > 1 ) {
      esq--;
      refaz( esq, dir, a );
   }
   
   /* Ordena o vetor */
   while ( dir > 1 ) {
      x = a[ 1 ];
      a[ 1 ]= a[ dir ];
      a[ dir ] = x;
      dir--;
      refaz( esq, dir, a );
   }
} /* heapSort */