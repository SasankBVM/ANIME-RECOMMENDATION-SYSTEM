import streamlit as st,pickle as pk,pandas as pd,numpy as np
df=pd.read_csv('animes.csv')
similarity=pk.load(open('similarity.pkl','rb'))
with st.columns(3)[1]:
     st.image('anime.jpeg')
def recommend(anime):
        anime_index=df[df['title']==anime].index[0]
        similar=similarity[anime_index]
        anime_list=sorted(list(enumerate(similar)),reverse=True,key=lambda x:x[1])[1:6]
        recanim=[]
        for i in anime_list:
            anime_id=i[0]
            recanim.append(df.iloc[i[0]].title)
        return recanim
top_20=pk.load(open('top.pkl','rb'))
anime=pk.load(open('anime.pkl','rb'))
# top=set()
# for i in top_20:
#      top.add(i)
# top=list(top)
anime_list=anime['title'].values
st.title("ANIME RECOMENDATION SYSTEM")
anime_selected=st.selectbox(
    'SELECT THE ANIME',anime_list
)
if st.button("RECOMMEND"):
    recoma=recommend(anime_selected)
    for i in recoma:
        st.write(i)
if st.checkbox("TOP 20 ANIMES BASED ON POPULARITY"):
     st.write("One Peice")
     st.write("Naruto")
     st.write("Naruto Shippuden")
     for i in range(1,18):
            if top_20[i]!='Gintama.':
                st.write(top_20[i])
            if top_20[i]=='Fullmetal Alchemist: Brotherhood':
                 st.write(top_20[i])
                 st.write("Shingeki No Kyojin")
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)