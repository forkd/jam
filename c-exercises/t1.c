#include "graph.h"
#include "conio.h"
#include "stdio.h"

main () {
   _setvideomode( _VRES16COLOR );

   _settextcolor( 4 );
   _outtext( "Isto estah em vermelho\n" );
   _getche();

   _setvideomode( _DEFAULTMODE );
}
