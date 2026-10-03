# Generated from /Users/dheerajshyampvs/PythonProjects/forge/compiler/frontend/gen_script/fds_parser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,231,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,0,1,0,1,1,4,1,46,8,1,11,1,12,1,47,1,1,1,1,5,1,52,8,1,10,
        1,12,1,55,9,1,1,1,5,1,58,8,1,10,1,12,1,61,9,1,1,1,1,1,1,1,5,1,66,
        8,1,10,1,12,1,69,9,1,1,1,1,1,5,1,73,8,1,10,1,12,1,76,9,1,1,1,1,1,
        3,1,80,8,1,1,2,1,2,1,2,5,2,85,8,2,10,2,12,2,88,9,2,1,2,3,2,91,8,
        2,1,3,1,3,3,3,95,8,3,1,3,5,3,98,8,3,10,3,12,3,101,9,3,1,4,1,4,4,
        4,105,8,4,11,4,12,4,106,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        3,6,119,8,6,1,7,1,7,1,8,1,8,1,8,5,8,126,8,8,10,8,12,8,129,9,8,1,
        9,1,9,1,9,5,9,134,8,9,10,9,12,9,137,9,9,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,3,10,146,8,10,1,11,1,11,5,11,150,8,11,10,11,12,11,153,
        9,11,1,11,1,11,5,11,157,8,11,10,11,12,11,160,9,11,1,11,1,11,1,11,
        3,11,165,8,11,1,12,1,12,5,12,169,8,12,10,12,12,12,172,9,12,1,12,
        1,12,5,12,176,8,12,10,12,12,12,179,9,12,1,12,5,12,182,8,12,10,12,
        12,12,185,9,12,1,13,1,13,5,13,189,8,13,10,13,12,13,192,9,13,1,13,
        5,13,195,8,13,10,13,12,13,198,9,13,1,14,1,14,1,14,5,14,203,8,14,
        10,14,12,14,206,9,14,1,15,4,15,209,8,15,11,15,12,15,210,1,16,1,16,
        1,17,1,17,1,17,1,17,5,17,219,8,17,10,17,12,17,222,9,17,1,17,1,17,
        1,17,1,17,1,17,3,17,229,8,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,0,5,2,0,1,1,20,20,1,0,15,16,1,0,17,18,1,
        0,21,22,2,0,2,2,20,20,245,0,39,1,0,0,0,2,79,1,0,0,0,4,90,1,0,0,0,
        6,94,1,0,0,0,8,104,1,0,0,0,10,110,1,0,0,0,12,112,1,0,0,0,14,120,
        1,0,0,0,16,122,1,0,0,0,18,130,1,0,0,0,20,145,1,0,0,0,22,164,1,0,
        0,0,24,166,1,0,0,0,26,186,1,0,0,0,28,199,1,0,0,0,30,208,1,0,0,0,
        32,212,1,0,0,0,34,228,1,0,0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,41,
        1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,39,1,0,0,0,
        42,43,5,0,0,1,43,1,1,0,0,0,44,46,5,7,0,0,45,44,1,0,0,0,46,47,1,0,
        0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,80,1,0,0,0,49,53,5,3,0,0,50,52,
        5,1,0,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,
        54,59,1,0,0,0,55,53,1,0,0,0,56,58,3,4,2,0,57,56,1,0,0,0,58,61,1,
        0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,
        80,5,32,0,0,63,67,5,4,0,0,64,66,5,2,0,0,65,64,1,0,0,0,66,69,1,0,
        0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,74,
        3,10,5,0,71,73,5,2,0,0,72,71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,
        74,75,1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,0,77,78,5,31,0,0,78,80,1,
        0,0,0,79,45,1,0,0,0,79,49,1,0,0,0,79,63,1,0,0,0,80,3,1,0,0,0,81,
        91,3,6,3,0,82,86,5,30,0,0,83,85,3,2,1,0,84,83,1,0,0,0,85,88,1,0,
        0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,0,89,91,
        5,5,0,0,90,81,1,0,0,0,90,82,1,0,0,0,91,5,1,0,0,0,92,95,3,8,4,0,93,
        95,3,10,5,0,94,92,1,0,0,0,94,93,1,0,0,0,95,99,1,0,0,0,96,98,7,0,
        0,0,97,96,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,
        7,1,0,0,0,101,99,1,0,0,0,102,103,5,24,0,0,103,105,5,12,0,0,104,102,
        1,0,0,0,105,106,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,108,
        1,0,0,0,108,109,3,10,5,0,109,9,1,0,0,0,110,111,3,12,6,0,111,11,1,
        0,0,0,112,118,3,14,7,0,113,114,5,13,0,0,114,115,3,12,6,0,115,116,
        5,14,0,0,116,117,3,12,6,0,117,119,1,0,0,0,118,113,1,0,0,0,118,119,
        1,0,0,0,119,13,1,0,0,0,120,121,3,16,8,0,121,15,1,0,0,0,122,127,3,
        18,9,0,123,124,7,1,0,0,124,126,3,18,9,0,125,123,1,0,0,0,126,129,
        1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,17,1,0,0,0,129,127,1,
        0,0,0,130,135,3,20,10,0,131,132,7,2,0,0,132,134,3,20,10,0,133,131,
        1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,19,1,
        0,0,0,137,135,1,0,0,0,138,139,7,1,0,0,139,146,3,20,10,0,140,141,
        7,3,0,0,141,146,5,24,0,0,142,143,5,24,0,0,143,146,7,3,0,0,144,146,
        3,22,11,0,145,138,1,0,0,0,145,140,1,0,0,0,145,142,1,0,0,0,145,144,
        1,0,0,0,146,21,1,0,0,0,147,151,5,8,0,0,148,150,3,32,16,0,149,148,
        1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,154,
        1,0,0,0,153,151,1,0,0,0,154,158,3,24,12,0,155,157,3,32,16,0,156,
        155,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,
        161,1,0,0,0,160,158,1,0,0,0,161,162,5,9,0,0,162,165,1,0,0,0,163,
        165,3,34,17,0,164,147,1,0,0,0,164,163,1,0,0,0,165,23,1,0,0,0,166,
        183,3,26,13,0,167,169,5,2,0,0,168,167,1,0,0,0,169,172,1,0,0,0,170,
        168,1,0,0,0,170,171,1,0,0,0,171,173,1,0,0,0,172,170,1,0,0,0,173,
        177,5,25,0,0,174,176,5,2,0,0,175,174,1,0,0,0,176,179,1,0,0,0,177,
        175,1,0,0,0,177,178,1,0,0,0,178,180,1,0,0,0,179,177,1,0,0,0,180,
        182,3,26,13,0,181,170,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,
        184,1,0,0,0,184,25,1,0,0,0,185,183,1,0,0,0,186,196,3,28,14,0,187,
        189,7,4,0,0,188,187,1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,
        191,1,0,0,0,191,193,1,0,0,0,192,190,1,0,0,0,193,195,3,28,14,0,194,
        190,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,
        27,1,0,0,0,198,196,1,0,0,0,199,204,3,30,15,0,200,201,5,26,0,0,201,
        203,3,30,15,0,202,200,1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,0,204,
        205,1,0,0,0,205,29,1,0,0,0,206,204,1,0,0,0,207,209,3,10,5,0,208,
        207,1,0,0,0,209,210,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,211,
        31,1,0,0,0,212,213,5,2,0,0,213,33,1,0,0,0,214,229,5,23,0,0,215,229,
        5,24,0,0,216,220,5,29,0,0,217,219,3,2,1,0,218,217,1,0,0,0,219,222,
        1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,223,1,0,0,0,222,220,
        1,0,0,0,223,229,5,6,0,0,224,225,5,10,0,0,225,226,3,10,5,0,226,227,
        5,11,0,0,227,229,1,0,0,0,228,214,1,0,0,0,228,215,1,0,0,0,228,216,
        1,0,0,0,228,224,1,0,0,0,229,35,1,0,0,0,28,39,47,53,59,67,74,79,86,
        90,94,99,106,118,127,135,145,151,158,164,170,177,183,190,196,204,
        210,220,228
    ]

class fds_parser ( Parser ):

    grammarFileName = "fds_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'#['", "']#'", "'('", "')'", "'='", "'?'", "':'", 
                     "'+'", "'-'", "'*'", "'/'", "','", "';'", "'++'", "'--'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'|'" ]

    symbolicNames = [ "<INVALID>", "NEWLINE", "NL", "FDS_BLOCK_OPEN", "FDS_INLINE_OPEN", 
                      "FRGN_BLOCK_CLOSE", "FRGN_INLINE_CLOSE", "FRGN_CODE", 
                      "MLBRACE", "MRBRACE", "LPAREN", "RPAREN", "EQUALS", 
                      "QMARK", "COLON", "PLUS", "MINUS", "STAR", "SLASH", 
                      "COMMA", "SEMI_COLON", "INC", "DEC", "NUMBER", "VAR", 
                      "M_HSEP", "M_VBAR", "NEWLINE_OR_NL", "WS", "FRGN_INLINE_OPEN", 
                      "FRGN_BLOCK_OPEN", "FDS_INLINE_CLOSE", "FDS_BLOCK_CLOSE", 
                      "ERROR" ]

    RULE_start = 0
    RULE_part = 1
    RULE_stmt = 2
    RULE_simple_stmt = 3
    RULE_assignment = 4
    RULE_expr = 5
    RULE_ternary_expr = 6
    RULE_binary_expr = 7
    RULE_addition = 8
    RULE_multiplication = 9
    RULE_unary_sign = 10
    RULE_matrix = 11
    RULE_matrix_rows = 12
    RULE_block_row = 13
    RULE_matrix_row = 14
    RULE_matrix_cell = 15
    RULE_matrix_inner_ignores = 16
    RULE_atom = 17

    ruleNames =  [ "start", "part", "stmt", "simple_stmt", "assignment", 
                   "expr", "ternary_expr", "binary_expr", "addition", "multiplication", 
                   "unary_sign", "matrix", "matrix_rows", "block_row", "matrix_row", 
                   "matrix_cell", "matrix_inner_ignores", "atom" ]

    EOF = Token.EOF
    NEWLINE=1
    NL=2
    FDS_BLOCK_OPEN=3
    FDS_INLINE_OPEN=4
    FRGN_BLOCK_CLOSE=5
    FRGN_INLINE_CLOSE=6
    FRGN_CODE=7
    MLBRACE=8
    MRBRACE=9
    LPAREN=10
    RPAREN=11
    EQUALS=12
    QMARK=13
    COLON=14
    PLUS=15
    MINUS=16
    STAR=17
    SLASH=18
    COMMA=19
    SEMI_COLON=20
    INC=21
    DEC=22
    NUMBER=23
    VAR=24
    M_HSEP=25
    M_VBAR=26
    NEWLINE_OR_NL=27
    WS=28
    FRGN_INLINE_OPEN=29
    FRGN_BLOCK_OPEN=30
    FDS_INLINE_CLOSE=31
    FDS_BLOCK_CLOSE=32
    ERROR=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_start

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PartsContext(StartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.StartContext
            super().__init__(parser)
            self._part = None # PartContext
            self.parts = list() # of PartContexts
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(fds_parser.EOF, 0)
        def part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fds_parser.PartContext)
            else:
                return self.getTypedRuleContext(fds_parser.PartContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParts" ):
                return visitor.visitParts(self)
            else:
                return visitor.visitChildren(self)



    def start(self):

        localctx = fds_parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.PartsContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 152) != 0):
                self.state = 36
                localctx._part = self.part()
                localctx.parts.append(localctx._part)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(fds_parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_part

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FdsInlineContext(PartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.PartContext
            super().__init__(parser)
            self.value = None # ExprContext
            self.copyFrom(ctx)

        def FDS_INLINE_OPEN(self):
            return self.getToken(fds_parser.FDS_INLINE_OPEN, 0)
        def FDS_INLINE_CLOSE(self):
            return self.getToken(fds_parser.FDS_INLINE_CLOSE, 0)
        def expr(self):
            return self.getTypedRuleContext(fds_parser.ExprContext,0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.NL)
            else:
                return self.getToken(fds_parser.NL, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFdsInline" ):
                return visitor.visitFdsInline(self)
            else:
                return visitor.visitChildren(self)


    class FrgnCodeContext(PartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.PartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FRGN_CODE(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.FRGN_CODE)
            else:
                return self.getToken(fds_parser.FRGN_CODE, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFrgnCode" ):
                return visitor.visitFrgnCode(self)
            else:
                return visitor.visitChildren(self)


    class FdsBlockContext(PartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.PartContext
            super().__init__(parser)
            self._stmt = None # StmtContext
            self.stmts = list() # of StmtContexts
            self.copyFrom(ctx)

        def FDS_BLOCK_OPEN(self):
            return self.getToken(fds_parser.FDS_BLOCK_OPEN, 0)
        def FDS_BLOCK_CLOSE(self):
            return self.getToken(fds_parser.FDS_BLOCK_CLOSE, 0)
        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.NEWLINE)
            else:
                return self.getToken(fds_parser.NEWLINE, i)
        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fds_parser.StmtContext)
            else:
                return self.getTypedRuleContext(fds_parser.StmtContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFdsBlock" ):
                return visitor.visitFdsBlock(self)
            else:
                return visitor.visitChildren(self)



    def part(self):

        localctx = fds_parser.PartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_part)
        self._la = 0 # Token type
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = fds_parser.FrgnCodeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 45 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 44
                        self.match(fds_parser.FRGN_CODE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 47 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                pass
            elif token in [3]:
                localctx = fds_parser.FdsBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(fds_parser.FDS_BLOCK_OPEN)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 50
                    self.match(fds_parser.NEWLINE)
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1642169600) != 0):
                    self.state = 56
                    localctx._stmt = self.stmt()
                    localctx.stmts.append(localctx._stmt)
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 62
                self.match(fds_parser.FDS_BLOCK_CLOSE)
                pass
            elif token in [4]:
                localctx = fds_parser.FdsInlineContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.match(fds_parser.FDS_INLINE_OPEN)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 64
                    self.match(fds_parser.NL)
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 70
                localctx.value = self.expr()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 71
                    self.match(fds_parser.NL)
                    self.state = 76
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 77
                self.match(fds_parser.FDS_INLINE_CLOSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForeignBlockContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.StmtContext
            super().__init__(parser)
            self._part = None # PartContext
            self.body = list() # of PartContexts
            self.copyFrom(ctx)

        def FRGN_BLOCK_OPEN(self):
            return self.getToken(fds_parser.FRGN_BLOCK_OPEN, 0)
        def FRGN_BLOCK_CLOSE(self):
            return self.getToken(fds_parser.FRGN_BLOCK_CLOSE, 0)
        def part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fds_parser.PartContext)
            else:
                return self.getTypedRuleContext(fds_parser.PartContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeignBlock" ):
                return visitor.visitForeignBlock(self)
            else:
                return visitor.visitChildren(self)


    class StatementContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simple_stmt(self):
            return self.getTypedRuleContext(fds_parser.Simple_stmtContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = fds_parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 10, 15, 16, 21, 22, 23, 24, 29]:
                localctx = fds_parser.StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.simple_stmt()
                pass
            elif token in [30]:
                localctx = fds_parser.ForeignBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(fds_parser.FRGN_BLOCK_OPEN)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 152) != 0):
                    self.state = 83
                    localctx._part = self.part()
                    localctx.body.append(localctx._part)
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 89
                self.match(fds_parser.FRGN_BLOCK_CLOSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_simple_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimpleStatementContext(Simple_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.Simple_stmtContext
            super().__init__(parser)
            self.assign = None # AssignmentContext
            self.expression = None # ExprContext
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(fds_parser.AssignmentContext,0)

        def expr(self):
            return self.getTypedRuleContext(fds_parser.ExprContext,0)

        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.SEMI_COLON)
            else:
                return self.getToken(fds_parser.SEMI_COLON, i)
        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.NEWLINE)
            else:
                return self.getToken(fds_parser.NEWLINE, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleStatement" ):
                return visitor.visitSimpleStatement(self)
            else:
                return visitor.visitChildren(self)



    def simple_stmt(self):

        localctx = fds_parser.Simple_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simple_stmt)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.SimpleStatementContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 92
                localctx.assign = self.assignment()
                pass

            elif la_ == 2:
                self.state = 93
                localctx.expression = self.expr()
                pass


            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==20:
                self.state = 96
                _la = self._input.LA(1)
                if not(_la==1 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_assignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignmentStmtContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.AssignmentContext
            super().__init__(parser)
            self._VAR = None # Token
            self.targets = list() # of Tokens
            self.value = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(fds_parser.ExprContext,0)

        def EQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.EQUALS)
            else:
                return self.getToken(fds_parser.EQUALS, i)
        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.VAR)
            else:
                return self.getToken(fds_parser.VAR, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStmt" ):
                return visitor.visitAssignmentStmt(self)
            else:
                return visitor.visitChildren(self)



    def assignment(self):

        localctx = fds_parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            localctx = fds_parser.AssignmentStmtContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 104 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 102
                    localctx._VAR = self.match(fds_parser.VAR)
                    localctx.targets.append(localctx._VAR)
                    self.state = 103
                    self.match(fds_parser.EQUALS)

                else:
                    raise NoViableAltException(self)
                self.state = 106 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 108
            localctx.value = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ternary_expr(self):
            return self.getTypedRuleContext(fds_parser.Ternary_exprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = fds_parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            localctx = fds_parser.ExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.ternary_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ternary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_ternary_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TernaryExpressionContext(Ternary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.Ternary_exprContext
            super().__init__(parser)
            self.left = None # Binary_exprContext
            self.middle = None # Ternary_exprContext
            self.right = None # Ternary_exprContext
            self.copyFrom(ctx)

        def binary_expr(self):
            return self.getTypedRuleContext(fds_parser.Binary_exprContext,0)

        def QMARK(self):
            return self.getToken(fds_parser.QMARK, 0)
        def COLON(self):
            return self.getToken(fds_parser.COLON, 0)
        def ternary_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fds_parser.Ternary_exprContext)
            else:
                return self.getTypedRuleContext(fds_parser.Ternary_exprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernaryExpression" ):
                return visitor.visitTernaryExpression(self)
            else:
                return visitor.visitChildren(self)



    def ternary_expr(self):

        localctx = fds_parser.Ternary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ternary_expr)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.TernaryExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            localctx.left = self.binary_expr()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 113
                self.match(fds_parser.QMARK)
                self.state = 114
                localctx.middle = self.ternary_expr()
                self.state = 115
                self.match(fds_parser.COLON)
                self.state = 116
                localctx.right = self.ternary_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Binary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_binary_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BinaryExpressionContext(Binary_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.Binary_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def addition(self):
            return self.getTypedRuleContext(fds_parser.AdditionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryExpression" ):
                return visitor.visitBinaryExpression(self)
            else:
                return visitor.visitChildren(self)



    def binary_expr(self):

        localctx = fds_parser.Binary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_binary_expr)
        try:
            localctx = fds_parser.BinaryExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.addition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_addition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddExpressionContext(AdditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.AdditionContext
            super().__init__(parser)
            self.left = None # MultiplicationContext
            self._PLUS = None # Token
            self.ops = list() # of Tokens
            self._MINUS = None # Token
            self._tset251 = None # Token
            self._multiplication = None # MultiplicationContext
            self.rights = list() # of MultiplicationContexts
            self.copyFrom(ctx)

        def multiplication(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fds_parser.MultiplicationContext)
            else:
                return self.getTypedRuleContext(fds_parser.MultiplicationContext,i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.PLUS)
            else:
                return self.getToken(fds_parser.PLUS, i)
        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.MINUS)
            else:
                return self.getToken(fds_parser.MINUS, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpression" ):
                return visitor.visitAddExpression(self)
            else:
                return visitor.visitChildren(self)



    def addition(self):

        localctx = fds_parser.AdditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_addition)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.AddExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            localctx.left = self.multiplication()
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 123
                    localctx._tset251 = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==16):
                        localctx._tset251 = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    localctx.ops.append(localctx._tset251)
                    self.state = 124
                    localctx._multiplication = self.multiplication()
                    localctx.rights.append(localctx._multiplication) 
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_multiplication

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MulExpressionContext(MultiplicationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.MultiplicationContext
            super().__init__(parser)
            self.left = None # Unary_signContext
            self._STAR = None # Token
            self.ops = list() # of Tokens
            self._SLASH = None # Token
            self._tset288 = None # Token
            self._unary_sign = None # Unary_signContext
            self.rights = list() # of Unary_signContexts
            self.copyFrom(ctx)

        def unary_sign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fds_parser.Unary_signContext)
            else:
                return self.getTypedRuleContext(fds_parser.Unary_signContext,i)

        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.STAR)
            else:
                return self.getToken(fds_parser.STAR, i)
        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.SLASH)
            else:
                return self.getToken(fds_parser.SLASH, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpression" ):
                return visitor.visitMulExpression(self)
            else:
                return visitor.visitChildren(self)



    def multiplication(self):

        localctx = fds_parser.MultiplicationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_multiplication)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.MulExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            localctx.left = self.unary_sign()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 131
                localctx._tset288 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    localctx._tset288 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.ops.append(localctx._tset288)
                self.state = 132
                localctx._unary_sign = self.unary_sign()
                localctx.rights.append(localctx._unary_sign)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_signContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_unary_sign

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class UnarySignContext(Unary_signContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.Unary_signContext
            super().__init__(parser)
            self.sign = None # Token
            self.operand = None # Unary_signContext
            self.copyFrom(ctx)

        def unary_sign(self):
            return self.getTypedRuleContext(fds_parser.Unary_signContext,0)

        def PLUS(self):
            return self.getToken(fds_parser.PLUS, 0)
        def MINUS(self):
            return self.getToken(fds_parser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnarySign" ):
                return visitor.visitUnarySign(self)
            else:
                return visitor.visitChildren(self)


    class PostIncDecContext(Unary_signContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.Unary_signContext
            super().__init__(parser)
            self.variable = None # Token
            self.op = None # Token
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(fds_parser.VAR, 0)
        def INC(self):
            return self.getToken(fds_parser.INC, 0)
        def DEC(self):
            return self.getToken(fds_parser.DEC, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostIncDec" ):
                return visitor.visitPostIncDec(self)
            else:
                return visitor.visitChildren(self)


    class UnaryValueContext(Unary_signContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.Unary_signContext
            super().__init__(parser)
            self.value = None # MatrixContext
            self.copyFrom(ctx)

        def matrix(self):
            return self.getTypedRuleContext(fds_parser.MatrixContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryValue" ):
                return visitor.visitUnaryValue(self)
            else:
                return visitor.visitChildren(self)


    class PreIncDecContext(Unary_signContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.Unary_signContext
            super().__init__(parser)
            self.op = None # Token
            self.variable = None # Token
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(fds_parser.VAR, 0)
        def INC(self):
            return self.getToken(fds_parser.INC, 0)
        def DEC(self):
            return self.getToken(fds_parser.DEC, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreIncDec" ):
                return visitor.visitPreIncDec(self)
            else:
                return visitor.visitChildren(self)



    def unary_sign(self):

        localctx = fds_parser.Unary_signContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_unary_sign)
        self._la = 0 # Token type
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = fds_parser.UnarySignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                localctx.sign = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    localctx.sign = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 139
                localctx.operand = self.unary_sign()
                pass

            elif la_ == 2:
                localctx = fds_parser.PreIncDecContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 141
                localctx.variable = self.match(fds_parser.VAR)
                pass

            elif la_ == 3:
                localctx = fds_parser.PostIncDecContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                localctx.variable = self.match(fds_parser.VAR)
                self.state = 143
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 4:
                localctx = fds_parser.UnaryValueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 144
                localctx.value = self.matrix()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_matrix

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AtomLiteralContext(MatrixContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.MatrixContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(fds_parser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomLiteral" ):
                return visitor.visitAtomLiteral(self)
            else:
                return visitor.visitChildren(self)


    class MatrixLiteralContext(MatrixContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.MatrixContext
            super().__init__(parser)
            self.rows = None # Matrix_rowsContext
            self.copyFrom(ctx)

        def MLBRACE(self):
            return self.getToken(fds_parser.MLBRACE, 0)
        def MRBRACE(self):
            return self.getToken(fds_parser.MRBRACE, 0)
        def matrix_rows(self):
            return self.getTypedRuleContext(fds_parser.Matrix_rowsContext,0)

        def matrix_inner_ignores(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fds_parser.Matrix_inner_ignoresContext)
            else:
                return self.getTypedRuleContext(fds_parser.Matrix_inner_ignoresContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixLiteral" ):
                return visitor.visitMatrixLiteral(self)
            else:
                return visitor.visitChildren(self)



    def matrix(self):

        localctx = fds_parser.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_matrix)
        self._la = 0 # Token type
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = fds_parser.MatrixLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(fds_parser.MLBRACE)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 148
                    self.matrix_inner_ignores()
                    self.state = 153
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 154
                localctx.rows = self.matrix_rows()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 155
                    self.matrix_inner_ignores()
                    self.state = 160
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 161
                self.match(fds_parser.MRBRACE)
                pass
            elif token in [10, 23, 24, 29]:
                localctx = fds_parser.AtomLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_rowsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_matrix_rows

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MatrixRowsContext(Matrix_rowsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.Matrix_rowsContext
            super().__init__(parser)
            self._block_row = None # Block_rowContext
            self.groups = list() # of Block_rowContexts
            self.copyFrom(ctx)

        def block_row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fds_parser.Block_rowContext)
            else:
                return self.getTypedRuleContext(fds_parser.Block_rowContext,i)

        def M_HSEP(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.M_HSEP)
            else:
                return self.getToken(fds_parser.M_HSEP, i)
        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.NL)
            else:
                return self.getToken(fds_parser.NL, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixRows" ):
                return visitor.visitMatrixRows(self)
            else:
                return visitor.visitChildren(self)



    def matrix_rows(self):

        localctx = fds_parser.Matrix_rowsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_matrix_rows)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.MatrixRowsContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            localctx._block_row = self.block_row()
            localctx.groups.append(localctx._block_row)
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 170
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 167
                        self.match(fds_parser.NL)
                        self.state = 172
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 173
                    self.match(fds_parser.M_HSEP)
                    self.state = 177
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 174
                        self.match(fds_parser.NL)
                        self.state = 179
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 180
                    localctx._block_row = self.block_row()
                    localctx.groups.append(localctx._block_row) 
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_rowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_block_row

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlockRowContext(Block_rowContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.Block_rowContext
            super().__init__(parser)
            self._matrix_row = None # Matrix_rowContext
            self.lines = list() # of Matrix_rowContexts
            self.copyFrom(ctx)

        def matrix_row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fds_parser.Matrix_rowContext)
            else:
                return self.getTypedRuleContext(fds_parser.Matrix_rowContext,i)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.NL)
            else:
                return self.getToken(fds_parser.NL, i)
        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.SEMI_COLON)
            else:
                return self.getToken(fds_parser.SEMI_COLON, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockRow" ):
                return visitor.visitBlockRow(self)
            else:
                return visitor.visitChildren(self)



    def block_row(self):

        localctx = fds_parser.Block_rowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block_row)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.BlockRowContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            localctx._matrix_row = self.matrix_row()
            localctx.lines.append(localctx._matrix_row)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 190
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2 or _la==20:
                        self.state = 187
                        _la = self._input.LA(1)
                        if not(_la==2 or _la==20):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 192
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 193
                    localctx._matrix_row = self.matrix_row()
                    localctx.lines.append(localctx._matrix_row) 
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_rowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_matrix_row

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MatrixRowContext(Matrix_rowContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.Matrix_rowContext
            super().__init__(parser)
            self._matrix_cell = None # Matrix_cellContext
            self.cells = list() # of Matrix_cellContexts
            self.copyFrom(ctx)

        def matrix_cell(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fds_parser.Matrix_cellContext)
            else:
                return self.getTypedRuleContext(fds_parser.Matrix_cellContext,i)

        def M_VBAR(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.M_VBAR)
            else:
                return self.getToken(fds_parser.M_VBAR, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixRow" ):
                return visitor.visitMatrixRow(self)
            else:
                return visitor.visitChildren(self)



    def matrix_row(self):

        localctx = fds_parser.Matrix_rowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_matrix_row)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.MatrixRowContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            localctx._matrix_cell = self.matrix_cell()
            localctx.cells.append(localctx._matrix_cell)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 200
                self.match(fds_parser.M_VBAR)
                self.state = 201
                localctx._matrix_cell = self.matrix_cell()
                localctx.cells.append(localctx._matrix_cell)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_cellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_matrix_cell

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MatrixCellContext(Matrix_cellContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.Matrix_cellContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self.elements = list() # of ExprContexts
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fds_parser.ExprContext)
            else:
                return self.getTypedRuleContext(fds_parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixCell" ):
                return visitor.visitMatrixCell(self)
            else:
                return visitor.visitChildren(self)



    def matrix_cell(self):

        localctx = fds_parser.Matrix_cellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_matrix_cell)
        try:
            localctx = fds_parser.MatrixCellContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 208 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 207
                    localctx._expr = self.expr()
                    localctx.elements.append(localctx._expr)

                else:
                    raise NoViableAltException(self)
                self.state = 210 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_inner_ignoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(fds_parser.NL, 0)

        def getRuleIndex(self):
            return fds_parser.RULE_matrix_inner_ignores

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix_inner_ignores" ):
                return visitor.visitMatrix_inner_ignores(self)
            else:
                return visitor.visitChildren(self)




    def matrix_inner_ignores(self):

        localctx = fds_parser.Matrix_inner_ignoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_matrix_inner_ignores)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(fds_parser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return fds_parser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarLiteralContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.AtomContext
            super().__init__(parser)
            self.variable = None # Token
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(fds_parser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarLiteral" ):
                return visitor.visitVarLiteral(self)
            else:
                return visitor.visitChildren(self)


    class FrgnInlineContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.AtomContext
            super().__init__(parser)
            self.frgn_inline = None # Token
            self._part = None # PartContext
            self.body = list() # of PartContexts
            self.copyFrom(ctx)

        def FRGN_INLINE_CLOSE(self):
            return self.getToken(fds_parser.FRGN_INLINE_CLOSE, 0)
        def FRGN_INLINE_OPEN(self):
            return self.getToken(fds_parser.FRGN_INLINE_OPEN, 0)
        def part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fds_parser.PartContext)
            else:
                return self.getTypedRuleContext(fds_parser.PartContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFrgnInline" ):
                return visitor.visitFrgnInline(self)
            else:
                return visitor.visitChildren(self)


    class ParenLiteralContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.AtomContext
            super().__init__(parser)
            self.paren = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(fds_parser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(fds_parser.RPAREN, 0)
        def LPAREN(self):
            return self.getToken(fds_parser.LPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenLiteral" ):
                return visitor.visitParenLiteral(self)
            else:
                return visitor.visitChildren(self)


    class NumberLiteralContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.AtomContext
            super().__init__(parser)
            self.number = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(fds_parser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberLiteral" ):
                return visitor.visitNumberLiteral(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = fds_parser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                localctx = fds_parser.NumberLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                localctx.number = self.match(fds_parser.NUMBER)
                pass
            elif token in [24]:
                localctx = fds_parser.VarLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                localctx.variable = self.match(fds_parser.VAR)
                pass
            elif token in [29]:
                localctx = fds_parser.FrgnInlineContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                localctx.frgn_inline = self.match(fds_parser.FRGN_INLINE_OPEN)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 152) != 0):
                    self.state = 217
                    localctx._part = self.part()
                    localctx.body.append(localctx._part)
                    self.state = 222
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 223
                self.match(fds_parser.FRGN_INLINE_CLOSE)
                pass
            elif token in [10]:
                localctx = fds_parser.ParenLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 224
                localctx.paren = self.match(fds_parser.LPAREN)
                self.state = 225
                self.expr()
                self.state = 226
                self.match(fds_parser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





