import numpy as np
import matplotlib.pyplot as plt


class Shape:
    @staticmethod
    def square():
        x1 = np.concatenate(
            (
                np.linspace(0, 1, 100),
                np.ones(100),
                np.linspace(0, 1, 100),
                np.zeros(100),
            )
        )
        y1 = np.concatenate(
            (
                np.zeros(100),
                np.linspace(0, 1, 100),
                np.ones(100),
                np.linspace(0, 1, 100),
            )
        )
        return x1, y1

    @staticmethod
    def triangle():
        x1 = np.concatenate(
            (
                np.linspace(0, 1, 100),
                np.linspace(1, 0.5, 100),
                np.linspace(0.5, 0, 100),
            )
        )
        y1 = np.concatenate(
            (np.zeros(100), np.linspace(0, 1, 100), np.linspace(1, 0, 100))
        )
        return x1, y1

    @staticmethod
    def line():
        x1 = np.linspace(0, 1, 100)
        y1 = np.zeros(100)
        return x1, y1


class Ifs:
    def __init__(self):
        self._equationList = []

    def AddEquations(self, EqnLst):
        self.size = len(EqnLst[0])
        Output = all(len(elem) == self.size for elem in EqnLst)
        if Output:

            if self.size == 6:
                for eqn in EqnLst:
                    *coef, e, f = eqn
                    self._equationList.append(
                        (np.array(coef), np.array([e, f]))
                    )
            elif self.size == 7:
                for eqn in EqnLst:
                    *coef, e, f, p = eqn
                    self._equationList.append(
                        (np.array(coef), np.array([e, f]), p)
                    )
            else:
                raise ValueError("Ifs's length can only be 6 or 7")
        else:
            raise ValueError("unequal length of ifs's")

    def __str__(self):
        if self._equationList == []:
            print("object is empty")
        if self.size == 6:

            out = ""
            for idx, (coef, intercept) in enumerate(self._equationList, 1):
                a, b, c, d = coef
                e, f = intercept
                out = (
                    out
                    + f"""equation = {idx}: [[a = {a} b = {b}]   [e = {e}
	      [c = {c} d = {d}]]   f = {f}]\n\n"""
                )
            return out
        else:
            out = ""
            for idx, (coef, intercept, probability) in enumerate(
                self._equationList, 1
            ):
                a, b, c, d = coef
                e, f = intercept
                p = probability
                out = (
                    out
                    + f"""equation = {idx}: [[a = {a} b = {b}]   [[e = {e}]  p={p}
	       [c = {c} d = {d}]]   [f = {f}]]\n\n"""
                )
            return out

    def deterministic(self, shape=Shape.square(), iterations=6):

        if len(self._equationList[0]) == 3:
            raise ValueError("Deterministic only accepts ifs's of size 6")

        if len(shape[0]) != len(shape[1]):
            raise ValueError(
                "x co-ordinates and y co-ordinates should be equal"
            )

        if len(shape) != 2:
            raise ValueError("Invalid co-ordinate format")

        arr = np.column_stack(shape)
        for i in range(iterations):
            allEquations = []
            for coef, intercept in self._equationList:
                coef_ = coef.reshape(-1, 2)
                transformed_arr = (coef_ * arr[:, None]).sum(
                    axis=2
                ) + intercept[None, :]
                allEquations.append(transformed_arr)
            arr = np.vstack(allEquations)
        self._coords = arr
        return arr

    def randomIteration(self, iterations=20000):

        if len(self._equationList[0]) == 2:
            raise ValueError("Random Iteration only accepts Ifs's of size 7")

        total_prob = 0
        for _, _, prob in self._equationList:
            total_prob += prob

        if abs(total_prob - 1) > 0.05:
            raise ValueError("Total probability of Ifs's must be equal to 1")

        x = 1
        y = 1
        arr = []
        x1 = 0
        y1 = 0
        for t in range(iterations):
            rand = np.random.random()
            for coef, intercept, probability in self._equationList:
                if rand < probability and not rand <= 0:
                    [[x1], [y1]] = np.matmul(
                        coef.reshape(-1, 2), np.array([[x], [y]])
                    ) + intercept.reshape(-1, 1)
                    arr.append([x1, y1])
                    x, y = x1, y1
                rand = rand - probability

        arr = np.array(arr)
        self._coords = arr
        return arr

    def plot(self):
        x, y = zip(*self._coords)
        plt.scatter(x, y, 1, "g")
        plt.show()

