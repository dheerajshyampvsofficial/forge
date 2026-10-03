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
        4,1,34,214,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,1,1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,1,5,1,51,8,1,10,1,12,
        1,54,9,1,1,1,1,1,1,1,5,1,59,8,1,10,1,12,1,62,9,1,1,1,1,1,5,1,66,
        8,1,10,1,12,1,69,9,1,1,1,1,1,1,1,1,1,5,1,75,8,1,10,1,12,1,78,9,1,
        1,1,1,1,1,1,5,1,83,8,1,10,1,12,1,86,9,1,1,1,1,1,4,1,90,8,1,11,1,
        12,1,91,1,1,3,1,95,8,1,1,2,1,2,3,2,99,8,2,1,2,5,2,102,8,2,10,2,12,
        2,105,9,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,115,8,4,1,5,1,5,1,
        6,1,6,1,6,5,6,122,8,6,10,6,12,6,125,9,6,1,7,1,7,1,7,5,7,130,8,7,
        10,7,12,7,133,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,142,8,8,1,9,1,
        9,5,9,146,8,9,10,9,12,9,149,9,9,1,9,1,9,5,9,153,8,9,10,9,12,9,156,
        9,9,1,9,1,9,1,9,3,9,161,8,9,1,10,1,10,1,10,5,10,166,8,10,10,10,12,
        10,169,9,10,1,11,1,11,4,11,173,8,11,11,11,12,11,174,1,11,5,11,178,
        8,11,10,11,12,11,181,9,11,1,12,1,12,1,12,5,12,186,8,12,10,12,12,
        12,189,9,12,1,13,4,13,192,8,13,11,13,12,13,193,1,14,1,14,1,15,1,
        15,1,15,1,15,1,15,1,15,3,15,204,8,15,1,16,1,16,4,16,208,8,16,11,
        16,12,16,209,1,16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,0,5,2,0,1,1,20,20,1,0,15,16,1,0,17,18,1,0,21,22,2,
        0,2,2,20,20,228,0,37,1,0,0,0,2,94,1,0,0,0,4,98,1,0,0,0,6,106,1,0,
        0,0,8,108,1,0,0,0,10,116,1,0,0,0,12,118,1,0,0,0,14,126,1,0,0,0,16,
        141,1,0,0,0,18,160,1,0,0,0,20,162,1,0,0,0,22,170,1,0,0,0,24,182,
        1,0,0,0,26,191,1,0,0,0,28,195,1,0,0,0,30,203,1,0,0,0,32,207,1,0,
        0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,
        1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,41,5,0,0,1,41,1,1,0,0,0,42,
        46,5,3,0,0,43,45,5,1,0,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,
        0,46,47,1,0,0,0,47,52,1,0,0,0,48,46,1,0,0,0,49,51,3,2,1,0,50,49,
        1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,
        54,52,1,0,0,0,55,95,5,32,0,0,56,60,5,4,0,0,57,59,5,2,0,0,58,57,1,
        0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,
        60,1,0,0,0,63,67,3,6,3,0,64,66,5,2,0,0,65,64,1,0,0,0,66,69,1,0,0,
        0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,71,
        5,31,0,0,71,95,1,0,0,0,72,76,5,30,0,0,73,75,3,2,1,0,74,73,1,0,0,
        0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,
        1,0,0,0,79,95,5,5,0,0,80,84,5,29,0,0,81,83,3,2,1,0,82,81,1,0,0,0,
        83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,84,1,
        0,0,0,87,95,5,6,0,0,88,90,5,7,0,0,89,88,1,0,0,0,90,91,1,0,0,0,91,
        89,1,0,0,0,91,92,1,0,0,0,92,95,1,0,0,0,93,95,3,4,2,0,94,42,1,0,0,
        0,94,56,1,0,0,0,94,72,1,0,0,0,94,80,1,0,0,0,94,89,1,0,0,0,94,93,
        1,0,0,0,95,3,1,0,0,0,96,99,3,6,3,0,97,99,3,32,16,0,98,96,1,0,0,0,
        98,97,1,0,0,0,99,103,1,0,0,0,100,102,7,0,0,0,101,100,1,0,0,0,102,
        105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,5,1,0,0,0,105,103,
        1,0,0,0,106,107,3,8,4,0,107,7,1,0,0,0,108,114,3,10,5,0,109,110,5,
        13,0,0,110,111,3,8,4,0,111,112,5,14,0,0,112,113,3,8,4,0,113,115,
        1,0,0,0,114,109,1,0,0,0,114,115,1,0,0,0,115,9,1,0,0,0,116,117,3,
        12,6,0,117,11,1,0,0,0,118,123,3,14,7,0,119,120,7,1,0,0,120,122,3,
        14,7,0,121,119,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,
        0,0,0,124,13,1,0,0,0,125,123,1,0,0,0,126,131,3,16,8,0,127,128,7,
        2,0,0,128,130,3,16,8,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,1,
        0,0,0,131,132,1,0,0,0,132,15,1,0,0,0,133,131,1,0,0,0,134,135,7,1,
        0,0,135,142,3,16,8,0,136,137,7,3,0,0,137,142,5,24,0,0,138,139,5,
        24,0,0,139,142,7,3,0,0,140,142,3,18,9,0,141,134,1,0,0,0,141,136,
        1,0,0,0,141,138,1,0,0,0,141,140,1,0,0,0,142,17,1,0,0,0,143,147,5,
        8,0,0,144,146,3,28,14,0,145,144,1,0,0,0,146,149,1,0,0,0,147,145,
        1,0,0,0,147,148,1,0,0,0,148,150,1,0,0,0,149,147,1,0,0,0,150,154,
        3,20,10,0,151,153,3,28,14,0,152,151,1,0,0,0,153,156,1,0,0,0,154,
        152,1,0,0,0,154,155,1,0,0,0,155,157,1,0,0,0,156,154,1,0,0,0,157,
        158,5,9,0,0,158,161,1,0,0,0,159,161,3,30,15,0,160,143,1,0,0,0,160,
        159,1,0,0,0,161,19,1,0,0,0,162,167,3,22,11,0,163,164,5,25,0,0,164,
        166,3,22,11,0,165,163,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,
        168,1,0,0,0,168,21,1,0,0,0,169,167,1,0,0,0,170,179,3,24,12,0,171,
        173,7,4,0,0,172,171,1,0,0,0,173,174,1,0,0,0,174,172,1,0,0,0,174,
        175,1,0,0,0,175,176,1,0,0,0,176,178,3,24,12,0,177,172,1,0,0,0,178,
        181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,23,1,0,0,0,181,179,
        1,0,0,0,182,187,3,26,13,0,183,184,5,26,0,0,184,186,3,26,13,0,185,
        183,1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,
        25,1,0,0,0,189,187,1,0,0,0,190,192,3,6,3,0,191,190,1,0,0,0,192,193,
        1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,27,1,0,0,0,195,196,5,
        2,0,0,196,29,1,0,0,0,197,204,5,23,0,0,198,204,5,24,0,0,199,200,5,
        10,0,0,200,201,3,6,3,0,201,202,5,11,0,0,202,204,1,0,0,0,203,197,
        1,0,0,0,203,198,1,0,0,0,203,199,1,0,0,0,204,31,1,0,0,0,205,206,5,
        24,0,0,206,208,5,12,0,0,207,205,1,0,0,0,208,209,1,0,0,0,209,207,
        1,0,0,0,209,210,1,0,0,0,210,211,1,0,0,0,211,212,3,6,3,0,212,33,1,
        0,0,0,25,37,46,52,60,67,76,84,91,94,98,103,114,123,131,141,147,154,
        160,167,174,179,187,193,203,209
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "'|'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'}'" ]

    symbolicNames = [ "<INVALID>", "NEWLINE", "NL", "FDS_BLOCK_OPEN", "FDS_INLINE_OPEN", 
                      "FRGN_BLOCK_CLOSE", "FRGN_INLINE_CLOSE", "FRGN_CODE", 
                      "MLBRACE", "MRBRACE", "LPAREN", "RPAREN", "EQUALS", 
                      "QMARK", "COLON", "PLUS", "MINUS", "STAR", "SLASH", 
                      "COMMA", "SEMI_COLON", "INC", "DEC", "NUMBER", "VAR", 
                      "M_HSEP", "M_VBAR", "NEWLINE_OR_NL", "WS", "FRGN_INLINE_OPEN", 
                      "FRGN_BLOCK_OPEN", "FDS_INLINE_CLOSE", "FDS_BLOCK_CLOSE", 
                      "ERROR", "FRGN_RBRACE" ]

    RULE_start = 0
    RULE_part = 1
    RULE_simple_stmt = 2
    RULE_expr = 3
    RULE_ternary_expr = 4
    RULE_binary_expr = 5
    RULE_addition = 6
    RULE_multiplication = 7
    RULE_unary_sign = 8
    RULE_matrix = 9
    RULE_matrix_rows = 10
    RULE_block_row = 11
    RULE_matrix_row = 12
    RULE_matrix_cell = 13
    RULE_matrix_inner_ignores = 14
    RULE_atom = 15
    RULE_assignment = 16

    ruleNames =  [ "start", "part", "simple_stmt", "expr", "ternary_expr", 
                   "binary_expr", "addition", "multiplication", "unary_sign", 
                   "matrix", "matrix_rows", "block_row", "matrix_row", "matrix_cell", 
                   "matrix_inner_ignores", "atom", "assignment" ]

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
    FRGN_RBRACE=34

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
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1642169752) != 0):
                self.state = 34
                localctx._part = self.part()
                localctx.parts.append(localctx._part)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
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



    class FrgnTextContext(PartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.PartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FRGN_CODE(self, i:int=None):
            if i is None:
                return self.getTokens(fds_parser.FRGN_CODE)
            else:
                return self.getToken(fds_parser.FRGN_CODE, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFrgnText" ):
                return visitor.visitFrgnText(self)
            else:
                return visitor.visitChildren(self)


    class FrgnBlockContext(PartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.PartContext
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
            if hasattr( visitor, "visitFrgnBlock" ):
                return visitor.visitFrgnBlock(self)
            else:
                return visitor.visitChildren(self)


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


    class FdsBlockContext(PartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.PartContext
            super().__init__(parser)
            self._part = None # PartContext
            self.body = list() # of PartContexts
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
        def part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fds_parser.PartContext)
            else:
                return self.getTypedRuleContext(fds_parser.PartContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFdsBlock" ):
                return visitor.visitFdsBlock(self)
            else:
                return visitor.visitChildren(self)


    class FrgnInlineContext(PartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.PartContext
            super().__init__(parser)
            self._part = None # PartContext
            self.body = list() # of PartContexts
            self.copyFrom(ctx)

        def FRGN_INLINE_OPEN(self):
            return self.getToken(fds_parser.FRGN_INLINE_OPEN, 0)
        def FRGN_INLINE_CLOSE(self):
            return self.getToken(fds_parser.FRGN_INLINE_CLOSE, 0)
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


    class StmtContext(PartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.PartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simple_stmt(self):
            return self.getTypedRuleContext(fds_parser.Simple_stmtContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)



    def part(self):

        localctx = fds_parser.PartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_part)
        self._la = 0 # Token type
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = fds_parser.FdsBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(fds_parser.FDS_BLOCK_OPEN)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 43
                    self.match(fds_parser.NEWLINE)
                    self.state = 48
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1642169752) != 0):
                    self.state = 49
                    localctx._part = self.part()
                    localctx.body.append(localctx._part)
                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 55
                self.match(fds_parser.FDS_BLOCK_CLOSE)
                pass
            elif token in [4]:
                localctx = fds_parser.FdsInlineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(fds_parser.FDS_INLINE_OPEN)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 57
                    self.match(fds_parser.NL)
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 63
                localctx.value = self.expr()
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
                self.match(fds_parser.FDS_INLINE_CLOSE)
                pass
            elif token in [30]:
                localctx = fds_parser.FrgnBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.match(fds_parser.FRGN_BLOCK_OPEN)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1642169752) != 0):
                    self.state = 73
                    localctx._part = self.part()
                    localctx.body.append(localctx._part)
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 79
                self.match(fds_parser.FRGN_BLOCK_CLOSE)
                pass
            elif token in [29]:
                localctx = fds_parser.FrgnInlineContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 80
                self.match(fds_parser.FRGN_INLINE_OPEN)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1642169752) != 0):
                    self.state = 81
                    localctx._part = self.part()
                    localctx.body.append(localctx._part)
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 87
                self.match(fds_parser.FRGN_INLINE_CLOSE)
                pass
            elif token in [7]:
                localctx = fds_parser.FrgnTextContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 89 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 88
                        self.match(fds_parser.FRGN_CODE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 91 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass
            elif token in [8, 10, 15, 16, 21, 22, 23, 24]:
                localctx = fds_parser.StmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 93
                self.simple_stmt()
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
            self.expression = None # ExprContext
            self.assign = None # AssignmentContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(fds_parser.ExprContext,0)

        def assignment(self):
            return self.getTypedRuleContext(fds_parser.AssignmentContext,0)

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
        self.enterRule(localctx, 4, self.RULE_simple_stmt)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.SimpleStatementContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 96
                localctx.expression = self.expr()
                pass

            elif la_ == 2:
                self.state = 97
                localctx.assign = self.assignment()
                pass


            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==20:
                self.state = 100
                _la = self._input.LA(1)
                if not(_la==1 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            localctx = fds_parser.ExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 106
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
        self.enterRule(localctx, 8, self.RULE_ternary_expr)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.TernaryExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            localctx.left = self.binary_expr()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 109
                self.match(fds_parser.QMARK)
                self.state = 110
                localctx.middle = self.ternary_expr()
                self.state = 111
                self.match(fds_parser.COLON)
                self.state = 112
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
        self.enterRule(localctx, 10, self.RULE_binary_expr)
        try:
            localctx = fds_parser.BinaryExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 116
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
            self._tset243 = None # Token
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
        self.enterRule(localctx, 12, self.RULE_addition)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.AddExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            localctx.left = self.multiplication()
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 119
                    localctx._tset243 = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==16):
                        localctx._tset243 = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    localctx.ops.append(localctx._tset243)
                    self.state = 120
                    localctx._multiplication = self.multiplication()
                    localctx.rights.append(localctx._multiplication) 
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
            self._tset280 = None # Token
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
        self.enterRule(localctx, 14, self.RULE_multiplication)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.MulExpressionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            localctx.left = self.unary_sign()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 127
                localctx._tset280 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    localctx._tset280 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.ops.append(localctx._tset280)
                self.state = 128
                localctx._unary_sign = self.unary_sign()
                localctx.rights.append(localctx._unary_sign)
                self.state = 133
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
        self.enterRule(localctx, 16, self.RULE_unary_sign)
        self._la = 0 # Token type
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = fds_parser.UnarySignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                localctx.sign = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    localctx.sign = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 135
                localctx.operand = self.unary_sign()
                pass

            elif la_ == 2:
                localctx = fds_parser.PreIncDecContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 137
                localctx.variable = self.match(fds_parser.VAR)
                pass

            elif la_ == 3:
                localctx = fds_parser.PostIncDecContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                localctx.variable = self.match(fds_parser.VAR)
                self.state = 139
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
                self.state = 140
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
        self.enterRule(localctx, 18, self.RULE_matrix)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = fds_parser.MatrixLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(fds_parser.MLBRACE)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 144
                    self.matrix_inner_ignores()
                    self.state = 149
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 150
                localctx.rows = self.matrix_rows()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 151
                    self.matrix_inner_ignores()
                    self.state = 156
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 157
                self.match(fds_parser.MRBRACE)
                pass
            elif token in [10, 23, 24]:
                localctx = fds_parser.AtomLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 159
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixRows" ):
                return visitor.visitMatrixRows(self)
            else:
                return visitor.visitChildren(self)



    def matrix_rows(self):

        localctx = fds_parser.Matrix_rowsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_matrix_rows)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.MatrixRowsContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            localctx._block_row = self.block_row()
            localctx.groups.append(localctx._block_row)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 163
                self.match(fds_parser.M_HSEP)
                self.state = 164
                localctx._block_row = self.block_row()
                localctx.groups.append(localctx._block_row)
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 22, self.RULE_block_row)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.BlockRowContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            localctx._matrix_row = self.matrix_row()
            localctx.lines.append(localctx._matrix_row)
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 172 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 171
                        _la = self._input.LA(1)
                        if not(_la==2 or _la==20):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 174 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==2 or _la==20):
                            break

                    self.state = 176
                    localctx._matrix_row = self.matrix_row()
                    localctx.lines.append(localctx._matrix_row) 
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self.enterRule(localctx, 24, self.RULE_matrix_row)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.MatrixRowContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            localctx._matrix_cell = self.matrix_cell()
            localctx.cells.append(localctx._matrix_cell)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 183
                self.match(fds_parser.M_VBAR)
                self.state = 184
                localctx._matrix_cell = self.matrix_cell()
                localctx.cells.append(localctx._matrix_cell)
                self.state = 189
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
        self.enterRule(localctx, 26, self.RULE_matrix_cell)
        self._la = 0 # Token type
        try:
            localctx = fds_parser.MatrixCellContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 191 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 190
                localctx._expr = self.expr()
                localctx.elements.append(localctx._expr)
                self.state = 193 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 31556864) != 0)):
                    break

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
        self.enterRule(localctx, 28, self.RULE_matrix_inner_ignores)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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


    class ParenLiteralContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a fds_parser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(fds_parser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(fds_parser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(fds_parser.RPAREN, 0)

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
        self.enterRule(localctx, 30, self.RULE_atom)
        try:
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                localctx = fds_parser.NumberLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                localctx.number = self.match(fds_parser.NUMBER)
                pass
            elif token in [24]:
                localctx = fds_parser.VarLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                localctx.variable = self.match(fds_parser.VAR)
                pass
            elif token in [10]:
                localctx = fds_parser.ParenLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.match(fds_parser.LPAREN)
                self.state = 200
                self.expr()
                self.state = 201
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
        self.enterRule(localctx, 32, self.RULE_assignment)
        try:
            localctx = fds_parser.AssignmentStmtContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 207 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 205
                    localctx._VAR = self.match(fds_parser.VAR)
                    localctx.targets.append(localctx._VAR)
                    self.state = 206
                    self.match(fds_parser.EQUALS)

                else:
                    raise NoViableAltException(self)
                self.state = 209 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 211
            localctx.value = self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





