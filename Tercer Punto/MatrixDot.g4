grammar MatrixDot;

// Parser rules
program     : stmt* EOF ;
stmt        : expr ';' ;
expr        : dotExpr
            | matrixLiteral
            | NUMBER
            ;

dotExpr     : DOT '(' expr ',' expr ')' ;
matrixLiteral
            : '[' rowList ']' ;
rowList     : row (',' row)* ;
row         : '[' numList? ']' ;
numList     : signedNumber (',' signedNumber)* ;

signedNumber
            : NUMBER
            ;

// Lexer rules
DOT         : 'dot' ;
NUMBER      : '-'? DIGIT+ ('.' DIGIT+)? ;
WS          : [ \t\r\n]+ -> skip ;
LBRACK      : '[' ;
RBRACK      : ']' ;
COMMA       : ',' ;
SEMI        : ';' ;

// fragments
fragment DIGIT : [0-9] ;
