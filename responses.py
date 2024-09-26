
from random import choice, randint
import re


# idées de dialogues possibles avec le bot:
'''
* WarpBot stuff element classe
    - element : terre/feu/eau/air/dopou
    - classe : logique poto
pourquoi pas rajouter une manière de spécifier docri/12pa 6pm/etc
l'idée est de renvoyer un message avec la présentation des stuff classiques ou spécifiques à chaque classe selon ce que la personne a mis comme info

* WarpBot calcul invo dofusbook
    - invo : dragonnet/momie/bouftou/craqueleur/sanglier/tofu
    - dofusbook : lien d'un stuff dofusbook (ex : https://d-bk.net/fr/t/9nwN )
l'idée est d'envoyer le calcul des dégats des sorts de l'invo en question par le stuff en question

* WarpBot stream
donne les infos sur les prochains stream que je vais faire
'''


'''
idée présentation stuffs : dict avec tous les elements/modes + toutes les classes
chaque element du dict c'est un dict
quand une classe ne contient pas l'element on dit "j'ai pas de scpécifique mais voici les bases de cet element"
bi elem écris de la maniere suivante "terre+feu" mais rangés par ordre alphabétique, histoire de pouvoir créer facilement la string 
'''
ELEMENTS=['terre', 'feu', 'eau', 'air', 'dopou', 'feu+terre', 'eau+terre', 
          'air+terre', 'dopou+terre', 'eau+feu', 'air+feu', 'dopou+feu', 
          'air+eau', 'dopou+eau', 'air+dopou', 'air+eau+terre', 'air+eau+feu', 
          'air+feu+terre', 'eau+feu+terre', 'air+dopou+eau', 'air+dopou+terre', 
          'dopou+feu+terre', 'air+dopou+feu', 'dopou+eau+feu', 'dopou+eau+terre', 
          'multi','',False]
CLASSES=['xelor', 'enutrof', 'eniripsa', 'osamodas', 'zobal', 'sadida',
       'steamer', 'sacrieur', 'iop', 'pandawa', 'ecaflip', 'cra', 'feca',
       'sram', 'roublard','',False]
#dans elements et classes je rajoute vide et faux pour prendre en compte les cas où on ne remplis pas l'argument de l'un des deux, ça peut être normal

stuffs=dict()

stuffs["terre"]={'12/6': ["<https://d-bk.net/fr/t/8vYb>"], '11/6': ["<https://d-bk.net/fr/t/9WxC>"], 'cc': [], 'no_cc': []}
stuffs["feu"]={'12/6': ["<https://d-bk.net/fr/t/A8Zv>"], '11/6': ["<https://d-bk.net/fr/t/8yAu>"], 'cc': [], 'no_cc': []}
stuffs["eau"]={'12/6': ["<https://d-bk.net/fr/t/B7er>"], '11/6': ["<https://d-bk.net/fr/t/B9MR>"], 'cc': [], 'no_cc': []}
stuffs["air"]={'12/6': ["<https://d-bk.net/fr/t/5qJF>"], '11/6': ["<https://d-bk.net/fr/t/9RJp>"], 'cc': [], 'no_cc': []}
# stuffs["dopou"]={'12/6': [], '11/6': [], 'cc': [], 'no_cc': []} ### Dopou is always with another element
stuffs["feu+terre"]={'12/6': [], '11/6': [], 'cc': ["<https://d-bk.net/fr/t/7ESW>"], 'no_cc': ["<https://d-bk.net/fr/t/AwSG>"]}
stuffs["eau+terre"]={'12/6': [], '11/6': ["<https://d-bk.net/fr/t/Azb9>"], 'cc': [], 'no_cc': []}
# stuffs["air+terre"]={'12/6': [], '11/6': [], 'cc': [], 'no_cc': []}
# stuffs["dopou+terre"]={'12/6': [], '11/6': [], 'cc': [], 'no_cc': []}
stuffs["eau+feu"]={'12/6': [], '11/6': ["<https://d-bk.net/fr/t/931X>"], 'cc': [], 'no_cc': []}
stuffs["air+feu"]={'12/6': [], '11/6': [], 'cc': ["<https://d-bk.net/fr/t/7OhS>"], 'no_cc': []}
# stuffs["dopou+feu"]={'12/6': [], '11/6': [], 'cc': [], 'no_cc': []}
stuffs["air+eau"]={'12/6': ["<https://d-bk.net/fr/t/8Ql4>"], '11/6': ["<https://d-bk.net/fr/t/BMXD>"], 'cc': [], 'no_cc': []}
stuffs["dopou+eau"]={'12/6': [], '11/6': ["<https://d-bk.net/fr/t/AzPu>"], 'cc': [], 'no_cc': []}
stuffs["air+dopou"]={'12/6': [], '11/6': ["<https://d-bk.net/fr/t/BK5m>"], 'cc': [], 'no_cc': []}
stuffs["air+eau+terre"]={'12/6': [], '11/6': ["<https://d-bk.net/fr/t/2OhT>"], 'cc': [], 'no_cc': []}
stuffs["air+eau+feu"]={'12/6': [], '11/6': [], 'cc': ["<https://d-bk.net/fr/t/2OhM>"], 'no_cc': ["<https://d-bk.net/fr/t/BQYM>"]}
stuffs["air+feu+terre"]={'12/6': [], '11/6': [], 'cc': ["<https://d-bk.net/fr/t/4qgX>"], 'no_cc': ["<https://d-bk.net/fr/t/AP7x>"]}
stuffs["eau+feu+terre"]={'12/6': [], '11/6': [], 'cc': ["<https://d-bk.net/fr/t/47TD>"], 'no_cc': []}
stuffs["air+dopou+eau"]={'12/6': [], '11/6': ["<https://d-bk.net/fr/t/A9Iy>"], 'cc': [], 'no_cc': []}
# stuffs["air+dopou+terre"]={'12/6': [], '11/6': [], 'cc': [], 'no_cc': []}
# stuffs["dopou+feu+terre"]={'12/6': [], '11/6': [], 'cc': [], 'no_cc': []}
# stuffs["air+dopou+feu"]={'12/6': [], '11/6': [], 'cc': [], 'no_cc': []}
stuffs["dopou+eau+feu"]={'12/6': [], '11/6': ["<https://d-bk.net/fr/t/BQQd>"], 'cc': [], 'no_cc': []}
stuffs["dopou+eau+terre"]={'12/6': [], '11/6': ["<https://d-bk.net/fr/t/BQQl>"], 'cc': [], 'no_cc': []}
stuffs["multi"]={'12/6': [], '11/6': [], 'cc': ["<https://d-bk.net/fr/t/2Ol7>"], 'no_cc': []}
stuffs["osamodas"]={'feu' :{'12/6' :["<https://d-bk.net/fr/t/9nwN>"]}, 'eau+feu':{'cher' : ["<https://d-bk.net/fr/t/9UXA>"],'plus abordable' : ["<https://d-bk.net/fr/t/AQSn>"]}}

#prend une liste d'éléments et la met sous la forme elt1+elt2+elt3...
def from_elts_to_multi(elt_list):
    sorted_list=sorted(elt_list)
    return '+'.join(sorted_list)

#prends les éléments sous le format elt1+elt2+elt3... et les remet dans le bon ordre
def rearrange_elt(elts):
    elt_spl=elts.split("+")
    return from_elts_to_multi(elt_spl)

def get_response(user_input: str, user_name : str, channel : str):
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Ok tu arrive à envoyer des messages vides?? Sorcier!'
    elif lowered =='salut warpbot' :
        return f'Salut {user_name}!'
    elif lowered =='!warpbot lance un dé' or lowered =='!wb lance un dé':
        return f'Tu as eu: {randint(1, 6)}'
    elif command :=re.match(r"(?P<botname>!\w+) (?P<function>\w+)\s?(?P<arg1>[+\w]*)\s?(?P<arg2>[a-z0-9\/\.\-:]*)", lowered):
        print(command.group('botname'),command.group('function'),command.group('arg1'),command.group('arg2'))
        if command.group('botname')!= '!warpbot' and command.group('botname')!= '!wb':
            return -1
        
        if command.group('function')=="stuff":
            element = command.group('arg1')
            classe = command.group('arg2')
            # print(element,classe)
            return stuff_response(element=element,classe=classe)
        
        elif command.group('function')=="calcul":
            return "ça fait 13 frelon"
        else:
            resp= f"""
Argument **{command.group('function')}** inconnu, les fonctions utilisables sont:
- stuff : pour recevoir des recommandations de stuff
- calcul : pour avoir des estimations de dommage d'invocations ou dopou
- stream : pour avoir des infos sur les prochains stream de warp

"""
            return resp
    return -1


def stuff_response(element=False,classe=False):
    elt=rearrange_elt(element)

    # vérification que les arguments soient corrects
    if not classe in CLASSES and not elt in ELEMENTS: #classe+element non reconnus
        resp=f"""
Réponse expliquand le fonctionnement des commandes classe et elt.    
Arguments : element ={elt}, classe={classe}
"""
        return resp
    elif not elt in ELEMENTS: #élément non reconnu
        resp=f"""
Je ne reconnais pas l'élément **{elt}** désolé, la liste des éléments dans ma bibliothèque est:
- terre
- feu
- eau
- air
- dopou
- multi
ou toute combinaison de ces éléments (excepté multi) séparés d'un '+', ex: element1+element2+... avec 3 éléments maximum
Arguments : element ={elt}, classe={classe}
"""
        return resp
    elif not classe in CLASSES: #classe non reconnue
        resp=f"""
Réponse expliquand le fonctionnement des commandes classe.        
Arguments : element ={elt}, classe={classe}
"""
        return resp
    
    if not classe or classe=='': # pas de classe spécifiée
        if not '+' in elt: #mono élément
            if elt in ["terre","feu","eau"]:
                resp= f"""
Pour l'élément {elt} je te recommande :
- 12/6 : {stuffs[elt]["12/6"][0]}
- 11/6 : {stuffs[elt]["11/6"][0]} 
N'hésite pas à tag Warp pour plus de détails sur ces stuffs."""
            elif elt=="air":
                resp= f"""
Pour l'élément {elt} je te recommande :
- 11/6 : {stuffs[elt]["11/6"][0]} (vraiment le mieux)
- 12/6 : {stuffs[elt]["12/6"][0]}
N'hésite pas à tag Warp pour plus de détails sur ces stuffs."""
            elif elt=="dopou":
                resp= f"""
Les dopou ne se jouent pas spécialement tous seuls, meme si ils sont prédominants il y a toujours un élément avec, mes recommandations sont donc les suivantes :
- eau air dopou : {stuffs["air+dopou+eau"]["11/6"][0]}
- eau dopou : {stuffs["dopou+eau"]["11/6"][0]}
- air dopou : {stuffs["air+dopou"]["11/6"][0]}
- terre eau dopou : {stuffs["dopou+eau+terre"]["11/6"][0]} (fonctionne pour terre dopou)
- feu eau dopou : {stuffs["dopou+eau+feu"]["11/6"][0]} (fonctionne pour feu dopou)
N'hésite pas à tag Warp pour plus de détails sur ces stuffs."""
            elif elt=='multi':
                resp= f"""
Pour jouer {elt} je te recommande :
- docri : {stuffs[elt]["cc"][0]}
N'hésite pas à tag Warp pour plus de détails sur ce stuff."""
            else : #élément non reconnu
                resp=f"""
Tu n'as pas fournis d'élément, la requête doit avoir le format : !WarpBot stuff *element* *classe*."""
        
        else: #mutli element
            if elt in stuffs.keys():
                resp= f"""
Pour l'élément {elt} je te recommande :\n"""
                for mode in stuffs[elt].keys():
                    if len(stuffs[elt][mode])>0:
                        resp+=f"- {mode} : {stuffs[elt][mode][0]}\n"
                resp+="N'hésite pas à tag Warp pour plus de détails sur ces stuffs."
            else: #élément non présent dans la biblio
                resp=f"""
Je n'ai pas de stuff dans ma bibliothèque qui corresponde au combo {elt}, tu peux tag Warp pour savoir pourquoi et peut-être qu'il aura quelque chose à te proposer."""
    else: #avec une classe précisée
        if classe in stuffs.keys():
            if elt in stuffs[classe].keys():
                resp=f"""
Pour l'élément {elt} de la classe {classe} je te recommande :\n"""
                for mode in stuffs[classe][elt].keys():
                    if len(stuffs[classe][elt][mode])>0:
                        resp+=f"- {mode} : {stuffs[classe][elt][mode][0]}\n"
                resp+="N'hésite pas à tag Warp pour plus de détails sur ces stuffs."
        else:
            resp=f"""
Je n'ai pas de stuff {elt} spécifiques pour la classe {classe}, tu trouveras probablement ton bonheur dans les stuffs classiques de l'élément:\n"""
            for mode in stuffs[elt].keys():
                if len(stuffs[elt][mode])>0:
                    resp+=f"- {mode} : {stuffs[elt][mode][0]}\n"
            resp+="N'hésite pas à tag Warp pour plus de détails sur ces stuffs."
    return resp


