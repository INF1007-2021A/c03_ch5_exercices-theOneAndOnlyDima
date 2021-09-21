#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        return number + (number * -2)
    else:
        return number


def use_prefixes() -> List[str]:
    noms = []
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    for i in range(len(prefixes)):
        noms.append(prefixes[i] + suffixe)
    return noms


def prime_integer_summation() -> int:
    nb_premiers = []
    nombre = 2
    somme = 0
    while len(nb_premiers) < 100:
        for i in range(2, nombre):
            if nombre % i == 0:
                nombre += 1
                break
        else:
            nb_premiers.append(nombre)
            nombre += 1
    for j in range(len(nb_premiers)):
        somme += nb_premiers[j]
    return somme


def factorial(number: int) -> int:
    if number == 0:
        return 1
    fact = 1
    for i in range(2, number + 1):
        fact *= i
    return fact


def use_continue() -> None:
    for i in range(1, 10 + 1):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    groupe_bool = []
    for i in groups:
        if len(i) > 10 or len(i) < 4:
            groupe_bool.append(False)
            continue
        elif 25 in i:
            groupe_bool.append(True)
            continue
        elif min(i) < 18:
            groupe_bool.append(False)
            continue
        elif max(i) > 70 and 50 in i:
            groupe_bool.append(False)
            continue
        groupe_bool.append(True)
    return groupe_bool


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
