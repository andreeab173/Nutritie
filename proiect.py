def recomandari_nutritionale(tip_corp):
    if tip_corp == "ectomorf":
        print("Recomandari nutritionale:")
        print("Dieta bogata in calorii (alimentatie frecventa)")
        print("Accent pe carbohidrati complecsi si proteine.")
        print("Consum de grasimi sanatoase(nuci, avocado)")
    elif tip_corp == "mezomorf":
        print("Recomandari nutritionale:")
        print("Dieta echilibrata in calorii")
        print("Accent pe proteine > carbohidrati si grasimi sanatoase")
        print("Accent pe proteine la fiecare masa")
    elif tip_corp == "endomorf":
        print("Recomandari nutritionale:")
        print("Dieta controlata in calorii (doar calorii de calitate)")
        print("Accent pe proteine si grasimi sanatoase")
        print("Limitarea carbohidratilor simpli")
    else:
        print("Tipul de corp introdus nu este valid.")

def calcul_rata_metabolica(varsta, kg, inaltime, sex):
    if sex == "femeie":
        return 10 * kg + 6.25 * inaltime - 5 * varsta - 161
    elif sex == "barbat":
        return 10 * kg + 6.25 * inaltime - 5 * varsta + 5
    else:
        print("Sexul introdus nu este valid.")
        return None

def calcul_calorii(rmb, activitate):
    if activitate == "sedentar":
        return rmb * 1.2
    elif activitate == "usor":
        return rmb * 1.375
    elif activitate == "moderat":
        return rmb * 1.55
    elif activitate == "greu":
        return rmb * 1.725
    elif activitate == "foarte greu":
        return rmb * 1.9
    else:
        print("Nivel de activitate invalid.")
        return None

def calcul_macronutrienti(calorii_totale, kg, activitate):
    if activitate == "sedentar":
        proteine_per_kg = 0.8
    elif activitate == "usor":
        proteine_per_kg = 1.2
    elif activitate in ["moderat", "greu", "foarte greu"]:
        proteine_per_kg = 2

    proteine = proteine_per_kg * kg
    grasimi = 1 * kg  # 1g/kg
    calorii_proteine = proteine * 4  # calorii din proteine (4 kcal per gram)
    calorii_grasimi = grasimi * 9  # calorii din grasimi (9 kcal per gram)

    calorii_ramase = calorii_totale - calorii_proteine - calorii_grasimi
    carbohidrati = calorii_ramase / 4  # grame carbohidrati (4 kcal per gram)
    calorii_carbohidrati = carbohidrati * 4  # calorii din carbohidrati

    return proteine, grasimi, carbohidrati, calorii_proteine, calorii_grasimi, calorii_carbohidrati

def main():
    tip_corp = input("Introduceti tipul dumneavoastra de corp (ectomorf, mezomorf, endomorf): ")
    recomandari_nutritionale(tip_corp)

    varsta = int(input("Introduceti varsta: "))
    kg = int(input("Introduceti kilogramele: "))
    inaltime = int(input("Introduceti inaltimea: "))
    sex = input("Introduceti sexul (femeie sau barbat): ").lower()

    rmb = calcul_rata_metabolica(varsta, kg, inaltime, sex)
    if rmb is None:
        return

    activitate = input("Introduceti nivelul de activitate (sedentar, usor, moderat, greu, foarte greu): ").lower()
    calorii_totale = calcul_calorii(rmb, activitate)
    if calorii_totale is None:
        return

    proteine, grasimi, carbohidrati, calorii_proteine, calorii_grasimi, calorii_carbohidrati = calcul_macronutrienti(calorii_totale, kg, activitate)

    print(f"Proteine: {proteine} g ({calorii_proteine} kcal)")
    print(f"Grasimi: {grasimi} g ({calorii_grasimi} kcal)")
    print(f"Carbohidrati: {carbohidrati} g ({calorii_carbohidrati} kcal)")

    obiectiv = input("Introduceti obiectivul (slabire, mentinere, crestere): ").lower()
    if obiectiv == "slabire":
        print("Obiectiv: Slabire")
        ajustare = calorii_totale * 0.1  # 10% scădere
        calorii_totale -= ajustare
        print(f"Necesar caloric pentru slabire: {calorii_totale} kcal.")
    elif obiectiv == "mentinere":
        print("Obiectiv: Mentinere")
        print(f"Necesar caloric pentru mentinere: {calorii_totale} kcal.")
    elif obiectiv == "crestere":
        print("Obiectiv: Crestere masa musculara")
        ajustare = calorii_totale * 0.1  # 10% creștere
        calorii_totale += ajustare
        print(f"Necesar caloric pentru crestere: {calorii_totale} kcal.")
    else:
        print("Obiectivul introdus nu este valid.")

if __name__ == "__main__":
    main()
