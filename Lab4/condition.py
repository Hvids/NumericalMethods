TYPE_A = 'A'
TYPE_B = 'B'


class Condition:
    def __init__(self, alpha, betta, rhs, type_c,y,dy):
        self.alpha = alpha
        self.betta = betta
        self.rhs = rhs
        self.type = type_c
        self.fomula = alpha*y + betta*dy

    def F(self,dict_s):
        return self.fomula.subs(dict_s).evalf() - self.rhs

    def get_y(self,dy):
        if not self.alpha == 0:
            return (self.rhs - dy*self.betta)/self.alpha
        if self.alpha == 0:
            raise NameError('Not solve fo me')
    def get_dy(self,y):
        if not self.betta == 0:
            return (self.rhs - y*self.alpha)/self.betta
        if self.betta == 0:
            raise NameError('Not solve for me')

    def make_diff(self, step, order=1):
        if self.type == TYPE_A:
            res = self.__make_diff_for_A(step, order)
        else:
            res = self.__make_diff_for_B(step, order)
        return res

    def __make_diff_for_A(self, h, order):
        if order == 1:
            res = [self.alpha - self.betta / h, self.betta / h]
        else:
            res = [self.alpha - 3 * self.betta / (2 * h), +4 * self.betta / (2 * h), -1 * self.betta / (2 * h)]
        return res

    def __make_diff_for_B(self, h, order):
        if order == 1:
            res = [-self.betta / h, self.alpha + self.betta / h]
        else:
            res = [self.betta / (2 * h), -3 * self.betta / (2 * h), self.alpha + 3 * self.betta / (2 * h)]
        return res


class CondtionShooting:
    def __init__(self,f, rhs):
        self.f = f
        self.rhs
    def subs(self, x):
        return self.f.subs(x)


if __name__=='__main__':
    alpha, betta, y_0 = 1, 0, 1
    delta, gamma, y_1 = 2, 1, 0
    h = 0.2
    cond1 = Condition(alpha, betta, y_0, TYPE_A)
    cond2 = Condition(delta, gamma, y_1, TYPE_B)
    print(f'{cond1.make_diff(h)} == {[1.0,0]}\n{cond2.make_diff(h)} == {[-5,7]}')
