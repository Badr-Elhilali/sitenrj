import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import seaborn as sns
import numpy as np


st.title('Analyse des données')

st.header('Analyse de la consommation et de la production')
st.subheader('La Consommation par Année de 2013 à 2021')


df=pd.read_csv("./df/df_day.csv",index_col=0)
#df=df[df['year']<2022]

st.write(df.shape)
st.write(df.head())
st.write(df.columns)

st.subheader("La consommation en MW d'électricité par année")

# La consommation d'électricité par année
def conso(df):
    df=df[df['year']<2022]
    consommation_par_annee = df.groupby("year")["Consommation (MW)"].sum()
 
conso(df)
st.image('consor.png')
st.write("1-Tendance globale de la consommation : Globalement, la consommation d'électricité a montré une tendance à la hausse au cours des dernières années. Cela peut être dû à une augmentation de la demande d'électricité dans divers secteurs économiques et sociaux")
st.write("1-Pic de consommation : Nous pouvons identifier certaines années où la consommation a atteint son niveau le plus élevé. Ces pics peuvent être associés à des événements spécifiques, tels que des périodes de forte chaleur ou des augmentations de l'activité industrielle.")
st.write("2-Variations annuelles : Malgré la tendance générale à la hausse, nous remarquons également des variations annuelles de la consommation. Ces fluctuations peuvent être influencées par des facteurs saisonniers, des politiques énergétiques, ou des changements économiques.")
st.write("3-Impacts des mesures d'efficacité énergétique : Si des politiques d'efficacité énergétique ont été mises en œuvre au fil des années, elles pourraient avoir joué un rôle dans la stabilisation ou la réduction de la croissance de la consommation d'électricité.")
st.write("")
df_day=pd.read_csv("./df/df_day.csv",index_col=0)
                 
# Évolution de la production d'électricité par source au fil du temps

def load_data():
    data=pd.read_csv('./df/df_day.csv')
    return data
#affichage de la table de donnée
df_load=load_data()

#selectbox production
st.subheader("La production en MW d'électricité")
option=st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=['Thermique (MW)', 
          'Nucléaire (MW)', 
          'Eolien (MW)',
            'Solaire (MW)', 
            'Hydraulique (MW)', 
            'Pompage (MW)',
            'Bioénergies (MW)'],
    )
 #bloquer les axes 
df_day=df_day[df_day['year']<2022] 
def lineplot():

    if option =='Thermique (MW)':
        st.bar_chart(data=df_day[['Thermique (MW)','year']],x='year')
        st.write("Production thermique : La production d'électricité à partir de sources thermiques semble avoir été la principale source d'énergie au début de la période étudiée, mais on peut observer une diminution progressive de cette production au fil des années.")
    elif option=='Nucléaire (MW)':
        st.bar_chart(data=df_day[['Nucléaire (MW)','year']],x='year')
        st.write("Production nucléaire : La production d'électricité à partir de sources nucléaires a maintenu une certaine stabilité au cours des années, avec des variations mineures")
    elif option=='Eolien (MW)':
        st.bar_chart(data=df_day[['Eolien (MW)','year']],x='year')
    elif option=='Solaire (MW)':
        st.bar_chart(data=df_day[['Solaire (MW)','year']],x='year')
        st.write("Énergie éolienne et solaire : Les sources d'énergie éolienne et solaire ont connu une augmentation significative de leur production d'électricité au fil du temps, reflétant une adoption croissante des énergies renouvelables")
    elif option=='Hydraulique (MW)':
        st.bar_chart(data=df_day[['Hydraulique (MW)','year']],x='year')
    elif option=='Pompage (MW)':
        st.bar_chart(data=df_day[['Pompage (MW)','year']],x='year')
        st.write("Production hydraulique et pompage : La production d'électricité à partir de sources hydrauliques et de pompage a montré des variations en fonction des conditions climatiques et des besoins en électricité.")
    elif option=='Bioénergies (MW)':
        st.bar_chart(data=df_day[['Bioénergies (MW)','year']],x='year')
        st.write("Bioénergies : La production d'électricité à partir de sources de bioénergies a également connu une augmentation constante, soulignant l'intérêt croissant pour les sources d'énergie renouvelables.")
lineplot()

st.subheader("Répartition de la consommation par région en 2021")
image8=Image.open("2021.png")
st.image(image8)

st.subheader("La distribution de la consommation d'électricité en fonction des régions")
image2=Image.open("p3.png")
st.image(image2)


st.subheader("La matrice de corrélation des variables")
image3=Image.open("h1.png")
st.image(image3)

st.subheader("La production en MW d'électricité par région")
image1=Image.open("i2.png")
st.image(image1)




st.subheader("La consommation et la production selon les régions - 2021")
image4=Image.open("carte.png")
st.image(image4)

st.subheader("L'évolution de la production des énergies en france")
image5=Image.open("nrjv.png")
st.image(image5)
st.subheader("La production en énergie renouvelable par région")
vert=Image.open("vert.png")
st.image(vert)


st.subheader("L'équilibre de production consommation éléctrique")
image6=Image.open("eq.png")
st.image(image6)

