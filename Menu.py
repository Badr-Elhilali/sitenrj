import streamlit as st
import pandas as pd
import numpy as np



#from Menu import --pour afficher les variable de la page principale

st.set_page_config(page_title='Menu',layout='wide')
st.sidebar.image('https://i0.wp.com/imprimer-cc.vocaleo.fr/files/2014/11/Fotolia_62378596_Subscription_XXL-ELECTRICITE.jpg?w=2250',caption='Online Analytics')


def main():
   
    st.title('Consommation en électricité de 2013-2022 en France')
    st.subheader('Présentation du sujet ')

if __name__=='__main__':
    main()
   
    st.write("""
                L’enjeux de la sécurité de l’approvisionnement en énergie est une question capitale. En effet, l’électricité a cette particularité de ne pas pouvoir être stockée en grande quantité.
    L'énergie électrique est aussi devenue un élément essentiel de la vie quotidienne et de l'activité économique moderne. Elle est utilisée pour alimenter les foyers, les industries et les transports. 

    Pour répondre à la demande croissante d'électricité, les fournisseurs d'énergie ont besoin de prévoir avec précision la consommation électrique future. La prévision de la consommation d'électricité est un enjeu clé pour garantir la fiabilité du système électrique, optimiser la production et minimiser les coûts.


    La prévision de la consommation d'électricité repose sur l'analyse de données historiques, qui permettent de détecter des tendances et des cycles saisonniers dans la consommation électrique. Les variables clés pour la prévision de la consommation d'électricité sont la date et l'heure, qui permettent de tenir compte des fluctuations de la demande au cours du temps, ainsi que les données de production d'énergie, comme la production thermique, nucléaire et éolienne.

    Il est important de retenir que la quantité d’électricité produite et injectée dans le réseau doit toujours être en équilibre.  A tout moment nous devons avoir une consommation égale à la production.
    Tout déséquilibre provoquerai un blackout total. 
    Dans ce projet, nous analyserons les consommations des régions afin d’anticiper les déséquilibres. Nous porterons une attention particulière aux énergies renouvelables.

             
             """)
    expander = st.expander("Objectifs")
    expander.markdown("""
                    	*  Comprendre la relation entre la consommation et la production des différentes sources d'énergie électrique
                         - Focus sur les énergies renouvelables
                    *  Produire un modèle permettant de calculer les estimations des consommations à venir pour les différents départements français


                   """)

    

    
   
