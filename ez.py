from problemBuilder import resolve

def lazyStudent(ine : int):
    try:
        ine = int(input('Donne ton numéro étudiant je te résout tout ça !'))
    except ValueError:
        print('Le numéro étudiant ne contiens aucune lettre (numéro de dossier sur l\'ent')
        return
    resolve(ine)