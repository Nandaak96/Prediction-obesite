## IMPORTER LES BIBLIOTHEQUES NECESSAIRES

import streamlit as st  ## Permet de créer l'interface de l'application
import joblib           ## Permet d'importer le modèle que nous avons entrainé
import numpy as np      ## Permet de manipuler les données numériques
import pandas as pd     ## Permet d'importer notre BDD
import time             ## Permet de manipuler le temps
import altair as alt    ## Pour créer des graphiques interactifs

##  CONFIGURATION DE NOTRE INTERFACE UTILISATEUR
 
st.set_page_config(page_title="🩺Prédiction du niveau d'obésité", page_icon="🩺", layout="wide")
    #page_title : le titre de l’onglet dans le navigateur.
    #page_icon : l’icône de l’onglet.
    #layout="wide" : élargit la mise en page pour utiliser toute la largeur de l’écran.


##  AJOUT D'UNE IMAGE COMME BANNIERE
from PIL import Image
image = Image.open("/Users/nanda/Documents/DATA ANALYTICS-PARIS 1/ProjetPython_Sante/Image2.jpg")

st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image(image, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)


## TITRE DE L'APPLICATION
st.title("🩺 Prédiction du Niveau d'Obésité")
st.subheader("Veuillez renseigner les informations suivantes pour estimer votre niveau de risque.")



  ## PERMET DE CHARGER NOTRE MODELE
model = joblib.load("modele_projetpython_Vf.joblib")


## SIDEBAR CONFIGURATION
st.sidebar.title("📊 À propos de l'application")

st.sidebar.info(
"""
Cette application prédit votre **risque d'obésité** en fonction de vos habitudes
alimentaires, d'activité physique et de style de vie.
"""
)
st.sidebar.markdown("---")       ## Séparateur

st.sidebar.header("📘 Informations utiles")

st.sidebar.markdown(
"""
- **Modèle utilisé :** XGB Classifier 
- **Données :** Dataset public sur les habitudes de vie 
- **Précision actuelle :** ~ 72% 
"""
)
st.sidebar.markdown("---")

st.sidebar.header("👤 À propos des créateurs")

st.sidebar.markdown(
"""
Développé par:
- Akouyo AKPAKLI  
- Abdoulaye NDIAYE
- Léa GRAVELLARD           
- 🔗 [GitHub](https://github.com/tonprofil) 

"""
)
st.sidebar.markdown("---")

st.sidebar.caption("⚠️ Ceci est un outil pédagogique. Ne remplace pas un avis médical.")


## Pour faire la correspondance entre les input utilisateurs et notre BDD on crée un dictionnaire de correspondance
## On associe donc chaque input utilisateur au code correspondant dans notre BDD
genre_dic = {"Homme": 1, "Femme": 0}
historique_dic = {"Oui": 1, "Non": 0}
favc_dic={"Oui": 1, "Non": 0}
fcvc_dic={"Toujours":3, "Quelques fois":2, "Jamais": 1}
ncp_dic={"Entre 1 et 2 repas":1, "3 repas":2, "Plus de 3 repas":3}
caec_dic={"Non":1, "Quelques fois":2, "Fréquemment":3, "Toujours": 4}
calc_dic={"Toujours":4, "Souvent":3, "Quelques fois":2, "Jamais":1}
ch2o_dic={"Moins d'1 L":1, "Entre 1 et 2 L":2, "Plus de 2 L":3}
scc_dic={"Oui": 1, "Non": 0}
smoke_dic={"Oui": 1, "Non": 0}
faf_dic={"Jamais":1, "1 à 2 fois par semaine":2, "2 à 3 fois par semaine":3,"Plus de 3 fois par semaine": 4}
tue_dic={"Moins d'1hr":1, "Entre 1 et 3hrs":2, "Plus de 3hrs":3, "Pas d'utilisation":0}
mtrans_dic={"Voiture":0, "Moto":2, "Vélo":1, "Transports publics":3, "Marche":4}

## INTERFACE UTILISATEUR ORGANISEE EN 3 COLONNES
col1, col2, col3 = st.columns(3)
    #Divise la page en 3 colonnes pour organiser les champs de manière ergonomique.

## COLONNE 1 - Input utilisateur
with col1:
    st.markdown("Informations personnelles")
    genre = st.selectbox("Genre", ["Homme", "Femme"], key="genre_select")
    âge = st.number_input("Âge", min_value=16, max_value=100, value=25, key="age_select")

    # On recrée les variables taille et poids mais uniquement pour le calcul d’IMC
    taille = st.number_input("Taille (m)", min_value=1.0, max_value=2.5, value=1.7, key="taille_select")
    poids = st.number_input("Poids (kg)", min_value=30, max_value=200, value=70, key="poids_select")
    historique = st.selectbox("Antécédents familiaux de surpoids", ["Oui", "Non"])
    
    #selectbox : pour les listes déroulantes.
    #number_input : champ de saisie numérique avec limites.


with col2:
    st.markdown(" Habitudes alimentaires")
    favc = st.selectbox("Consomme souvent des aliments très caloriques", ["Oui", "Non"], key="favc_select")
    fcvc = st.selectbox("Fréquence de consommation de légumes", ["Toujours", "Quelques fois", "Jamais"], key="fcvc_select")
    ncp = st.selectbox("Nombre de repas principaux par jour", ["Entre 1 et 2 repas", "3 repas", "Plus de 3 repas"], key="ncp_select")
    caec = st.selectbox("Grignotage entre les repas", ["Non", "Quelques fois", "Fréquemment", "Toujours"], key="caec_select")
    calc = st.selectbox("Fréquence de consommation d'alcool", ["Toujours", "Souvent", "Quelques fois", "Jamais"], key="calc_select")
    

with col3:
    st.markdown("Mode de vie")
    ch2o = st.selectbox("Consommation quotidienne d'eau", ["Moins d'1 L", "Entre 1 et 2 L", "Plus de 2 L"], key="ch2o_select")
    scc = st.selectbox("Suivi de la consommation de calorie", ["Oui", "Non"], key="scc_select")
    smke = st.selectbox("Fumez-vous ?", ["Non", "Oui"], key="smoke_select")
    faf = st.selectbox("Féquence d'activité physique", ["Jamais", "1 à 2 fois par semaine", "2 à 3 fois par semaine","Plus de 3 fois par semaine" ], key="faf_select")
    tue = st.selectbox("Temps d'écran par jour", ["Moins d'1hr", "Entre 1 et 3hrs", "Plus de 3hrs", "Pas d'utilisation"], key="tue_select")
    mtrans = st.selectbox("Mode de déplacement le plus utilisé", ["Voiture", "Moto", "Vélo", "Transports publics", "Marche"], key="mtrans_select")
    
    
## On a ici fait correspondre les dictionnaires crées aux variables de notre BDD
FAMILY_HISTO=historique_dic[historique]
GENDER = genre_dic[genre]
FC_CAL = favc_dic[favc]
FC_VEG = fcvc_dic[fcvc]
NB_MAIN_MEAL = ncp_dic[ncp]
SNACKING=caec_dic[caec]
C_ALCOHOL=calc_dic[calc]
CH2O=ch2o_dic[ch2o]
CAL_BEVERAGE=scc_dic[scc]
SMOKE=smoke_dic[smke]
F_SPORT=faf_dic[faf]
TIME_TECH_USAGE=tue_dic[tue]
MODE_TRANSP=mtrans_dic[mtrans]

## On va mettre en français les valeurs texte de notre variable prédictive pour avoir les outputs en FR
obesity_translation = {
    "Insufficient_Weight": "Insuffisance pondérale",
    "Normal_Weight": "Poids normal",
    "Overweight_Level_I": "Surpoids niveau I",
    "Overweight_Level_II": "Surpoids niveau II",
    "Obesity_Type_I": "Obésité type I",
    "Obesity_Type_II": "Obésité type II",
    "Obesity_Type_III": "Obésité type III"
}

## Nous avons récupérer notre BDD 
dt = pd.read_csv('BDDobesity_level_V2.csv')

## On va transformer certaines variables qui sont float en INT parce que ce sont des variables catégorielles
cols_to_convert = ["Age", "FCVC","FAVC", "NCP", "FAF", "TUE", "CH2O"]
dt[cols_to_convert] = dt[cols_to_convert].astype(int)
dt["FAVC"] = dt["FAVC"].replace({0: "Non", 1: "Oui"})

## Création d'une version dupliquée de notre BDD pour la suite
dt_all=dt

## Puisque nous nous n'avons pas la variable IMC dans notre BDD df_all, nous allons le calculer à partir des colonnes Taille et Poids :
if "IMC" not in dt_all.columns:
    dt_all["IMC"] = dt_all["Weight"] / (dt_all["Height"] ** 2)

## Nous allons rappeler notre variable cible encodée
cible_en= joblib.load("cible_en.joblib")

## Lancer la prédiction 
if st.button("📊 Prédire le risque"):

    # Calcul IMC
    imc = poids / (taille ** 2)
    if imc < 18.5:
        statut = "Insuffisance pondérale"
    elif imc < 25:
        statut = "Poids normal"
    elif imc < 30:
        statut = "Surpoids"
    else:
        statut = "Obésité"

    ## IMC et STATUT affiché à l'utilisateur
    st.info(f"💡 Votre IMC est de **{imc:.2f}** → **{statut}**") 
    
    ## Prédiction du risque comportemental
    input_data = pd.DataFrame([{
    'GENDER': genre_dic[genre],
    'AGE': âge,
    'FAMILY_HISTO': historique_dic[historique],
    'FC_CAL': favc_dic[favc],
    'FC_VEG': fcvc_dic[fcvc],
    'NB_MAIN_MEAL': ncp_dic[ncp],
    'SNACKING': caec_dic[caec],
    'SMOKE': smoke_dic[smke],
    'CH2O': ch2o_dic[ch2o],
    'CAL_BEVERAGE': scc_dic[scc],
    'F_SPORT': faf_dic[faf],
    'TIME_TECH_USAGE': tue_dic[tue],
    'C_ALCOHOL': calc_dic[calc],
    'MODE_TRANSP': mtrans_dic[mtrans]
    }])

     # barre de progression
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i+1)

    prediction = model.predict(input_data)
    output = cible_en.inverse_transform(prediction)[0]
    output_fr = obesity_translation.get(output, output)

    ## Explications affichées à l'utilisateur sur l'IMC
    st.write(
    "L'indice de masse corporelle (IMC) est calculé en divisant le poids (kg) par le carré de la taille (m). "
    "Il sert à classer votre statut pondéral. \n\n"
    "L'IMC permet d'évaluer rapidement la corpulence et d'identifier un risque de santé lié au poids. "
    "Cependant, il ne distingue pas la masse musculaire de la masse grasse ni la répartition de la graisse, "
    "et peut être moins précis chez certaines populations (athlètes, personnes âgées, enfants). "
    "Son principal avantage est sa simplicité de calcul, ce qui en fait un outil pratique pour le dépistage "
    "et le suivi à grande échelle."
    )


     ## 1) Histogramme de la distribution des IMC 
    hist = (
        alt.Chart(dt_all)
        .mark_bar(opacity=0.5)
        .encode(
            alt.X("IMC:Q", bin=alt.Bin(maxbins=30), title="IMC"),
            y=alt.Y("count()", title="Effectif")
        )
        .properties(width=500, height=300, title="Distribution des IMC")
    )
    # Ligne rouge à la valeur de l'IMC de l'utilisateur pour connaitre sa position
    rule = (
        alt.Chart(pd.DataFrame({"IMC": [imc]}))
        .mark_rule(color="red", size=3)
        .encode(x="IMC:Q")
    )
    st.subheader("📊 Où vous situez-vous sur la population (IMC)")
    st.write(
    "Parmi notre population d’environ 20 000 personnes interrogées, ce graphique montre la répartition des IMC. "
    "Votre ligne rouge indique où vous vous situez par rapport à cette population, "
    "pour vous donner un ordre d’idée de votre positionnement."
)
    # Afficher l'histogramme interactif 
    st.altair_chart(hist + rule, use_container_width=False)

    ## 2) Création des catégories standard d'IMC (Barres horizontales)
    # L'utilisateur pourra donc voir sa position au sein de sa catégorie
    cats = pd.DataFrame([
        {"category": "Insuffisance pondérale", "min": 0,    "max": 18.5},
        {"category": "Poids normal",            "min": 18.5, "max": 25},
        {"category": "Surpoids",                "min": 25,   "max": 30},
        {"category": "Obésité",                 "min": 30,   "max": dt_all["IMC"].max()}
    ])

    range_chart = (
        alt.Chart(cats)
           .mark_bar(orient="horizontal", size=20)
           .encode(
               y=alt.Y(
                   "category:N",
                   title="Catégorie d'IMC",
                   axis=alt.Axis(labelAngle=0, labelFontSize=12, labelLimit=200)
               ),
               x=alt.X("min:Q", title="IMC"),
               x2="max:Q",
               color=alt.Color("category:N", legend=None)
           )
           .properties(
               width=500,
               height=250,   # on monte à 150px pour voir toutes les lignes
               title="Plages d’IMC par catégorie"
           )
    )

    # Règle verticale pour marquer la poser de l'utilisateur dans sa catégorie selon son IMC
    marker = (
        alt.Chart(pd.DataFrame({"IMC": [imc]}))
           .mark_rule(color="red", size=3)
           .encode(x="IMC:Q")
    )

    st.subheader("📏 Votre IMC dans les catégories standard")
    st.write(
    "Les différentes catégories de l’IMC sont l’insuffisance pondérale, le poids normal, le surpoids et l’obésité :\n"
    "- **Insuffisance pondérale** (IMC < 18,5)\n"
    "- **Poids normal** (18,5 – 25)\n"
    "- **Surpoids** (25 – 30)\n"
    "- **Obésité** (IMC ≥ 30)"
)

    ## Afficher le bar chart interactif
    st.altair_chart(range_chart + marker, use_container_width=False)


    ## 3) Affichage du risque d'obésité
    st.success(f"✅ Risque d'obésité **comportemental** prédit : **{output_fr}**")

    
       # Importances de variables du modèle
    feature_cols = [
        "Gender", "Age", "family_history_with_overweight",
        "FAVC", "FCVC", "NCP", "CAEC",
        "SMOKE", "CH2O", "SCC", "FAF", "TUE", "CALC", "MTRANS"
    ]
    importances = model.feature_importances_

    # Mapping vers les libellés français
    label_map = {
        "Gender": "Genre",
        "Age": "Âge",
        "family_history_with_overweight": "Antécédents familiaux de surpoids",
        "FAVC": "Consommation fréquente d'aliments caloriques",
        "FCVC": "Consommation de légumes",
        "NCP": "Nombre de repas principaux/jour",
        "CAEC": "Grignotage entre les repas",
        "SMOKE": "Fumez-vous ?",
        "CH2O": "Consommation quotidienne d'eau (L)",
        "SCC": "Suivi de la consommation calorique",
        "FAF": "Fréquence d’activité physique",
        "TUE": "Temps écran/jour",
        "CALC": "Consommation d’alcool",
        "MTRANS": "Mode de déplacement le plus utilisé"
    }
      # Construire le DataFrame des importances avec labels FR
    dt_imp = (
        pd.DataFrame({
            "variable": feature_cols,
            "importance": importances
        })
        .assign(variable_fr=lambda d: d["variable"].map(label_map))
        .sort_values("importance", ascending=False)
    )

    # Bar chart Altair avec labels français
    imp_chart = (
        alt.Chart(dt_imp)
           .mark_bar()
           .encode(
               x=alt.X("importance:Q", title="Importance"),
               y=alt.Y(
                   "variable_fr:N",
                   sort="-x",
                   title="Variable",
                   axis=alt.Axis(labelFontSize=12, labelAngle=0, labelLimit=200)
               ),
               tooltip=[
                   alt.Tooltip("variable_fr:N", title="Variable"),
                   alt.Tooltip("importance:Q", format=".2f", title="Importance")
               ]
           )
           .properties(
               width=500,
               height=500,
               title="Importances de variables du modèle"
           )
    )

    st.subheader("📈 Facteurs clés de prédiction d'obésité")
    st.write(
        "L’obésité est un phénomène multifactoriel : au-delà du poids et de la taille, "
        "le risque dépend de nombreux comportements et caractéristiques "
        "(activité physique, habitudes alimentaires, grignotage, consommation d’eau, "
        "d’alcool, rythme des repas, etc.).\n\n"
        "Sur notre population d’étude (~20 000 personnes), ce graphique classe "
        "ces variables par ordre d’importance pour la prédiction du risque d’obésité."
    )
    st.altair_chart(imp_chart, use_container_width=False)
