from pathlib import Path

import streamlit as st
from PIL import Image
import base64


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv_data_analyst_scientist.pdf"
profile_pic = current_dir / "assets" / "mouad.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "BENALI Mouad"
PAGE_ICON = ":wave:"
NAME = "BENALI Mouad"
DESCRIPTION = """
Ingénieure Data Analyst/ Data Scientist
"""
EMAIL = "benalimouad1@gmail.com"
Tel = "+33 7 64 01 84 40"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mouadbenali/",
    "GitHub": "https://github.com",
}
Certif = {
    "🏆 Conférence internationale sur Information Communication & Cybersecurity ICI2C ": current_dir / "assets"/"certif.pdf",
    "🏆 Modélisation de bases de données": current_dir / "assets"/"base.pdf",
    "🏆 Réalisation un dashboard avec Tableau": current_dir / "assets"/"dash.pdf",
    "🏆 librairies Python pour la Data Science": current_dir / "assets"/"data.pdf",
    "🏆 Deep Learning": current_dir / "assets"/"deeplearning.pdf",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("☎️", Tel)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Résumé Professionnel")
st.write(
    """
- ✔️ 4 ans d'expérience dans l'extraction d'informations exploitables à partir des données
- ✔️ Solide expérience pratique et connaissance en Python
- ✔️ Connaissance des bases de données SQL et l'optimisation de requêtes SQL.
- ✔️ Capacité à communiquer efficacement des résultats d'analyse de données aux parties prenantes non techniques.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Compétences")
st.write(
    """
- 👩‍💻 Langages de programmation : Python, R, Sql, Scala
- 🗄️ Base de données : Spark, PL/Sql, MYSQL, Hadoop, PostgreSQL.
- 📊 Dashboard Et Visualisation : Power BI, Streamlit, MS EXCEL
- 📚 Modeling: Régression linéaire, Régression logistique, PCA, K-Means Clustering, Arbres de décision, Forêts aléatoires
- 📟 L'environnement de développement intégré (IDE) : Xcode, Visual Studio, Jupyter-Notebook.
- 🌐 Outils de développement et de gestion de code : Gitlab, Docker
- 📶 Outils de gestion de données : MySQL Workbench
- ☁️ Cloud Computing: Aws

"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Expériences Professionelles")
st.write("---")

#  1
st.write("🚧", "**Data scientist - Analyst | PocketResult**")
st.write("Mars 2023 - Septembre 2023")
st.write(
    """
- ► Création des bases de données
- ► Collaboration étroite avec les équipes interfonctionnelles pour fournir des recommandations fondées sur les analyses de données.
- ► Data Cleaning : Préparation de nos données pour être analysé en nettoyant la base de données.
- ► Transformations de données : simplifier les données existantes en les modifiant ou en les restructurant
- ► Analyse Exploratoire : Faire une visualisations et des résumés pour examiner nos données pour mieux comprendre notre base de données. Création de Dashboards : Conception et développement de tableaux de bord interactifs pour présenter les résultats de l'analyse de données de manière convaincante.
- ► Mise en Production : Déploiement des modèles et solutions d'analyse dans des environnements de production, en veillant à leur fonctionnement optimal et à leur maintenance continue.

"""
)

# 2
st.write('\n')
st.write("🚧", "**Data scientist | Université IBN TOFAIL**")
st.write("janvier 2020 - Décembre 2020")
st.write(
    """
- ► Réalistion un projet de création d'un système de prédiction novateur basé sur mon sujet de recherche doctorat:
- *** Réalisation d'une analyse des données approfondie pour la sélection de produits optimaux à vendre.
- *** Utilisation d'un modèle basé sur la distance euclidienne pour comparer un produit optimal avec un ensemble de produits.
- *** Prédiction efficace du produit optimal à vendre en se basant sur les résultats de la comparaison.
- *** Création d'une interface graphique conviviale pour faciliter l'utilisation du système de prédiction par les utilisateurs.
"""
)
st.write('\n')
# 3
st.write("🚧", "**Data Analyst | Marjane**")
st.write("octobre 2019 - janvier 2020")
st.write(
    """
- ► Collecter, nettoyer, préparer et analyser des ensembles de données complexes liés aux ventes, aux stocks et aux préférences des clients.
- ► Mené une analyse rigoureuse des données pour évaluer la qualité des données, en identifiant les erreurs, les anomalies et les incohérences dans les jeux de données.
- ► Créé des tableaux de bord personnalisés en utilisant les outils internes de l'entreprise pour visualiser les données nettoyées et corrigées, fournissant ainsi une vue d'ensemble claire et précise de la qualité des données.
- ► Présenté de manière régulière des rapports de performance détaillés, mettant en avant les principaux indicateurs de performance (KPI) grâce aux tableaux de bord internes, tout en soulignant les améliorations de la qualité des données.
"""
)




# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Certificats de Compétence")
st.write("---")
for certificat, filename in Certif.items():
    pdf_path = f"[{certificat}]({filename})"
    #st.markdown(pdf_path)
    st.download_button(
        label=pdf_path,
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
