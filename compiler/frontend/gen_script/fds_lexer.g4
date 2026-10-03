lexer grammar fds_lexer;

tokens {
	NEWLINE,
	NL
}

@lexer::members {
# Delimeter stack
@property
def depthDelimeter(self):
  if not hasattr(self, '_depthDelimeter'):
    self._depthDelimeter = []
  return self._depthDelimeter

# Delimeter length
@property
def depthLevel(self):
  return len(self.depthDelimeter)

# 'MLBRACE' handler code
def handle_mlbrace_delimeter(self):
  self.depthDelimeter.append(f'#\x5B')

# 'MRBRACE' handler code
def handle_mrbrace_delimeter(self):
  if not self.depthDelimeter:
    raise Exception(
      f"Unmatched '\x5D#' found in line {self.line}."
    )

  delimiter = self.depthDelimeter.pop()

  if delimiter != f'#\x5B':
    raise Exception(
      f"Closing '\x5D#' does not match '{delimiter}' in line {self.line}."
    )

# 'LPAREN' handler code
def handle_lparen_delimeter(self):
  self.depthDelimeter.append('\x28')

# 'RPAREN' handler code
def handle_rparen_delimeter(self):
  if not self.depthDelimeter:
    raise Exception(
      f"Unmatched '\x29' found in line {self.line}."
    )

  delimiter = self.depthDelimeter.pop()

  if delimiter != '\x28':
    raise Exception(
      f"Closing '\x29' does not match '{delimiter}' in line {self.line}."
    )

# 'RBRACE' handler code
def handle_rbrace_delimeter(self, expected_delimeter: str = "%\x7B"):
  if (not self.depthDelimeter) or (not expected_delimeter):
    raise Exception(
      f"Unmatched '\x7D' at end of input"
    )
  
  delimiter = self.depthDelimeter.pop()
  
  if delimiter != expected_delimeter:
    raise Exception(
      f"Closing '\x7D' does not match '{expected_delimeter}' in line {self.line}."
    )
}

/*
 * Fragments (building blocks, never emitted)
 */

fragment DIGIT: [0-9];
fragment RBRACE: '}';

FDS_BLOCK_OPEN:
	'%%' {
    self.depthDelimeter.append('%%')
  } -> pushMode(fds);

FDS_INLINE_OPEN:
	'%{' {
    self.depthDelimeter.append('%\x7B')
  } -> pushMode(fds);

FRGN_BLOCK_CLOSE: '$$' -> popMode;

FRGN_INLINE_CLOSE:
	'}' {
    self.depthDelimeter and self.depthDelimeter[-1] == '$\x7B'
  }? {
    self.handle_rbrace_delimeter('$\x7B') 
  } -> popMode;

FRGN_CODE: ~[%$}]+ | '%' | '$';
FRGN_RBRACE: '}' -> type(FRGN_CODE);

mode fds;

/*
 * Opening and closing delimiters
 */

MLBRACE:
	'#[' {
      self.handle_mlbrace_delimeter()
    };

MRBRACE:
	']#' {
    self.handle_mrbrace_delimeter()
  };

LPAREN:
	'(' {
    self.handle_lparen_delimeter()
  };

RPAREN:
	')' {
    self.handle_rparen_delimeter()
  };

/*
 * Operators and punctuation
 */

EQUALS: '=';
QMARK: '?';
COLON: ':';
PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
COMMA: ',';
SEMI_COLON: ';';
INC: '++';
DEC: '--';

/*
 * Numeric and variable tokens
 */

NUMBER: DIGIT+ ('.' DIGIT*)? | '.' DIGIT+;
VAR:
	'@' DIGIT+ {
    self.text = self.text[1:]
    if not self.text.isdigit():
      raise SyntaxError(
        f"Syntax Error: Invalid '{self.text}' provided"
      )
  };

/*
 * Matrix separators
 */

M_HSEP: '---' '- '*;
M_VBAR: '|';

/*
 * Newline handling
 */

NEWLINE_OR_NL:
	'\r'? '\n' {
    top = self.depthDelimeter[-1] if self.depthDelimeter else None
    self.type = self.NEWLINE if top == '%%' else self.NL
  };

/*
 * Whitespace, fallback and end handler
 */

WS: [ \t]+ -> skip;

FRGN_INLINE_OPEN:
	'${' {
    self.depthDelimeter.append('$\x7B')
  } -> pushMode(DEFAULT_MODE);

FRGN_BLOCK_OPEN: '$$' -> pushMode(DEFAULT_MODE);

FDS_INLINE_CLOSE:
	'}' {
    self.handle_rbrace_delimeter()
  } -> popMode;

FDS_BLOCK_CLOSE:
	'%%' {
    self.depthDelimeter.pop()
  } -> popMode;

ERROR:
	. {raise Exception(
		f"Syntax Error: Invalid '{self.text}' provided"
	)};