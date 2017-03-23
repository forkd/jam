char ctoi ( char ch ) {
   return ( ch - 48 );
}

main () {
   char nCh,i=0,
      nStr[23] = "0123456789ab";
   
   while ( i < strlen( nStr ) ) {
      nCh = ctoi( *(nStr+i) );
      printf( "%d == %c\n", nCh, *(nStr+i) );
      ++i;
   }
}
