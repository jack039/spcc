%{
#include "y.tab.h"
%}
%%
[0-9]+ { return NUMBER; }
[\t ] ;
\n { return 0; }
. { return yytext[0]; }
%%
int yywrap()
{
 return 1;
}
//yacc -d expr.y
//lex expr.l
//gcc lex.yy.c y.tab.c -o parser
//./parser
