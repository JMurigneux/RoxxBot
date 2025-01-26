
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

* WarpBot twitch
donne les infos sur les prochains stream que je vais faire
'''


'''
idée présentation stuffs : dict avec tous les elements/modes + toutes les classes
chaque element du dict c'est un dict
quand une classe ne contient pas l'element on dit "j'ai pas de scpécifique mais voici les bases de cet element"
bi elem écris de la maniere suivante "terre+feu" mais rangés par ordre alphabétique, histoire de pouvoir créer facilement la string 
'''

#####################
# VARIABLES
#####################

ELEMENTS=['terre', 'feu', 'eau', 'air', 'dopou', 'feu+terre', 'eau+terre', 
          'air+terre', 'dopou+terre', 'eau+feu', 'air+feu', 'dopou+feu', 
          'air+eau', 'dopou+eau', 'air+dopou', 'air+eau+terre', 'air+eau+feu', 
          'air+feu+terre', 'eau+feu+terre', 'air+dopou+eau', 'air+dopou+terre', 
          'dopou+feu+terre', 'air+dopou+feu', 'dopou+eau+feu', 'dopou+eau+terre', 
          'multi']
CLASSES=['xelor', 'enutrof', 'eniripsa', 'osamodas', 'zobal', 'sadida',
       'steamer', 'sacrieur', 'iop', 'pandawa', 'ecaflip', 'cra', 'feca',
       'sram', 'roublard','vide']
#dans elements et classes je rajoute vide et faux pour prendre en compte les cas où on ne remplis pas l'argument de l'un des deux, ça peut être normal

STUFFS=dict()
STUFFS["terre"]={'kolo lunaire roxx': ["<https://d-bk.net/fr/t/8vYb>"],'kolo lunaire res': ["<https://d-bk.net/fr/t/ArAs>"],'kolo lunaire goule': ["<https://d-bk.net/fr/t/ANaF>"],'kolo chasseur ré fixes': ["<https://d-bk.net/fr/t/B0wS>"], 'scaramouchapeau': ["<https://d-bk.net/fr/t/9WxC>"],'plistik wulan': ["<https://d-bk.net/fr/t/BpSq>"], 'cc': [], 'no_cc': []}
STUFFS["feu"]={'bandit lumi': ["<https://d-bk.net/fr/t/A8Zv>"], 'funespadon': ["<https://d-bk.net/fr/t/8yAu>"], 'bandit firefoux': ["<https://d-bk.net/fr/t/7yVX>"], 'no_cc': []}
STUFFS["eau"]={'sanctuaire cryo': ["<https://d-bk.net/fr/t/B7er>"], 'sanctuaire wulan': ["<https://d-bk.net/fr/t/B9MR>"], 'cc': [], 'no_cc': []}
STUFFS["air"]={'no pano, dina usicke': ["<https://d-bk.net/fr/t/9pdy>"], 'no pano, klime sacrif': ["<https://d-bk.net/fr/t/9RJp>"],'ava padgref': ["<https://d-bk.net/fr/t/5qJF>"],'ava allister': ["<https://d-bk.net/fr/t/2EdT>"], 'cc': [], 'no_cc': []}
# STUFFS["dopou"]={'12/6': [], '11/6': [], 'cc': [], 'no_cc': []} ### Dopou is always with another element
STUFFS["feu+terre"]={'12/6': [], '11/6': [], 'cc': ["<https://d-bk.net/fr/t/7ESW>"], 'no_cc': ["<https://d-bk.net/fr/t/AwSG>"]}
STUFFS["eau+terre"]={'12/6': [],'11/6': [], 'noctu wulan': ["<https://d-bk.net/fr/t/Azb9>"], 'cc': [], 'no_cc': []}
STUFFS["air+terre"]={'nevark virale': ["<https://d-bk.net/fr/t/Bvq3>"], '11/6': [], 'cc': [], 'no_cc': []}
# STUFFS["dopou+terre"]={'12/6': [], '11/6': [], 'cc': [], 'no_cc': []}
STUFFS["eau+feu"]={'12/6': [], '11/6': [], 'Mazin pnose': ["<https://d-bk.net/fr/t/931X>"], 'cc': [], 'no_cc': []}
STUFFS["air+feu"]={'12/6': [], '11/6': [],'cc': [], 'Padgref strigide': ["<https://d-bk.net/fr/t/7OhS>"], 'no_cc': []}
# STUFFS["dopou+feu"]={'12/6': [], '11/6': [], 'cc': [], 'no_cc': []}
STUFFS["air+eau"]={'12/6': ["<https://d-bk.net/fr/t/8Ql4>"], '11/6': ["<https://d-bk.net/fr/t/BMXD>"], 'cc': ["<https://d-bk.net/fr/t/Br83>"], 'no_cc': []}
STUFFS["dopou+eau"]={'12/6': [], '11/6': ["<https://d-bk.net/fr/t/AzPu>"], 'cc': [], 'no_cc': []}
STUFFS["air+dopou"]={'12/6': [], '11/6': ["<https://d-bk.net/fr/t/BK5m>"], 'cc': [], 'no_cc': []}
STUFFS["air+eau+terre"]={'12/6': [], '11/6': ["<https://d-bk.net/fr/t/2OhT>"], 'cc': [], 'no_cc': []}
STUFFS["air+eau+feu"]={'12/6': [], '11/6': [], 'cc': ["<https://d-bk.net/fr/t/2OhM>"], 'no_cc': ["<https://d-bk.net/fr/t/BQYM>"]}
STUFFS["air+feu+terre"]={'12/6': [], '11/6': [], 'cc': ["<https://d-bk.net/fr/t/4qgX>"], 'no_cc': ["<https://d-bk.net/fr/t/AP7x>"]}
STUFFS["eau+feu+terre"]={'12/6': [], '11/6': [], 'cc': ["<https://d-bk.net/fr/t/47TD>"], 'no_cc': []}
STUFFS["air+dopou+eau"]={'12/6': ["<https://d-bk.net/fr/t/5kTX>"], '11/6': ["<https://d-bk.net/fr/t/A9Iy>"], 'cc': [], 'no_cc': []}
# STUFFS["air+dopou+terre"]={'12/6': [], '11/6': [], 'cc': [], 'no_cc': []}
# STUFFS["dopou+feu+terre"]={'12/6': [], '11/6': [], 'cc': [], 'no_cc': []}
# STUFFS["air+dopou+feu"]={'12/6': [], '11/6': [], 'cc': [], 'no_cc': []}
STUFFS["dopou+eau+feu"]={'12/6': [], '11/6': ["<https://d-bk.net/fr/t/BQQd>"], 'cc': [], 'no_cc': []}
STUFFS["dopou+eau+terre"]={'12/6': [], '11/6': ["<https://d-bk.net/fr/t/BQQl>"], 'cc': [], 'no_cc': []}
STUFFS["multi"]={'12/6': [], '11/6': [], 'strigide glours': ["<https://d-bk.net/fr/t/2Ol7>"], 'virale glours wukin': ["<https://d-bk.net/fr/t/Bv6e>"]}
STUFFS["osamodas"]={'feu' :{'12/6' :["<https://d-bk.net/fr/t/9nwN>"]}
                    ,'eau+feu':{'cher' : ["<https://d-bk.net/fr/t/9UXA>"],'plus abordable' : ["<https://d-bk.net/fr/t/AQSn>"]}
                    ,'air' :{'11/6' :["<https://d-bk.net/fr/t/9Y06>"]}
                    ,'eau' :{'12/6' :["<https://d-bk.net/fr/t/BCMB>"]}                    
                    }
STUFFS["sadida"]={'feu' :{'12/6' :["<https://d-bk.net/fr/t/9nwN>"]}
                    ,'eau+feu':{'cher' : ["<https://d-bk.net/fr/t/9UXA>"],'plus abordable' : ["<https://d-bk.net/fr/t/AQSn>"]}
                    ,'terre' :{'11/6' :["<https://d-bk.net/fr/t/BQpf>"]}
                    ,'eau+terre' :{'11/6' :["<https://d-bk.net/fr/t/BoWN>"]}                
                    }
STUFFS["iop"]={'dopou' :{'12/6' :["<https://d-bk.net/fr/t/5kTX>"]}              
                    }


#####################
# MAIN RESPONSE
#####################

# def get_response(user_input: str, user_name : str, channel : str):
#     lowered: str = user_input.lower()

#     if lowered == '':
#         return 'Ok tu arrive à envoyer des messages vides?? Sorcier!'
#     elif lowered =='salut warpbot' :
#         return f'Salut {user_name}!'    
#     elif lowered =='!warpbot lance un dé' or lowered =='!wb lance un dé':
#         return f'Tu as eu: {randint(1, 6)}'
#     elif command :=re.match(r"(?P<botname>!\w+)\s?(?P<function>\w*)\s?(?P<arg1>[+\w]*)\s?(?P<arg2>[a-z0-9\/\.\-:]*)", lowered):
#         print(command.group('botname'),command.group('function'),command.group('arg1'),command.group('arg2'))
#         if command.group('botname')!= '!warpbot' and command.group('botname')!= '!wb':
#             return -1
        
#         if command.group('function')=="stuff": #stuff
#             element = command.group('arg1')
#             classe = command.group('arg2')
#             # print(element,classe)
#             return stuff_response(element=element,classe=classe)
        
#         # elif command.group('function')=="calcul": #calcul
#         #     return calcul_response(command)
        
#         elif command.group('function')=="twitch": #twitch
#             resp= f"""
# Je stream la majorité des tournois pvp sur dofus touch, sauf quand je participe bien sur !
# Au programme :
# - 27/28/29 septembre : stream tournois du serveur Oshimo
# - 4/5/6 octobre : je participe au tournois sur herdegrize
# """
#             return resp
        
#         elif command.group('function')=="help": #help
#             return help_response(command)
        
#         else: #mauvaise fonction
#             resp= f"""
# Argument `{command.group('function')} ` inconnu, les fonctions utilisables sont:
# - help   : pour recevoir de l'aide sur l'utilisation du bot 
# - stuff  : pour recevoir des recommandations de stuff
# - twitch : pour avoir des infos sur les prochains stream de warp
# Tu peux utiliser `!WarpBot help xxx` pour avoir des informations sur comment formuler les requetes avec chacune des 2 fonctions stuff/twitch.
# """
# # - calcul : pour avoir des estimations de dommage d'invocations ou dopou
#             return resp
#     return -1



#####################
# FONCTIONS UTILES
#####################

#prend une liste d'éléments et la met sous la forme elt1+elt2+elt3...
def from_elts_to_multi(elt_list):
    sorted_list=sorted(elt_list)
    return '+'.join(sorted_list)

#prends les éléments sous le format elt1+elt2+elt3... et les remet dans le bon ordre
def lecture_elt(elts):
    elt_spl=[e.strip() for e in elts.replace("/","+").split(r"+")]
    # print(elts,elt_spl)
    if len(elt_spl)==1:
        elt_spl=[e.strip() for e in elts.split(r" ")]
        # print(elts,elt_spl)

    return from_elts_to_multi(elt_spl)

def help_response(command,plateforme="discord"):

    if plateforme=="discord":
        prefixe='/'
    elif plateforme=="twitch":
        prefixe="!"
    else :
        prefixe='/'

    if command=="stuff": #/wbhelp stuff
        resp= f"""
Pour recevoir des recommandations de stuff il faut utiliser la commande `{prefixe}stuff élément classe`
- **élément** : terre/feu/eau/air/dopou/multi ou toute combinaison d'éléments différents (excepté multi) séparés d'un '+', ex: élément+élément+... avec 3 éléments maximum
Exemple de requete valide : `{prefixe}stuff air+eau`
- OPTIONNEL **classe** : une des classes du jeu écrite avec le nom complet, pour recevoir des stuff spécifiques à la classe donnée s'il y en a dans la bibliothèque.
Ce qui nous fait une requete de la forme : `{prefixe}stuff eau+feu osamodas`
"""
#     elif command.group('arg1')=="calcul": #/wbhelp calcul
#         resp= f"""
# TODO : pas de fonction donc pas d'explication pour le moment
# """
    elif command=="twitch": #/wbhelp twitch
        resp= f"""
`{prefixe}twitch` Répond avec les infos sur les prochains stream de prévus (si il n'y a pas de tournois de prévus probablement qu'il n'y aura pas de stream).
"""
    else: #/wbhelp
        resp= f"""
Comment utiliser WarpBot? 

Il y a deux commandes :
- Stuff  : pour recevoir des recommandations de stuff. `{prefixe}wbhelp stuff` pour plus de détails.
- Twitch : pour avoir des infos sur les prochains stream de warp. Pas d'argument à rajouter, `{prefixe}twitch` vous renverra les informations nécessaires.
"""
# - Calcul : pour avoir des estimations de dommage d'invocations ou dopou . `/wbhelp calcul` pour plus de détails.
# - calcul : pour la formulation des calculs de dommage d'invocations ou dopou
    return resp
        
def stuff_response(element,classe,plateforme="discord"):

    elt=lecture_elt(element)

    if plateforme=="discord":
        prefixe='/'
    elif plateforme=="twitch":
        prefixe="!"
    else :
        prefixe='/'
        

    # vérification que les arguments soient corrects
    if not classe in CLASSES and not elt in ELEMENTS: #classe+element non reconnus
        resp=f"""
Je ne reconnais pas les arguments **{elt}** et **{classe}** fournis.
Pour recevoir de l'aide sur l'utilisation de la fonction stuff, taper `{prefixe}wbhelp stuff`.
Elements valides: terre/feu/eau/air/dopou/multi ou toute combinaison d'éléments différents (excepté multi) séparés d'un '+'.
Pour les classes il faut écrire le nom en entier.
Exemple de requete valide : `{prefixe}stuff eau+feu osamodas`.
"""
        return resp
    elif not elt in ELEMENTS: #élément non reconnu
        resp=f"""
Je ne reconnais pas l'élément **{elt}** désolé, pour recevoir de l'aide sur l'utilisation de la fonction stuff, taper `{prefixe}wbhelp stuff`.
Elements valides: terre/feu/eau/air/dopou/multi ou toute combinaison d'éléments différents (excepté multi) séparés d'un '+'.
Exemple de requete valide : `{prefixe}stuff air+eau`.
"""
        return resp
    elif not classe in CLASSES: #classe non reconnue
        resp=f"""
Je ne reconnais pas la classe **{classe}** désolé, pour recevoir de l'aide sur l'utilisation de la fonction stuff, taper `{prefixe}wbhelp stuff`.
Il faut écrire le nom de classe en entier.
Exemple de requete valide : `{prefixe}stuff eau+feu osamodas`.
"""
        return resp
    
    if classe=='vide': # pas de classe spécifiée
        if elt=="dopou":
            resp= f"""
Les dopou ne se jouent pas spécialement tous seuls, meme si ils sont prédominants il y a toujours un élément avec, mes recommandations sont donc les suivantes : 
- eau air dopou : 11/6 {STUFFS["air+dopou+eau"]["11/6"][0]} ou 12/6 {STUFFS["air+dopou+eau"]["12/6"][0]}
- eau dopou : {STUFFS["dopou+eau"]["11/6"][0]}
- air dopou : {STUFFS["air+dopou"]["11/6"][0]}
- terre eau dopou : {STUFFS["dopou+eau+terre"]["11/6"][0]} (fonctionne pour terre dopou)
- feu eau dopou : {STUFFS["dopou+eau+feu"]["11/6"][0]} (fonctionne pour feu dopou)
N'hésite pas à tag Warp pour plus de détails sur ces stuffs."""
            return resp        
        else:
            if elt in STUFFS.keys():
                resp= f"""
Pour un stuff {elt} je recommande :\n"""
                for mode in STUFFS[elt].keys():
                    if len(STUFFS[elt][mode])>0:
                        resp+=f"- {mode} : {STUFFS[elt][mode][0]}\n"
                resp+="N'hésite pas à tag Warp pour plus de détails sur ces stuffs."
                return resp

            else: #élément non présent dans la biblio
                resp=f"""
Je n'ai pas de stuff dans ma bibliothèque qui corresponde au combo {elt}, tu peux tag Warp pour savoir pourquoi et peut-être qu'il aura quelque chose à te proposer."""
                return resp
                
    else: #avec une classe précisée
        resp='pas trouvé'
        if classe in STUFFS.keys():
            if elt in STUFFS[classe].keys():
                resp=f"""
Pour l'élément {elt} de la classe {classe} je te recommande :\n"""
                for mode in STUFFS[classe][elt].keys():
                    if len(STUFFS[classe][elt][mode])>0:
                        resp+=f"- {mode} : {STUFFS[classe][elt][mode][0]}\n"
                resp+="N'hésite pas à tag Warp pour plus de détails sur ces stuffs."
                
        if resp=='pas trouvé':
            resp=f"""
Je n'ai pas de stuff {elt} spécifiques pour la classe {classe}, tu trouveras probablement ton bonheur dans les stuffs classiques de l'élément:\n"""
            for mode in STUFFS[elt].keys():
                if len(STUFFS[elt][mode])>0:
                    resp+=f"- {mode} : {STUFFS[elt][mode][0]}\n"
            resp+="N'hésite pas à tag Warp pour plus de détails sur ces stuffs."
        return resp

    resp="Vraisemblablement il y a une erreur dans le code : tu ne devrais pas arriver ici, tag Warp pour qu'il répare le bug stp <3"
    return resp

def calcul_response(command,plateforme="discord"):

    if plateforme=="discord":
        prefixe='/'
    elif plateforme=="twitch":
        prefixe="!"
    else :
        prefixe='/'
    if command.group('arg1')=="dopou": #/calcul dopou

        resp= f"""
Pour recevoir des recommandations de stuff il faut utiliser la fonction `{prefixe}stuff élément classe`
- **élément** : terre/feu/eau/air/dopou/multi ou toute combinaison de ces éléments (excepté multi) séparés d'un '+', ex: élément+élément+... avec 3 éléments maximum
Exemple de requete valide : `/stuff air+eau`
- **classe** : une des classes du jeu écrite avec le nom complet, pour recevoir des stuff spécifiques à la classe donnée s'il y en a dans la bibliothèque.
Ce qui nous fait une requete de la forme : `{prefixe}stuff eau+feu osamodas`
"""
    
    elif command.group('arg1')=='': #/calcul 
        resp= f"""

"""
    else: #/calcul dqzdzqd , arg1 erroné
        resp= f"""

"""
    return resp