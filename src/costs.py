"""
num % 6
0 Chaque metre de papier consomme coute 20 euros
1 Chaque metre de papier consomme coute 120 euros
2 Chaque metre de papier consomme coute 27 euros
3 Chaque metre carre de chute correspond a une perte de 2euros
4 Chaque metre carre de chute correspond a une perte de 11euros
5 Chaque metre carre de chute correspond a une perte de 3euros
"""
costs = [20, 120, 27, 2, 11, 3]

def productionLoss(combination : list, price : int) -> list:
    print(f"Chaque metre de papier consommé coute {price} euros")
    return [(sum([b.price for b in c]) - price) for c in combination]

def fallLoss(combination : list, price : int, max_width : int) -> list:
    print(f"Chaque metre carre de chute correspond a une perte de {price} euros")
    return [(sum([b.price for b in c]) - ((max_width - sum([b.width for b in c])) * 0.01 * price)) for c in combination]

def create_coef(index : int, combination : list, max_width : int) -> list:
    if (index <= 2):
        return productionLoss(combination, costs[index])
    # else
    return fallLoss(combination, costs[index], max_width)