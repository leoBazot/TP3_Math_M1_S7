from band import Band
from enum import Enum

class ConstraintType(Enum):
    INF = 0     # <=
    EQUAL = 1   # =
    SUP = 2     # >=

class Constraint:
    def __init__(self, coefs : list, type : ConstraintType, limit : int):
        self.coefs = coefs
        self.type = type
        self.limit = limit



# C1 maximum length of paper is 1000m
def constraint1(bands : list[Band], combination : list[Band]) -> list[Constraint]:
    return [Constraint([1 for _ in combination], ConstraintType.INF, 1000)]


# C2 Ne pas produire plus de 400m de chaque bande (A,B,C,D,E,(F))
def constraint2(bands : list[Band], combination : list[Band]) -> list[Constraint]:
    coefs = []
    for b in bands:
        coefs.append([c.count(b) for c in combination])
    return [Constraint(c, ConstraintType.INF, 400) for c in coefs]


# C3 Aucune bande ne peut representer plus de 50% de la longueur de bandes totales produites
def constraint3(bands : list[Band], combination : list[Band]) -> list[Constraint]:
    coefs = []
    for b in bands:
        coefs.append([(c.count(b) - (0,5 * len(c))) for c in combination])
    return [Constraint(c, ConstraintType.INF, 0) for c in coefs]


# C4 Il faut produire assez de chaque bande pour honorer les commandes : A :200m, B :150m, C :215m, D :180m, E :150m (F :100m).
def constraint4(bands : list[Band], combination : list[Band]) -> list[Constraint]:
    commands = [200, 150, 215, 180, 150, 100]
    return [Constraint([c.count(b) for c in combination], ConstraintType.SUP, commands[i]) for i, b in enumerate(bands)]


# C5 La quantite totale produide de bande A additionnee a celle de la bande C ne doit pas d ́epasser 750m.
def constraint5(bands : list[Band], combination : list[Band]) -> list[Constraint]:
    return [Constraint([c.count(bands[0]) + c.count(bands[2]) for c in combination], ConstraintType.INF, 750)]


# C6 Il faut au moins produire 100m de plus de la bande A que de la bande C
def constraint6(bands : list[Band], combination : list[Band]) -> list[Constraint]:
    return [Constraint([c.count(bands[0]) - c.count(bands[2]) for c in combination], ConstraintType.SUP, 100)]



"""
num  7
0 C1, C3 et C5
1 C2, C3 et C5
2 C1, C4 et C5
3 C2, C4 et C5
4 C1, C3 et C6
5 C2, C3 et C6
6 C1, C4 et C6
"""
def manageConstraint(num : int, bands : list[Band], combination : list[Band]) -> list[Constraint]:
    if num == 0:
        return constraint1(bands, combination) + constraint3(bands, combination) + constraint5(bands, combination)
    elif num == 1:
        return constraint2(bands, combination) + constraint3(bands, combination) + constraint5(bands, combination)
    elif num == 2:
        return constraint1(bands, combination) + constraint4(bands, combination) + constraint5(bands, combination)
    elif num == 3:
        return constraint2(bands, combination) + constraint4(bands, combination) + constraint5(bands, combination)
    elif num == 4:
        return constraint1(bands, combination) + constraint3(bands, combination) + constraint6(bands, combination)
    elif num == 5:
        return constraint2(bands, combination) + constraint3(bands, combination) + constraint6(bands, combination)
    elif num == 6:
        return constraint1(bands, combination) + constraint4(bands, combination) + constraint6(bands, combination)
    # else
    return []