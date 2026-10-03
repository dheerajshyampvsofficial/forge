# Generated from /Users/dheerajshyampvs/PythonProjects/forge/compiler/frontend/gen_script/fds_parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .fds_parser import fds_parser
else:
    from fds_parser import fds_parser

# This class defines a complete generic visitor for a parse tree produced by fds_parser.

class fds_parserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by fds_parser#Parts.
    def visitParts(self, ctx:fds_parser.PartsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#FdsBlock.
    def visitFdsBlock(self, ctx:fds_parser.FdsBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#FdsInline.
    def visitFdsInline(self, ctx:fds_parser.FdsInlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#FrgnBlock.
    def visitFrgnBlock(self, ctx:fds_parser.FrgnBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#FrgnInline.
    def visitFrgnInline(self, ctx:fds_parser.FrgnInlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#FrgnText.
    def visitFrgnText(self, ctx:fds_parser.FrgnTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#Stmt.
    def visitStmt(self, ctx:fds_parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#SimpleStatement.
    def visitSimpleStatement(self, ctx:fds_parser.SimpleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#Expression.
    def visitExpression(self, ctx:fds_parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#TernaryExpression.
    def visitTernaryExpression(self, ctx:fds_parser.TernaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#BinaryExpression.
    def visitBinaryExpression(self, ctx:fds_parser.BinaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#AddExpression.
    def visitAddExpression(self, ctx:fds_parser.AddExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#MulExpression.
    def visitMulExpression(self, ctx:fds_parser.MulExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#UnarySign.
    def visitUnarySign(self, ctx:fds_parser.UnarySignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#PreIncDec.
    def visitPreIncDec(self, ctx:fds_parser.PreIncDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#PostIncDec.
    def visitPostIncDec(self, ctx:fds_parser.PostIncDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#UnaryValue.
    def visitUnaryValue(self, ctx:fds_parser.UnaryValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#MatrixLiteral.
    def visitMatrixLiteral(self, ctx:fds_parser.MatrixLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#AtomLiteral.
    def visitAtomLiteral(self, ctx:fds_parser.AtomLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#MatrixRows.
    def visitMatrixRows(self, ctx:fds_parser.MatrixRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#BlockRow.
    def visitBlockRow(self, ctx:fds_parser.BlockRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#MatrixRow.
    def visitMatrixRow(self, ctx:fds_parser.MatrixRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#MatrixCell.
    def visitMatrixCell(self, ctx:fds_parser.MatrixCellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#matrix_inner_ignores.
    def visitMatrix_inner_ignores(self, ctx:fds_parser.Matrix_inner_ignoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#NumberLiteral.
    def visitNumberLiteral(self, ctx:fds_parser.NumberLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#VarLiteral.
    def visitVarLiteral(self, ctx:fds_parser.VarLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#ParenLiteral.
    def visitParenLiteral(self, ctx:fds_parser.ParenLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fds_parser#AssignmentStmt.
    def visitAssignmentStmt(self, ctx:fds_parser.AssignmentStmtContext):
        return self.visitChildren(ctx)



del fds_parser