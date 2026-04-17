%{
#include<stdio.h>
#include<stdlib.h>
void yyerror(const char *s);
int yylex();
%}
%token NUMBER
%%
E : E '+' E
 | E '-' E
 | E '*' E
 | E '/' E
 | '(' E ')'
 | NUMBER
 ;
%%
int main()
{
 printf("Enter arithmetic expression:\n");
 yyparse();
 printf("Valid Expression\n");
 return 0;
}
void yyerror(const char *s)
{
 printf("Invalid Expression\n");
 exit(0); }