import streamlit as st
import pandas as pd
import ScatterPlot
import Goals_Years
import maps
import shots_goalsXG
from logo import laliga_logo
from logo import bundesliga_logo
from logo import ligue1
from logo import prem_logo
from logo import serieA_logo
from logo import ligue2
import json,time
from league_details import leagues
import treemap_graph

@st.cache_data 
def load_data(csv):
    df = pd.read_csv(csv)
    return df
@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
    
@st.cache_resource
def display_animation():
    image_placeholder=st.empty()
    image_placeholder.image('https://cdn.dribbble.com/users/494229/screenshots/1601132/loadingicon14.gif')
    time.sleep(3)
    image_placeholder.empty()
    


display_animation()
st.header("Performance Trends of European Football Strikers: 2018-2020")

main_file=load_data('Data/StrikerAnalysis.csv')
year=main_file['Year'].unique()
year_chosen=st.sidebar.selectbox('**Select a year**',year)
league=main_file['League'].unique()
league=['La Liga','Bundesliga','France Ligue 1','Premier League','Serie A','France Ligue 2']
league_chosen=st.sidebar.selectbox('**Select the league**',league)


if league_chosen=='La Liga':
    laliga_logo.laligaLogo()
elif league_chosen=='Bundesliga':
    bundesliga_logo.bundesligaLogo()
elif league_chosen=='France Ligue 1':
    ligue1.ligue1Logo()
elif league_chosen=='Premier League':
    prem_logo.premLogo()
elif league_chosen=='Serie A':
    serieA_logo.serieALogo()
else:
    ligue2.ligue2Logo()
filtered_data=main_file[main_file['League']==league_chosen]
country=filtered_data['Country'].unique()
st.sidebar.write('Country: ',f'{country[0]}')
top_chosen=st.sidebar.select_slider('Select how many players you want to compare',options=list(range(0,50)),value=15)


tab1,tab2,tab3,tab4,tab5=st.tabs(['Country of the League','Goals vs XG','Goals by Clubs','Has the Striker met Expectation?','Goals scored by each team'])

main_file=main_file[main_file['Year']==year_chosen]
main_file=main_file[main_file['League']==league_chosen].sort_values(by='Goals',ascending=False)

with tab1:  
    st.header(f'{league_chosen} belongs to {country[0]}')
    
    if league_chosen=='La Liga':
        st.write(leagues.laliga_detail)
    elif league_chosen=='Bundesliga':
        st.write(leagues.bundesliga_detail)
    elif league_chosen=='France Ligue 1':
        st.write(leagues.ligue1_detail)
    elif league_chosen=='Premier League':
        st.write(leagues.prem_detail)
    elif league_chosen=='Serie A':
        st.write(leagues.serieA_detail)
    else:
        st.write(leagues.ligue2_detail)
    col1, col2, col3 = st.columns([1, 2, 1])    
    with col2:
        st.header('')
        maps.mapsViz(main_file,league_chosen)
    
    
    
    
with tab2:
    st.write(f"This graph presents a comparison between the actual goals scored and the expected goals (xG) for the top goal scorers in **{league_chosen}** for the year **{year_chosen}**.") 
    st.write('On the y-axis, we have the  goals (xG), which estimate the number of goals a player should have scored based on the quality of shots taken. The x-axis shows the actual number of goals scored by each player.')
    st.write('Each point on the graph represents a player, positioned according to their performance in terms of scoring and the quality of chances they received. Players closer to or above the line y = x performed as expected or exceeded their expected goals.')
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.header('')
        st.altair_chart(ScatterPlot.scatter_plot(main_file.head(top_chosen),'Goals','X G','Goals vs XG'))
    
    
    
with tab3:
    st.write("This graph presents the total goals scored by each football club over various years. Each bar represents a club, sorted in descending order based on the number of goals. The colors of the bars indicate whether the goals scored by a club are **above (steelblue) or below (red)** the average goals scored across all clubs. **A dashed steelblue line marks the average goals scored**, providing a reference point for comparing each club’s performance. Detailed information about the club, goals, and the year is available via tooltips when hovering over each bar. The graph aims to visually emphasize the clubs' scoring achievements relative to the overall average within the chosen league.")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.header('')
        Goals_Years.goalsvsyears(main_file,year_chosen,league_chosen)
    
    
    
with tab4:
    file_path='graph_text.txt'
    with open(file_path, 'r') as file:
        file_contents = file.read()
    st.markdown(f'{file_contents}')
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.header('')
        shots_goalsXG.expectation(main_file)
    
    

with tab5:
    treemap_graph.draw_treemap(main_file,league_chosen)
