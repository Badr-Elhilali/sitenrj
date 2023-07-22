import streamlit as st
import pandas as pd
from PIL import Image


import warnings
warnings.filterwarnings("ignore")

#from google.colab import drive
#drive.mount('/content/drive')

st.subheader('Machine learning')
st.write('Conservation des données colonnes : consommation, date, région, tarif,population')

st.markdown("* Variable cible : Consommation")
st.markdown("* Train test split 80/20")
st.markdown('* Ordre chronologie')
st.markdown('* Encoder région')


if st.button('Ramdomforest Classifier',key='classify'):
    st.subheader('Performance du modèle Radom Forest Regressor')
    st.markdown('* Train Score: 0.9912846928323011')
    st.markdown('* Test Score: 0.9233987229117269')
    
    st.subheader("Métrics")
    image1=Image.open("rd.png")
    st.image(image1)

    image3=Image.open("rd2.png")
    st.image(image3)

if st.button('Xgbost',key='xgb'):
    st.subheader('Performance du modèle Radom Xgboost')
    st.markdown('* Train Score: 0.999625080267915')
    st.markdown('* Test Score: 0.983290620866571')
    st.subheader("Métrics")
    image1=Image.open("perf2.png")
    st.image(image1)
    st.subheader("Comparaison entre les prédictions et les données réelles")
    
option=st.radio(
                        "Set selectbox label visibility",
                        key="visibility",
                        options=('Jour','Semaine','Mois'))

if option =='Jour':
                                g1=Image.open("day.png")
                                st.image(g1)
if option=='Semaine':
                                g2=Image.open("week.png")
                                st.image(g2)
if option=='Mois':
                                g3=Image.open("month.png")
                                st.image(g3)
                          
    


st.subheader('Importance des varibles')

image1=Image.open("imtreg.png")
st.image(image1)
st.subheader('Conclusion')

expander = st.expander("Objectifs")
expander.markdown("""
                        *  Comprendre la relation entre la consommation et la production des différentes sources d'énergie électrique :
                            - Consommations :small_red_triangle: Ile de france et Auvergne rhône alpes
                            - Productions :small_red_triangle: Auvergne rhône alpes et Grand Est

                            - Focus sur les énergies renouvelables :white_check_mark:
                        *  Produire un modèle permettant de calculer les estimations des consommations à venir pour les différents départements français
                            Meilleure modéle : XGBRegressor


                    """)



