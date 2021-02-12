# --- --- --- Méthode split

# --- --- Question 1

# s.split(" ") == ['la', 'méthode', 'split', 'est', 'parfois', 'bien', 'utile']
# s.split("e") == ['la méthod', ' split ', 'st parfois bi', 'n util', '']
# s.split("é") == ['la m', 'thode split est parfois bien utile']
# s.split() == ['la', 'méthode', 'split', 'est', 'parfois', 'bien', 'utile']
# s.split('') Erreur, le séparateur vide est un séparateur invalide.
# s.split('split') == ['la méthode ', ' est parfois bien utile']

# --- --- Question 2

# La méthode split() est appliquée sur une chaîne de caractère avec un séparateur
# de type string. Elle renvoie une liste de chaînes de caractères en séparant la 
# chaîne originale en plusieurs sous-chaînes qui ne contiennent pas le séparateur.

# --- --- Question 3

# Non, elle ne modifie pas la chaîne sur laquelle la méthode est appliquée.

# --- --- --- Méthode join

# --- --- Question 1

# "".join(l) == 'laméthodesplitestparfoisbienutile'
# " ".join(l) == 'la méthode split est parfois bien utile'
# ";".join(l) == 'la;méthode;split;est;parfois;bien;utile'
# " tralala ".join(l) == 'la tralala méthode tralala split tralala est tralala parfois tralala bien tralala utile'
# print ("\n".join(l)) -> Affiche un retour à la ligne après chaque mot
# "".join(s) == 'la méthode split est parfois bien utile'
# "!".join(s) == 'l!a! !m!é!t!h!o!d!e! !s!p!l!i!t! !e!s!t! !p!a!r!f!o!i!s! !b!i!e!n! !u!t!i!l!e'
# "".join() -> Erreur, un paramètre est nécessaire.
# "".join([]) == ''
# "".join([1,2]) -> Erreur, on attend un paramètre de type chaîne.

# --- --- Question 2

# La méthode join renvoie la concaténation des chaînes dans le tableau 
# passé en paramètre en insérant le séparateur sur lequel la méthode est
# appliquée entre chaque chaîne.

# --- --- Question 3

# Non, elle ne modifie pas la chaîne à laquelle elle s'applique.

# --- --- --- La méthode sort

# --- --- Question 1

# La liste list("timoleon") est devenue ['e', 'i', 'l', 'm', 'n', 'o', 'o', 't'].
# La liste list("Je n'ai jamais joué de flûte.") est devenue : 
# [' ', ' ', ' ', ' ', ' ', "'", '.', 'J', 'a', 'a', 'a', 'd', 'e', 'e', 'e', 'f', 'i', 'i', 'j', 'j', 'l', 'm', 'n', 'o', 's', 't', 'u', 'é', 'û']

# Les caractères semblent être rangés en fonction de leur code Unicode. Pour la
# plupart des caractères, c'est également leur code ASCII.

# --- --- Question 2

# On demande à Python de trier une liste non typée, donc il doit effectuer des 
# comparaisons entre des chaînes de caractères et des entiers. 
# On n'a pas spécifié dans le code de la méthode sort comment comparer une chaîne
# de caractères et un entier, donc on aboutit à une erreur à l'exécution.

# --- --- --- Une fonction sort pour les chaînes

