from MatrixDotParser import MatrixDotParser
from MatrixDotVisitor import MatrixDotVisitor

class Matrix:
    def __init__(self, rows, cols, elems):
        self.rows = rows
        self.cols = cols
        self.elems = elems
        self.size = rows * cols

class EvalVisitor(MatrixDotVisitor):
    # expr : dotExpr | matrixLiteral | NUMBER
    def visitProgram(self, ctx:MatrixDotParser.ProgramContext):
        results = []
        for s in ctx.stmt():
            results.append(self.visit(s))
        return results

    def visitStmt(self, ctx:MatrixDotParser.StmtContext):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx:MatrixDotParser.ExprContext):
        if ctx.dotExpr():
            return self.visit(ctx.dotExpr())
        elif ctx.matrixLiteral():
            return self.visit(ctx.matrixLiteral())
        else:
            # NUMBER terminal
            text = ctx.getText()
            if '.' in text:
                return float(text)
            else:
                return int(text)

    def visitDotExpr(self, ctx:MatrixDotParser.DotExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # left/right can be Matrix or scalar (we require matrices)
        if not isinstance(left, Matrix) or not isinstance(right, Matrix):
            raise Exception("dot expects two matrices")
        if left.size != right.size:
            raise Exception(f"Dimensiones incompatibles para dot: {left.rows}x{left.cols} vs {right.rows}x{right.cols}")
        # compute dot (flattened row-major)
        total = 0
        for a,b in zip(left.elems, right.elems):
            total += a*b
        return total

    def visitMatrixLiteral(self, ctx:MatrixDotParser.MatrixLiteralContext):
        rows_ctx = ctx.rowList().row()
        rows = []
        cols_count = None
        elems = []
        for rctx in rows_ctx:
            # each rctx is a RowContext
            # numList optional
            nums = []
            numList = rctx.numList()
            if numList is not None:
                # collect signedNumber tokens
                # each signedNumber is text like -3 or 4.5
                tokens = [n.getText() for n in rctx.numList().signedNumber()]
                for t in tokens:
                    if '.' in t:
                        nums.append(float(t))
                    else:
                        nums.append(int(t))
            # else empty row -> zero columns
            if cols_count is None:
                cols_count = len(nums)
            else:
                if len(nums) != cols_count:
                    raise Exception("Filas con número distinto de columnas en matrix literal")
            elems.extend(nums)
            rows.append(nums)
        if cols_count is None:
            cols_count = 0
        return Matrix(rows=len(rows), cols=cols_count, elems=elems)
