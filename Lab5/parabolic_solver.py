import numpy as np
from tma import tma


class ParabolicSolver:
    def __init__(self, equation, N, K, T):
        self.equation = equation
        self.N, self.K, self.T = N, K, T

        self.h = equation.l / N
        self.tau = T / K
        self.sigma = self.tau / (self.h ** 2)

    def _approximate_first_order_two_point(self, a, b, c, d, u, k):
        # двухточечная аппроксимация с первым порядком
        a[0] = 0
        b[0] = -(1 + 2 * self.sigma)
        c[0] = self.sigma
        d[0] = -(u[k - 1][0] + self.sigma * self.equation.phi_0(k * self.tau))
        a[-1] = self.sigma
        b[-1] = -(1 + 2 * self.sigma)
        c[-1] = 0
        d[-1] = -(u[k - 1][-1] + self.sigma * self.equation.phi_l(k * self.tau))
        return a, b, c, d


    def _approximate_second_order_two_point(self, a, b, c, d, u, k):
        # двухточечная аппроксимация со вторым порядком
        a[0] = 0
        b[0] = -(1 + 2 * self.sigma)
        c[0] = self.sigma
        d[0] = -(u[k - 1][0] + self.sigma * self.equation.phi_0(k * self.tau)) - self.tau * self.equation.f(0,
                                                                                                            k * self.tau)
        a[-1] = self.sigma
        b[-1] = -(1 + 2 * self.sigma)
        c[-1] = 0
        d[-1] = -(u[k - 1][-1] + self.sigma * self.equation.phi_l(k * self.tau)) - self.tau * self.equation.f(
            (self.N - 1) * self.h, k * self.tau)
        return a, b, c, d


    def _approximate_second_order_three_point(self, a, b, c, d, u, k):
        # трехточечная аппроксимация со вторым порядком
        a[0] = 0
        b[0] = -(1 + 2 * self.sigma)
        c[0] = self.sigma
        d[0] = -((1 - self.sigma) * u[k - 1][1] + self.sigma / 2 * u[k - 1][0]) - self.tau * self.equation.f(0,
                                                                                                             k * self.tau) - self.sigma * self.equation.phi_0(
            k * self.tau)
        a[-1] = self.sigma
        b[-1] = -(1 + 2 * self.sigma)
        c[-1] = 0
        d[-1] = self.equation.phi_l(k * self.tau) + self.equation.f((self.N - 1) * self.h, k * self.tau) * self.h / (
                2 * self.tau) * u[k - 1][-1]
        return a, b, c, d


    def solve_analytic(self):
        u = np.zeros((self.K, self.N))
        for k in range(self.K):
            for j in range(self.N):
                u[k][j] = self.equation.solution(j * self.h, k * self.tau)

        return u

    def solve_implicit(self, bound_type):

        a = np.zeros(self.N)
        b = np.zeros(self.N)
        c = np.zeros(self.N)
        d = np.zeros(self.N)
        u = np.zeros((self.K, self.N))
        for i in range(1, self.N - 1):
            u[0][i] = self.equation.psi(i * self.h)
        u[0][-1] = 0

        for k in range(1, self.K):
            for j in range(1, self.N - 1):
                a[j] = self.sigma
                b[j] = -(1 + 2 * self.sigma)
                c[j] = self.sigma
                d[j] = - u[k - 1][j] - self.tau * self.equation.f(j * self.h, k * self.tau)
            if bound_type == 1:
                a, b, c, d = self._approximate_first_order_two_point(a, b, c, d, u, k)
            if bound_type == 2:
                a, b, c, d = self._approximate_second_order_three_point(a, b, c, d, u, k)
            if bound_type == 3:
                a, b, c, d = self._approximate_second_order_two_point(a, b, c, d, u, k)
            u[k] = tma(a, b, c, d)
        return u

    def solve_explicit(self, bound_type):
        u = np.zeros((self.K, self.N))
        for j in range(1, self.N - 1):
            u[0][j] = self.equation.psi(j * self.h)

        for k in range(1, self.K):
            u[k][0] = self.equation.phi_0(k * self.tau)
            for j in range(1, self.N - 1):
                u[k][j] = self.sigma * u[k - 1][j + 1] + \
                          (1 - 2 * self.sigma) * u[k - 1][j] + \
                          self.sigma * u[k - 1][j - 1] + \
                          self.tau * self.equation.f(j * self.h, k * self.tau)

            if bound_type == 1:
                u[k][-1] = u[k][-2] + self.equation.phi_l(k * self.tau) * self.h
            elif bound_type == 2:
                u[k][-1] = self.equation.phi_l(
                    k * self.tau)  # (self.data.phil(k * self.tau) * 2 * self.h - u[k][-3] + 4 * u[k][-2]) / 3
            elif bound_type == 3:
                u[k][-1] = (self.equation.phi_l(k * self.tau) + u[k][-2] / self.h + 2 * self.tau * u[k - 1][
                    -1] / self.h) / (
                                   1 / self.h + 2 * self.tau / self.h)

        return u

    def solve_crank_nicholson(self, bound_type):
        theta = 0.5
        a = np.zeros(self.N)
        b = np.zeros(self.N)
        c = np.zeros(self.N)
        d = np.zeros(self.N)
        u = np.zeros((self.K, self.N))
        for j in range(1, self.N - 1):
            u[0][j] = self.equation.psi(j * self.h)

        for k in range(1, self.K):
            for j in range(1, self.N - 1):
                a[j] = self.sigma
                b[j] = -(1 + 2 * self.sigma)
                c[j] = self.sigma
                d[j] = -u[k - 1][j] - self.tau * self.equation.f(j * self.h, k * self.tau)

            if bound_type == 1:
                a, b, c, d = self._approximate_first_order_two_point(a, b, c, d, u, k)
            if bound_type == 2:
                a, b, c, d = self._approximate_second_order_three_point(a, b, c, d, u, k)
            if bound_type == 3:
                a, b, c, d = self._approximate_second_order_two_point(a, b, c, d, u, k)

            tmp_imp = tma(a, b, c, d)

            tmp_exp = np.zeros(self.N)
            tmp_exp[0] = self.equation.phi_0(self.tau)
            for j in range(1, self.N - 1):
                tmp_exp[j] = self.sigma * u[k - 1][j + 1] + \
                             (1 - 2 * self.sigma) * u[k - 1][j] + \
                             self.sigma * u[k - 1][j - 1] + self.tau * self.equation.f(j * self.h, k * self.tau)
            tmp_exp[-1] = self.equation.phi_l(self.tau)

            for j in range(self.N):
                u[k][j] = theta * tmp_imp[j] + (1 - theta) * tmp_exp[j]

        return u


