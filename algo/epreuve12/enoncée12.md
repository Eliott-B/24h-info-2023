 
 
 
On vous propose de jouer à un petit jeu de nombres. Ce jeu se joue à tour de rôle, et à chaque étape le joueur fabrique une séquence de chiffres en lisant à haute voix la séquence précédente (plus précisément en lisant le nombre de fois qu'apparaît chaque chiffre). Par exemple, 211 se lit "un 2, deux 1", ce qui donne la séquence 1221.

Les séquences sont donc générées itérativement en utilisant la séquence précédente pour la prochaine étape. Pour chaque étape, prenez la séquence précédente et remplacez chaque série de chiffres (exemple 111) par le nombre de chiffres (3) suivi du chiffre lui-même (1).

________________________________________

Par exemples,

    1 devient 11 (1 copie du chiffre 1),
    11 devient 21 (2 copies du chiffre 1),
    21 devient 1211 (un 2 suivi d'un 1),
    1211 devient 111221 (un 1, un 2, deux 1),
    111221 devient 312211 (trois 1, deux 2, un 1),

En partant de la séquence 1, après avoir appliqué 5 fois ce processus, on obtient la séquence 312211, qui contient 6 valeurs.

#####################Problème####################
Si la séquence initiale est 1113122113, quelle est la longueur L du résultat après avoir appliqué 50 fois le processus ? Le code pour ce niveau est alors donné par:



code = (n + 1) × L
où n est votre numéro d'équipe.





Indice: Pour information, la longueur du résultat après 40 itérations est: 360154.
