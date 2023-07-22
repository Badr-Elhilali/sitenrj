import streamlit as st
import pandas as pd

st.subheader('Présentation des données')
@st.cache_data(persist=True,max_entries=500)

def load_data():
    data=pd.read_csv('./bdd/conso.csv')
    return data
#affichage de la table de donnée
df=load_data()
df_sample=df.sample()
if st.sidebar.checkbox('Afficher les Donnée brutes', False):
    st.subheader('Jeu de données Consommations en éléctricité de 10 observations')
    st.write(df)

st.subheader('Identification des sources de données')
st.write("""
        Le jeu de données dont nous disposons concerne la consommation d'énergie électrique en France ainsi que la production des différentes sources d'énergie électrique, telles que l'énergie nucléaire, thermique et éolienne. Ces données sont collectées à une résolution horaire sur une période de plusieurs années.
        Les données principales proviennent du portail d’Open Data Réseaux Énergies.

        Les données de consommation présentent les données régionales depuis année 2013.  
        Nous y trouverons les données de consommation et la production selon les différentes filières composant le mix énergétique avec des mesures prises toutes les demi-heures. 



         """)

st.subheader('Ajout de données complémentaires')
st.markdown("""
                    	* Température 
            * Densité de population
            * Tarif

                   """)

st.subheader('Présentation finale des données')
df=pd.read_csv("./df/df_year.csv",index_col=0)
st.write(df.columns)




