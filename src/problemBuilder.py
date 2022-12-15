from mip import *
from costs import create_coef
from band import Band
# from ine import *
from constraints import manageConstraint, ConstraintType

"""
num % 5
0 245cm
1 283cm
2 255cm
3 271cm
4 292cm
"""
max_widths = [245, 283, 255, 271, 292]

"""
num % 4
0 A : 90cm, B :80cm, C :65cm, D :63cm, E :57cm
1 A : 110cm, B :92cm, C :80cm, D :74cm, E :70cm, F :65cm
2 A : 110cm, B :100cm, C :80cm, D :65cm, E :45cm
3 A : 85cm, B :80cm, C :75cmcm, D :70cm, E :60cm
"""
band_lists = [[90, 80, 65, 63, 57], [110, 92, 80, 74, 70, 65], [110, 100, 80, 65, 45], [85, 80, 75, 70, 60]]

"""
num % 3
0 A :15, B :12, C :10, D :9, E :7 (F :3)
1 A :100, B :80, C :70, D :65, E :60 (F :57)
2 A :15, B :14, C :13, D :16, E :14, (F :13)
"""
price_lists = [[15, 12, 10, 9, 7, 3], [100, 80, 70, 65, 60, 57], [15, 14, 13, 16, 14, 13]]


def combinaisons(plan : int, largeur: int, listeBandes: list, listeSelection: list):
    res = []
    sumSelection = sum([i.width for i in listeSelection])
    if sumSelection > largeur :
        if listeSelection[-2] == plan:
            res = [listeSelection[:-1]]
        else:
            res = []
    elif sumSelection == largeur:
        res = [listeSelection]
    else:
        for i in range(listeBandes.index(plan), len(listeBandes)):
            res += combinaisons(listeBandes[i], largeur, listeBandes, listeSelection + [listeBandes[i]])
    return res


def resolve(ine : int):
    #create model
    m = Model("paper is money", sense=MAXIMIZE)

    #max width
    max_width = max_widths[ine % 5]
    print(f"Largeur totale : {max_width}cm")

    #band list
    band_list = band_lists[ine % 4]
    price_list = price_lists[ine % 3]

    print(f"Largeurs des bandes : {band_list}")
    print(f"Prix par m des bandes : {price_list}")

    bands = []
    for i, b in enumerate(band_list):
        bands.append(Band(chr(ord('A') + i), b, price_list[i]))

    #Find possible combinations
    combination = combinaisons(bands[0], max_width, bands, [])


    #costs
    coef_obj = create_coef(ine % 6, combination, max_width)

    # fill model
    index = range(len(combination))

    varnames = [''.join([str(n) for n in c]) for c in combination]

    var = [m.add_var(v) for v in varnames]

    m.objective = xsum(coef_obj[i] * var[i] for i in index)
    
    # constraints
    constraints = manageConstraint(ine % 7, bands, combination);

    # print(f"max z = {' + '.join([str(coef_obj[i]) + str(name) for i, name in enumerate(varnames)])}")
    # print(f"avec {', '.join(varnames)} >= 0")
    # print("et")
    for c in constraints:
        # print(f"LEN CONSTRAINT : {len(c.coefs)}")
        if c.type == ConstraintType.INF:
            # print(f"{' + '.join([str(c.coefs[i]) + str(name) for i, name in enumerate(varnames)])} <= {c.limit}")
            m += xsum(c.coefs[i] * var[i] for i in index) <= c.limit
        elif c.type == ConstraintType.SUP:
            # print(f"{' + '.join([str(c.coefs[i]) + str(name) for i, name in enumerate(varnames)])} >= {c.limit}")
            m += xsum(c.coefs[i] * var[i] for i in index) >= c.limit
        # THIS CASE SHOULD NEVER HAPPEN BUT YET IS IMPLEMENTED IN CASE OF FUTURE UPDATES
        elif c.type == ConstraintType.EQUAL:
            # print(f"{' + '.join([str(c.coefs[i]) + str(name) for i, name in enumerate(varnames)])} = {c.limit}")
            m += xsum(c.coefs[i] * var[i] for i in index) == c.limit

    # lancement de l'optimisation
    m.optimize()

    if m.status == OptimizationStatus.OPTIMAL:
        #affichage du resultat
        for i in index:
            print(varnames[i] + " = " + str(var[i].x))
        print("bénéfice total :" + str(m.objective_value))
    else:
        print("Pas de solution possible")
    
    """ TESTS
    test = [(name, coef_obj[i]) for i, name in enumerate(varnames)]

    print(len(test))
    for t in test:
        print(t)
    """

if (__name__ == "__main__"):
    # a bunch of tests

    # test léo
    # print("-------------------------- Léo --------------------------")
    # resolve(leo)

    # test lisa
    # print()
    # print("-------------------------- Lisa --------------------------")
    # resolve(lisa)

    # test théo
    # print()
    # print("-------------------------- Théo --------------------------")
    # resolve(theo)

    # test marie
    # print()
    # print("-------------------------- Marie --------------------------")
    # resolve(marie)

    # test liam
    # print()
    # print("-------------------------- Liam --------------------------")
    # resolve(liam)
    pass