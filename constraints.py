from band import Band


# C1 maximum length of paper is 1000m
def constraint1(combination : list) -> tuple(list, int):




# C3 chanque bandes doit représenter moins de 50% du total des bandes
def constraint3(combination : list[Band]):
    for i, c in enumerate(combination):
        coef_prime = sum([liste_bandes[b] for b in c])
        m += xsum(coef_prime[i] * var[i] for i in index) >= quantite