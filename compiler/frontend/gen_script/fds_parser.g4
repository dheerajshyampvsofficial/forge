parser grammar fds_parser;

options {
	tokenVocab = fds_lexer;
}

start: (parts += part)* EOF # Parts;

part:
	FDS_BLOCK_OPEN NEWLINE* (body += part)* FDS_BLOCK_CLOSE	# FdsBlock
	| FDS_INLINE_OPEN NL* value = expr NL* FDS_INLINE_CLOSE	# FdsInline
	| FRGN_BLOCK_OPEN (body += part)* FRGN_BLOCK_CLOSE		# FrgnBlock
	| FRGN_INLINE_OPEN (body += part)* FRGN_INLINE_CLOSE	# FrgnInline
	| FRGN_CODE+											# FrgnText
	| simple_stmt											# Stmt;

simple_stmt: (expression = expr | assign = assignment) (
		SEMI_COLON
		| NEWLINE
	)* # SimpleStatement;

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
	MLBRACE matrix_inner_ignores* rows = matrix_rows matrix_inner_ignores* MRBRACE	# MatrixLiteral
	| atom																			# AtomLiteral;

// The whole literal: block rows, cut by ---
matrix_rows:
	groups += block_row (M_HSEP groups += block_row)* # MatrixRows;

// One block row: the text lines between two --- separators
block_row:
	lines += matrix_row ((NL | SEMI_COLON)+ lines += matrix_row)* # BlockRow;

// One text line, cut into cells by |
matrix_row:
	cells += matrix_cell (M_VBAR cells += matrix_cell)* # MatrixRow;

// The part of one line that belongs to one block
matrix_cell: elements += expr+ # MatrixCell;

// What to ignore inside matrix
matrix_inner_ignores: NL;

atom:
	number = NUMBER			# NumberLiteral
	| variable = VAR		# VarLiteral
	| LPAREN expr RPAREN	# ParenLiteral;

assignment: (targets += VAR EQUALS)+ value = expr # AssignmentStmt;
