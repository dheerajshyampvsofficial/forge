# Generated from /Users/dheerajshyampvs/PythonProjects/forge/compiler/frontend/gen_script/fds_lexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,33,224,6,-1,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,
        7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,
        2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,
        7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,
        2,26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,4,5,96,8,5,11,5,
        12,5,97,1,5,3,5,101,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,
        1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,
        1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,
        1,20,1,20,1,20,1,21,4,21,144,8,21,11,21,12,21,145,1,21,1,21,5,21,
        150,8,21,10,21,12,21,153,9,21,3,21,155,8,21,1,21,1,21,4,21,159,8,
        21,11,21,12,21,160,3,21,163,8,21,1,22,1,22,4,22,167,8,22,11,22,12,
        22,168,1,22,1,22,1,23,1,23,1,23,1,23,1,23,5,23,178,8,23,10,23,12,
        23,181,9,23,1,24,1,24,1,25,3,25,186,8,25,1,25,1,25,1,25,1,26,4,26,
        192,8,26,11,26,12,26,193,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,0,0,32,2,0,4,3,6,4,8,5,10,
        6,12,7,14,8,16,9,18,10,20,11,22,12,24,13,26,14,28,15,30,16,32,17,
        34,18,36,19,38,20,40,21,42,22,44,23,46,24,48,25,50,26,52,27,54,28,
        56,29,58,30,60,31,62,32,64,33,2,0,1,3,1,0,48,57,2,0,36,37,125,125,
        2,0,9,9,32,32,232,0,4,1,0,0,0,0,6,1,0,0,0,0,8,1,0,0,0,0,10,1,0,0,
        0,0,12,1,0,0,0,1,14,1,0,0,0,1,16,1,0,0,0,1,18,1,0,0,0,1,20,1,0,0,
        0,1,22,1,0,0,0,1,24,1,0,0,0,1,26,1,0,0,0,1,28,1,0,0,0,1,30,1,0,0,
        0,1,32,1,0,0,0,1,34,1,0,0,0,1,36,1,0,0,0,1,38,1,0,0,0,1,40,1,0,0,
        0,1,42,1,0,0,0,1,44,1,0,0,0,1,46,1,0,0,0,1,48,1,0,0,0,1,50,1,0,0,
        0,1,52,1,0,0,0,1,54,1,0,0,0,1,56,1,0,0,0,1,58,1,0,0,0,1,60,1,0,0,
        0,1,62,1,0,0,0,1,64,1,0,0,0,2,66,1,0,0,0,4,68,1,0,0,0,6,75,1,0,0,
        0,8,82,1,0,0,0,10,87,1,0,0,0,12,100,1,0,0,0,14,102,1,0,0,0,16,107,
        1,0,0,0,18,112,1,0,0,0,20,115,1,0,0,0,22,118,1,0,0,0,24,120,1,0,
        0,0,26,122,1,0,0,0,28,124,1,0,0,0,30,126,1,0,0,0,32,128,1,0,0,0,
        34,130,1,0,0,0,36,132,1,0,0,0,38,134,1,0,0,0,40,136,1,0,0,0,42,139,
        1,0,0,0,44,162,1,0,0,0,46,164,1,0,0,0,48,172,1,0,0,0,50,182,1,0,
        0,0,52,185,1,0,0,0,54,191,1,0,0,0,56,197,1,0,0,0,58,204,1,0,0,0,
        60,209,1,0,0,0,62,214,1,0,0,0,64,221,1,0,0,0,66,67,7,0,0,0,67,3,
        1,0,0,0,68,69,5,37,0,0,69,70,5,37,0,0,70,71,1,0,0,0,71,72,6,1,0,
        0,72,73,1,0,0,0,73,74,6,1,1,0,74,5,1,0,0,0,75,76,5,37,0,0,76,77,
        5,123,0,0,77,78,1,0,0,0,78,79,6,2,2,0,79,80,1,0,0,0,80,81,6,2,1,
        0,81,7,1,0,0,0,82,83,5,36,0,0,83,84,5,36,0,0,84,85,1,0,0,0,85,86,
        6,3,3,0,86,9,1,0,0,0,87,88,5,125,0,0,88,89,5,125,0,0,89,90,1,0,0,
        0,90,91,6,4,4,0,91,92,1,0,0,0,92,93,6,4,3,0,93,11,1,0,0,0,94,96,
        8,1,0,0,95,94,1,0,0,0,96,97,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,
        98,101,1,0,0,0,99,101,2,36,37,0,100,95,1,0,0,0,100,99,1,0,0,0,101,
        13,1,0,0,0,102,103,5,35,0,0,103,104,5,91,0,0,104,105,1,0,0,0,105,
        106,6,6,5,0,106,15,1,0,0,0,107,108,5,93,0,0,108,109,5,35,0,0,109,
        110,1,0,0,0,110,111,6,7,6,0,111,17,1,0,0,0,112,113,5,40,0,0,113,
        114,6,8,7,0,114,19,1,0,0,0,115,116,5,41,0,0,116,117,6,9,8,0,117,
        21,1,0,0,0,118,119,5,61,0,0,119,23,1,0,0,0,120,121,5,63,0,0,121,
        25,1,0,0,0,122,123,5,58,0,0,123,27,1,0,0,0,124,125,5,43,0,0,125,
        29,1,0,0,0,126,127,5,45,0,0,127,31,1,0,0,0,128,129,5,42,0,0,129,
        33,1,0,0,0,130,131,5,47,0,0,131,35,1,0,0,0,132,133,5,44,0,0,133,
        37,1,0,0,0,134,135,5,59,0,0,135,39,1,0,0,0,136,137,5,43,0,0,137,
        138,5,43,0,0,138,41,1,0,0,0,139,140,5,45,0,0,140,141,5,45,0,0,141,
        43,1,0,0,0,142,144,3,2,0,0,143,142,1,0,0,0,144,145,1,0,0,0,145,143,
        1,0,0,0,145,146,1,0,0,0,146,154,1,0,0,0,147,151,5,46,0,0,148,150,
        3,2,0,0,149,148,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,
        1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,154,147,1,0,0,0,154,155,
        1,0,0,0,155,163,1,0,0,0,156,158,5,46,0,0,157,159,3,2,0,0,158,157,
        1,0,0,0,159,160,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,163,
        1,0,0,0,162,143,1,0,0,0,162,156,1,0,0,0,163,45,1,0,0,0,164,166,5,
        64,0,0,165,167,3,2,0,0,166,165,1,0,0,0,167,168,1,0,0,0,168,166,1,
        0,0,0,168,169,1,0,0,0,169,170,1,0,0,0,170,171,6,22,9,0,171,47,1,
        0,0,0,172,173,5,45,0,0,173,174,5,45,0,0,174,175,5,45,0,0,175,179,
        1,0,0,0,176,178,5,45,0,0,177,176,1,0,0,0,178,181,1,0,0,0,179,177,
        1,0,0,0,179,180,1,0,0,0,180,49,1,0,0,0,181,179,1,0,0,0,182,183,5,
        124,0,0,183,51,1,0,0,0,184,186,5,13,0,0,185,184,1,0,0,0,185,186,
        1,0,0,0,186,187,1,0,0,0,187,188,5,10,0,0,188,189,6,25,10,0,189,53,
        1,0,0,0,190,192,7,2,0,0,191,190,1,0,0,0,192,193,1,0,0,0,193,191,
        1,0,0,0,193,194,1,0,0,0,194,195,1,0,0,0,195,196,6,26,11,0,196,55,
        1,0,0,0,197,198,5,123,0,0,198,199,5,123,0,0,199,200,1,0,0,0,200,
        201,6,27,12,0,201,202,1,0,0,0,202,203,6,27,13,0,203,57,1,0,0,0,204,
        205,5,36,0,0,205,206,5,36,0,0,206,207,1,0,0,0,207,208,6,28,13,0,
        208,59,1,0,0,0,209,210,5,125,0,0,210,211,6,29,14,0,211,212,1,0,0,
        0,212,213,6,29,3,0,213,61,1,0,0,0,214,215,5,37,0,0,215,216,5,37,
        0,0,216,217,1,0,0,0,217,218,6,30,15,0,218,219,1,0,0,0,219,220,6,
        30,3,0,220,63,1,0,0,0,221,222,9,0,0,0,222,223,6,31,16,0,223,65,1,
        0,0,0,13,0,1,97,100,145,151,154,160,162,168,179,185,193,17,1,1,0,
        5,1,0,1,2,1,4,0,0,1,4,2,1,6,3,1,7,4,1,8,5,1,9,6,1,22,7,1,25,8,6,
        0,0,1,27,9,5,0,0,1,29,10,1,30,11,1,31,12
    ]

class fds_lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    fds = 1

    NEWLINE = 1
    NL = 2
    FDS_BLOCK_OPEN = 3
    FDS_INLINE_OPEN = 4
    FRGN_BLOCK_CLOSE = 5
    FRGN_INLINE_CLOSE = 6
    FRGN_CODE = 7
    MLBRACE = 8
    MRBRACE = 9
    LPAREN = 10
    RPAREN = 11
    EQUALS = 12
    QMARK = 13
    COLON = 14
    PLUS = 15
    MINUS = 16
    STAR = 17
    SLASH = 18
    COMMA = 19
    SEMI_COLON = 20
    INC = 21
    DEC = 22
    NUMBER = 23
    VAR = 24
    M_HSEP = 25
    M_VBAR = 26
    NEWLINE_OR_NL = 27
    WS = 28
    FRGN_INLINE_OPEN = 29
    FRGN_BLOCK_OPEN = 30
    FDS_INLINE_CLOSE = 31
    FDS_BLOCK_CLOSE = 32
    ERROR = 33

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "fds" ]

    literalNames = [ "<INVALID>",
            "'#['", "']#'", "'('", "')'", "'='", "'?'", "':'", "'+'", "'-'", 
            "'*'", "'/'", "','", "';'", "'++'", "'--'", "'|'" ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "NL", "FDS_BLOCK_OPEN", "FDS_INLINE_OPEN", "FRGN_BLOCK_CLOSE", 
            "FRGN_INLINE_CLOSE", "FRGN_CODE", "MLBRACE", "MRBRACE", "LPAREN", 
            "RPAREN", "EQUALS", "QMARK", "COLON", "PLUS", "MINUS", "STAR", 
            "SLASH", "COMMA", "SEMI_COLON", "INC", "DEC", "NUMBER", "VAR", 
            "M_HSEP", "M_VBAR", "NEWLINE_OR_NL", "WS", "FRGN_INLINE_OPEN", 
            "FRGN_BLOCK_OPEN", "FDS_INLINE_CLOSE", "FDS_BLOCK_CLOSE", "ERROR" ]

    ruleNames = [ "DIGIT", "FDS_BLOCK_OPEN", "FDS_INLINE_OPEN", "FRGN_BLOCK_CLOSE", 
                  "FRGN_INLINE_CLOSE", "FRGN_CODE", "MLBRACE", "MRBRACE", 
                  "LPAREN", "RPAREN", "EQUALS", "QMARK", "COLON", "PLUS", 
                  "MINUS", "STAR", "SLASH", "COMMA", "SEMI_COLON", "INC", 
                  "DEC", "NUMBER", "VAR", "M_HSEP", "M_VBAR", "NEWLINE_OR_NL", 
                  "WS", "FRGN_INLINE_OPEN", "FRGN_BLOCK_OPEN", "FDS_INLINE_CLOSE", 
                  "FDS_BLOCK_CLOSE", "ERROR" ]

    grammarFileName = "fds_lexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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

    # Closing symbol handler code
    def handle_close_delimeter(self, expected_start_delimeter: str = "%\x7B"):
      if (not self.depthDelimeter) or (not expected_start_delimeter):
        raise Exception(
          f"Unmatched '\x7D' at end of input"
        )
      
      delimiter = self.depthDelimeter.pop()
      
      if delimiter != expected_start_delimeter:
        raise Exception(
          f"Closing '\x7D' does not match '{expected_start_delimeter}' in line {self.line}."
        )


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.FDS_BLOCK_OPEN_action 
            actions[2] = self.FDS_INLINE_OPEN_action 
            actions[4] = self.FRGN_INLINE_CLOSE_action 
            actions[6] = self.MLBRACE_action 
            actions[7] = self.MRBRACE_action 
            actions[8] = self.LPAREN_action 
            actions[9] = self.RPAREN_action 
            actions[22] = self.VAR_action 
            actions[25] = self.NEWLINE_OR_NL_action 
            actions[27] = self.FRGN_INLINE_OPEN_action 
            actions[29] = self.FDS_INLINE_CLOSE_action 
            actions[30] = self.FDS_BLOCK_CLOSE_action 
            actions[31] = self.ERROR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FDS_BLOCK_OPEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.depthDelimeter.append('%%')
              
     

    def FDS_INLINE_OPEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.depthDelimeter.append('%\x7B')
              
     

    def FRGN_INLINE_CLOSE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.handle_close_delimeter(
                  expected_start_delimeter = '\x7B\x7B'
                )
              
     

    def MLBRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                  self.handle_mlbrace_delimeter()
                
     

    def MRBRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                self.handle_mrbrace_delimeter()
              
     

    def LPAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                self.handle_lparen_delimeter()
              
     

    def RPAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                self.handle_rparen_delimeter()
              
     

    def VAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

                self.text = self.text[1:]
                if not self.text.isdigit():
                  raise SyntaxError(
                    f"Syntax Error: Invalid '{self.text}' provided"
                  )
              
     

    def NEWLINE_OR_NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:

                top = self.depthDelimeter[-1] if self.depthDelimeter else None
                self.type = self.NEWLINE if top == '%%' else self.NL
              
     

    def FRGN_INLINE_OPEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:

                self.depthDelimeter.append('\x7B\x7B')
              
     

    def FDS_INLINE_CLOSE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 10:

                self.handle_close_delimeter()
              
     

    def FDS_BLOCK_CLOSE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 11:

                self.depthDelimeter.pop()
              
     

    def ERROR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 12:

                raise Exception(
            		  f"Syntax Error: Invalid '{self.text}' provided in line {self.line}"
            	  )
              
     


