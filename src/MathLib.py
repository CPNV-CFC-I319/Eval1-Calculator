class MathLib:

    @classmethod
    def execute(self, mathRequest):
        oper = mathRequest.get_oper()
        ope1 = mathRequest.get_ope1()
        ope2 = mathRequest.get_ope2()

        if(oper == 'add'):
            res = ope1 + ope2
            mathRequest.set_res(res)

        if (oper == 'div'):
            res = ope1 / ope2
            mathRequest.set_res(res)