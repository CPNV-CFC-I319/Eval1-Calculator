class MathLib:

    @classmethod
    def execute(self, mathRequest):
        if(mathRequest.get_oper() == '+'):
            mathRequest.set_res(mathRequest.get_ope1() + mathRequest.get_ope2())