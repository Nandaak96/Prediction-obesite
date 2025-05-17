# 🩺WebApp de Prédiction du Risque d'Obésité

## Membres du groupe
Abdoulaye NDIAYE
Akouyo AKPAKLI
Léa GRAVELLARD 

## 🎯 Objectif de l'application

Cette application web permet de prédire le **niveau d’obésité** d’un individu à partir de ses habitudes alimentaires, son niveau d’activité physique, ses antécédents familiaux et d'autres facteurs.  
Elle vise à sensibiliser les utilisateurs à leur mode de vie et leur fournir une estimation de leur risque d’obésité.

---

## 📊 Dataset utilisé

Le jeu de données provient d’une enquête sur les comportements alimentaires et le style de vie. Il contient :
- des variables quantitatives (âge, taille, poids…),
- des variables qualitatives (fréquence des repas, transport utilisé, activité physique…).
qui sont pertinentes

Ce dataset est aussi bien adapté à une tâche de **classification supervisée multiclasse**.

---

## 🤖 Modélisation dans un fichier ipynb

### 🔎 Modèle de référence :
- **Random Classifier** utilisé en première intention → résultats peu précis ce qui a motivé la recherche d’un modèle plus robuste. 

### ✅ Modèle retenu :
- **XGBoost Classifier**, pour sa :
  - haute performance,
  - robustesse face à des variables mixtes,
  - précision nettement meilleure sur notre jeu de données.

Le modèle a été entraîné, évalué, puis sauvegardé pour être utilisé dans l’application.

---

## 🖥️ Fonctionnement global de l'application

L'application est développée dans un fichier .py avec **Streamlit**, une bibliothèque Python pour créer facilement des interfaces web. Nous l'avons déployé uniquement en local.

### ⚙️ Étapes de fonctionnement :
1. L’utilisateur entre ses informations via des champs interactifs (âge, sexe, fréquence des repas, activité physique, etc.).
2. Les données sont prétraitées pour correspondre aux formats attendus par le modèle (encodage, correspondance à la BDD …).
3. L'utilisateur clique sur 'Prédire' ce qui lance le calcul de l'IMC sur base de sa taille et son poids. L'application lui affiche aussi:
    - les explications sur ce qu'est l'IMC
    - La position de son IMC en rouge au sein de la distribution des IMC de notre population sur un histogramme
    - Les catégories standard d'IMC et sa position au sein de sa gatégorie le tout sur un bar chat horizontal
4.  La prédiction de son **niveau d’obésité** avec notre modèle XGBoost qui est ensuite traduit en une étiquette lisible (ex. : "Obésité Type I") et l'affichage des variables indépendantes de notre modèle selon leur niveau d'importance
5. Les résultats et informations sont affichées de façon claire et visuelle.
5. Une barre de progression améliore l’expérience utilisateur.

---

## 🛠️ Technologies utilisées

- `Python`
- `Pandas`, `Scikit-learn`, `XGBoost`
- `Streamlit` (interface utilisateur)
- `Time` pour manipuler le temps
- `Altair` pour la visualisation
- `joblib` pour la sauvegarde du modèle et de notre variable cible encodée

---

## 🚀 Lancer l’application localement

```Terminal
streamlit run webapp.py