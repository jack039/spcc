%{
#include <stdio.h>
int characters = 0;
int words = 0;
int sentences = 0;
int lines = 0;
int tabs = 0;
int numbers = 0;
int blanks = 0;
%}
%%
[0-9]+ { numbers++; characters += yyleng; }
[a-zA-Z]+ { words++; characters += yyleng; }
[.]|[?]|[!] { sentences++; characters++; }
\n { lines++; characters++; }
\t { tabs++; characters++; }
" " { blanks++; characters++; }
. { characters++; }
%%
int yywrap()
{
 return 1;
}
int main()
{
 printf("Enter the text (Press Ctrl+D to end input):\n");
 yylex();
 printf("\nNumber of Characters : %d\n", characters);
 printf("Number of Words : %d\n", words);
 printf("Number of Sentences : %d\n", sentences);
 printf("Number of Lines : %d\n", lines);
 printf("Number of Tabs : %d\n", tabs);
 printf("Number of Numbers : %d\n", numbers);
 printf("Number of BlankSpaces: %d\n", blanks);
 return 0;
}
// lex lex.l
//gcc lex.yy.c -o lex -ll
//./lex