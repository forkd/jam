/* cb.c *********************************************************************/
/*                                                                          */
/* DESCRICAO                                                                */
/*    O programa CB (Conversor de Bases) tem como funcao fazer a conversao  */
/* de base de um numero.                                                    */
/*                                                                          */
/* INFORMACOES                                                              */
/*    AUTOR : Jose Lopes de Oliveira Junior                                 */
/*    SISTEMA OPERACIONAL : Slackware Linux 10.1 ( kernel 2.4.29 )          */
/*    COMPILADOR : GCC 3.3.4 ( GNU COMPILER C )                             */
/*    DATA : ago/2005                                                       */
/*    CONTATO : jlojunior@gmail.com                                         */
/*                                                                          */
/****************************************************************************/

/* Bibliotecas importadas */
#include "libcb.h"

/* main *********************************************************************/
/* DESCRICAO                                                                */
/*    Funcao principal do programa. Nela sao verificados os parametros pas- */
/* sados e sao feitas as chamadas as funcoes das bibliotecas do programa de */
/* modo a processar e mostrar ao usuario o resultado de sua requisicao.     */
/*                                                                          */
/* ENTRADA                                                                  */
/*  > int argc     : O contador de argumentos.                              */
/*  > char *argv[] : A matriz que armazena todos os argumentos.             */
/****************************************************************************/
main ( int argc, char *argv[] ) {
   /* Verificando a quantidade de parametros passados */
   if ( argc < 2 ) {
      printf( "CB : Falta um parametro.\n" );
      printf( "\tDigite \"cb --ajuda\" para obter ajuda.\n" );
      
      exit( 1 );
   }
   
   if ( argc > 4 ) {
      printf( "CB : Excesso de parametros.\n" );
      printf( "\tDigite \"cb --ajuda\" para obter ajuda.\n" );
      
      exit( 1 );
   }
   
   /* Numero de parametros OK - Verifica se o parametro */
   /* passado eh um parametro especial.                 */
   /* Impressao da ajuda do programa */
   if ( ( ! strcmp( *( argv + 1 ), "--ajuda" ) ) || 
      ( ! strcmp( *( argv + 1 ), "-a" ) ) ) {
      printf( "Uso: dip NUMERO_IP/MASCARA\n" );
      printf( "\tonde: NUMERO_IP eh um numero IP valido e\n" );
      printf( "\t   MASCARA eh uma mascara de IP valida.\n" );
      printf( "ou   dip [opcoes]\n" );
      printf( "Gera e mostra informacoes acerca de um numero IP.\n" );
      printf( "opcoes:\n" );
      printf( "\t--ajuda, -a     Mostra esta ajuda e sai.\n" );
      printf( "\t--versao, -v    Mostra as notas da versao e sai.\n" );
      
      exit( 0 );
   }
   
   /* Impressao das notas da versao do programa */
   if ( ( ! strcmp( *( argv + 1 ), "--versao" ) ) || 
      ( ! strcmp( *( argv + 1 ), "-v" ) ) ) {
      printf( "\tCB ( Conversor de Bases ) 0.5   :)\n" );
      printf( "Escrito por Jose Lopes de Oliveira Júnior. " );
      printf( "<jlojunior@gmail.com>\n\n" );
      printf( "Copyright (C) 2005.\n" );
      
      printf( "\tEste programa é um software de livre distribuição, que pode\n" ); 
      printf( "ser copiado e distribuído sob os termos da Licença Geral\n" );
      printf( "GNU, conforme publicada pela Free Software Foundation,\n" );
      printf( "versão 2 da licença, ou (a critério do autor) qualquer versão\n" );
      printf( "posterior.\n" );
      printf( "\tEste programa é distribuído na expectativa de ser útil aos\n" );
      printf( "seus usuários, porém NÃO POSSUI NENHUMA GARANTIA, EXPLÍCITA OU\n" );
      printf( "IMPLÍCITA, COMERCIAL OU DE ATENDIMENTO A UMA DETERMINADA\n" );
      printf( "FINALIDADE. Consulte a Licença Pública Geral GNU.\n" );
      
      exit( 0 );
   }
   
   /* Numero de parametros OK e os parametros passados nao sao */
   /* especiais. Aqui realiza-se o tratamento disso.           */
   
   /* Somente um parametro passado */
   if ( argc == 2 ) {
      if ( verNumero( *( argv + 1 ), 10 ) ) {
         char resultado[ 256 ];
	 
         decPara( *( argv + 1 ), resultado, 2 );
	 
	 printf( "CB : ( %s )10 == ( %s )2\n", *( argv + 1 ), resultado );
	 
	 exit( 0 );
      }
      else {
         printf( "CB : Numero invalido para a base especificada.\n" );
	 
	 printf( "\tDigite \"cb --ajuda\" para obter ajuda.\n" );
      
         exit( 1 );
      }
   }
   
   /* Todos os parametros passados */
   if ( argc == 4 ) {
      char baseEntrada = atoi( *( argv + 1 ) ), 
         baseSaida = atoi( *( argv + 2 ) );
      
      if ( ( baseEntrada < 2 ) && ( baseEntrada > 36 ) ) {
         printf( "CB : Base de entrada invalida.\n" );
	 
	 printf( "\tDigite \"cb --ajuda\" para obter ajuda.\n" );
      
         exit( 1 );
      }
      
      if ( ( baseSaida < 2 ) && ( baseSaida > 36 ) ) {
         printf( "CB : Base de saida invalida.\n" );
	 
	 printf( "\tDigite \"cb --ajuda\" para obter ajuda.\n" );
      
         exit( 1 );
      }
      
      if ( verNumero( *( argv + 1 ), baseEntrada ) ) {
         char resultado[ 256 ];
	 
	 if ( baseEntrada == baseSaida )
	    strcpy( resultado, *( argv + 3 ) );
	 else if ( baseEntrada == 10 )
	    decPara( *( argv + 3 ), resultado, baseSaida );
	 else if ( baseSaida == 10 )
	    paraDec( *( argv + 3 ), resultado, baseEntrada );
	 else {
	    char auxiliar[ 256 ];
	    
	    paraDec( *( argv + 3 ), auxiliar, baseEntrada );
	    
	    decPara( auxiliar, resultado, baseSaida );
	 }
	 
	 printf( "CB : ( %s )%d == ( %s )%d\n", *( argv + 1 ), baseEntrada,
	    resultado, baseSaida );
      }
      else {
         printf( "CB : Numero invalido para a base especificada.\n" );
	 
	 printf( "\tDigite \"cb --ajuda\" para obter ajuda.\n" );
      
         exit( 1 );
      }
   }
}
