from problemBuilder import resolve


try:
    ine = int(input('Donne ton numéro étudiant je te résout tout ça !\n> '))
    resolve(ine)
except ValueError:
    print('Le numéro étudiant ne contiens aucune lettre (numéro de dossier sur l\'ent')