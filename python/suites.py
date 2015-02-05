class Suite:
    def __init__(self, s_function):
        self.sequel_function = s_function
        pass

    def converge(self, seuil=5, lim=10000):
        iterator = self.sequel_function()
        matching = 1
        nb_iterations = 1
        current_number = next(iterator)
        for i in iterator:
            nb_iterations += 1
            if i == current_number:
                matching += 1
                if matching == seuil:
                    return nb_iterations - seuil + 1, current_number
                else:
                    continue
            else:
                matching = 1
                current_number = i

            lim -= 1
            if lim == 0:
                break

        return None

    def display(self, n):
        """
            Retourne une liste contenant les n premiers éléments de la suite
        """
        iterator = self.sequel_function()

        ret = []
        for i in iterator:
            if n == 0:
                break
            ret.append(i)
            n -= 1

        return ret


def generate_list(l):
    """
        Returns a function that yields each element of the given list
    """

    def generator():
        liste = l
        for i in liste:
            yield i

    return generator

