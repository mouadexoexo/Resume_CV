from pathlib import Path

import streamlit as st
from PIL import Image
import base64




# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = Path(__file__).parent / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "mouad.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "BENALI Mouad"
PAGE_ICON = ":wave:"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

NAME = "BENALI Mouad"
DESCRIPTION = """
"""
EMAIL = "benalimouad1@gmail.com"
Tel = "+33 7 64 01 84 40"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mouadbenali/",
    "GitHub": "https://github.com/mouadexoexo",
}
Certif = {
    "🏆 Conférence internationale sur Information Communication & Cybersecurity ICI2C ": current_dir / "assets"/"certif.pdf",
    "🏆 Modélisation de bases de données": current_dir / "assets"/"base.pdf",
    "🏆 Réalisation un dashboard avec Tableau": current_dir / "assets"/"dash.pdf",
    "🏆 librairies Python pour la Data Science": current_dir / "assets"/"data.pdf",
    "🏆 Deep Learning": current_dir / "assets"/"deeplearning.pdf",
}





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
- ✔️ Une Expérience Solide dans l'extraction d'informations exploitables à partir des données
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
- 👩‍💻 Langages de programmation : Python, R, Sql, Scala, SAS
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
st.write("🚀","Missions")
st.write(
    """
- ► Création des bases de données.
- ► Collaboration étroite avec les équipes interfonctionnelles pour fournir des recommandations fondées sur les analyses de données.
- ► Data Cleaning : Préparation de nos données pour être analysé en nettoyant la base de données.
- ► Transformations de données : simplifier les données existantes en les modifiant ou en les restructurant
- ► Analyse Exploratoire : Faire une visualisations et des résumés pour examiner nos données pour mieux comprendre notre base de données.
- ► Création de Dashboards : Conception et développement de tableaux de bord interactifs pour présenter les résultats de l'analyse de données de manière convaincante.
- ► Mise en Production : Déploiement des modèles et solutions d'analyse dans des environnements de production, en veillant à leur fonctionnement optimal et à leur maintenance continue.

"""
)

st.write(" ✅","Résultats")
st.write(
    """
- ► Contribution significative à l'avancement de projets en cours.
- ► Finalisation réussie d'un projet, avec satisfaction client.
- ► Transformation efficace des données pour les rendre plus compréhensibles
"""
)

st.write( "🛠️","Environnement technique")
st.write("""
- ► Python : PySpark - Streamlit - pandas
- ► MYSQL WORKBENCH
- ► Streamlit
- ► Excel
- ► Spark
- ► Outil Interne de l'Entreprise
""")
st.write('\n')
st.write("-----------------")


# 2
st.write("🚧", "**Data scientist | Université IBN TOFAIL**")
st.write("janvier 2020 - Décembre 2020")
st.write( "🧩","Contexte")
st.write( "Réalisation un projet de création d'un système de prédiction novateur basé sur mon sujet de recherche doctorat")
st.write("🚀","Missions")
st.write(
    """
Réaliser un projet de recherche novateur visant à développer un système de prédiction basé sur les avancées de son sujet de thèse. Cette mission englobe la recherche, la conception, le développement et l'évaluation de solutions de pointe en matière de prédiction de données, tout en contribuant à l'avancement des connaissances dans le domaine de la science des données.

"""
)
st.write(" ✅","Résultats")
st.write("""
- ► Création d'un système de prédiction optimal des produits à vendre.
- ► Documenter et soumettre les résultats de la recherche à un journal scientifique de renom.
- ► Obtenir l'acceptation de la publication dans le journal.
- ► Présenter les résultats lors de conférences scientifiques de renom pour partager l'innovation et contribuer à la diffusion des connaissances dans le domaine de la data science.
""")
st.write( "🛠️","Environnement technique")
st.write("""
- ► Python : PCA - DTW - LCSS - Scikit-learn
- ► Méthodes de Similarité : LCSS - DTW - Distance EUclidean
- ► Flask
""")
st.write('\n')
st.write("-----------------")
# 3
st.write("🚧", "**Data Analyst | Marjane**")
st.write("octobre 2019 - janvier 2020")
st.write( "🧩","Contexte")
st.write("Marjane est un secteur de la grande distribution au Maroc qui propose une variété de produits, notamment des produits alimentaires, des produits électroniques, des vêtements, des articles ménagers, et bien plus encore. Pendant mon stage chez Marjane, j'ai eu l'opportunité de travailler au sein d'une équipe multidisciplinaire composée de développeurs, de spécialistes des données et de chefs de projet.")
st.write("🚀","Missions")
st.write(
    """
- ► Collecter, nettoyer, préparer et analyser des ensembles de données complexes liés aux ventes, aux stocks et aux préférences des clients.
- ► Mené une analyse rigoureuse des données pour évaluer la qualité des données, en identifiant les erreurs, les anomalies et les incohérences dans les jeux de données.
- ► Créé des tableaux de bord personnalisés en utilisant les outils internes de l'entreprise pour visualiser les données nettoyées et corrigées, fournissant ainsi une vue d'ensemble claire et précise de la qualité des données.
- ► Présenté de manière régulière des rapports de performance détaillés, mettant en avant les principaux indicateurs de performance (KPI) grâce aux tableaux de bord internes, tout en soulignant les améliorations de la qualité des données.
"""
)
st.write(" ✅","Résultats")
st.write(
    """
- ► Identification et résolution proactive des erreurs de données, améliorant ainsi la fiabilité des informations utilisées pour les décisions opérationnelles.
- ► Augmentation de la vitesse de prise de décision de l'équipe de gestion grâce à des tableaux de bord interactifs, ce qui a permis d'obtenir des résultats opérationnels plus rapides.
- ► Facilitation de l'accès aux données essentielles pour les équipes, améliorant ainsi la communication et la collaboration au sein de l'entreprise.
- ► Détection rapide et correction des anomalies dans les données de ventes
- ► Correction des données incorrectes ou obsolètes dans les bases de données, assurant la précision des informations utilisées pour les opérations et les décisions stratégiques.
"""
)
st.write( "🛠️","Environnement technique")
st.write("""
  - ►  Python: Pandas, NumPy et scikit-learn
  - ►  SQL - PostgreSQL
  - ►  Excel
  - ►  Outil Interne de l'Entreprise
""")

st.write("-----------------")


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Certificats de Compétence")
st.write("---")
pdf_data = {}
for certificat, filename in Certif.items():
    with open(filename, "rb") as pdf_file:
        pdf_data[certificat] = pdf_file.read()
        
for certificat, pdf_byte in pdf_data.items():
    pdf_path = f"[{certificat}]({filename})"
    #st.markdown(pdf_path)
    st.download_button(
        label=f"{certificat}",
        data=pdf_byte,
        file_name=f"{certificat}.pdf",
        mime="application/pdf",
    )

