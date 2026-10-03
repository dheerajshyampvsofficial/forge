parser grammar fds_parser;

options {
	tokenVocab = fds_lexer;
}

start: (statements += simple_stmt)* EOF # Statements;

simple_stmt: (expression = expr | assign = assignment) SEMI_COLON # SimpleStatement;

expr: ternary_expr # Expression;

ternary_expr:
	left = binary_expr (
		QMARK middle = ternary_expr COLON right = ternary_expr
	)? # TernaryExpression;

binary_expr: addition # BinaryExpression;

addition:
	left = multiplication (
		ops += (PLUS | MINUS) rights += multiplication
	)* # AddExpression;

multiplication:
	left = unary_sign (
		ops += (STAR | SLASH) rights += unary_sign
	)* # MulExpression;

unary_sign:
	sign = (PLUS | MINUS) operand = unary_sign	# UnarySign
	| op = (INC | DEC) variable = VAR			# PreIncDec
	| variable = VAR op = (INC | DEC)			# PostIncDec
	| value = matrix							# UnaryValue;

matrix:
	MLBRACE rows = matrix_rows MRBRACE	# MatrixLiteral
	| atom								# AtomLiteral;

// The whole literal: block rows, cut by ---
matrix_rows:
	groups += block_row (M_HSEP groups += block_row)* # MatrixRows;

// One block row: the text lines between two --- separators
block_row:
	lines += matrix_row (NL lines += matrix_row)* # BlockRow;

// One text line, cut into cells by |
matrix_row:
	cells += matrix_cell (M_VBAR cells += matrix_cell)* # MatrixRow;

// The part of one line that belongs to one block
matrix_cell: elements += expr+ # MatrixCell;

atom:
	number = NUMBER			# NumberLiteral // renamed: T_NUMBER -> NUMBER
	| variable = VAR		# VarLiteral // renamed: T_VAR -> VAR
	| LPAREN expr RPAREN	# ParenLiteral;

assignment: variable = VAR EQUALS value = expr # AssignmentStmt;