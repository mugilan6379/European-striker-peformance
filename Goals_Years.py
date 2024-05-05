import streamlit as st
import pandas as pd
import altair as alt

def goalsvsyears(main_file, year_chosen,league_chosen): 
    source_file = pd.read_csv('Data/StrikerAnalysis.csv')
    #source_file = source_file[source_file['League'] != main_file['League'][0]]
    grouped_data = main_file.groupby(['Club', 'Year'])['Goals'].sum().reset_index()
    grouped_data['Year'] = grouped_data['Year'].astype(int)

   
    average_goals = grouped_data['Goals'].mean()
    ref_data = pd.DataFrame({'y': [average_goals], 'label': 'Average Goals scored'})

    referenceLine = alt.Chart(ref_data).mark_rule(color='steelblue', strokeDash=[10, 10]).encode(
        y='y'
    )
    label = alt.Chart(ref_data).mark_text(
        align='right',
        baseline='bottom',
        dx=5).encode(
        y='y',
        text='label',
        color='red'
    )
    bar = alt.Chart(grouped_data).mark_bar().encode(
        x=alt.X('Club:N', sort='-y'),
        y='Goals:Q',
        tooltip=['Club', 'Goals', 'Year'],
        color=alt.condition(
            alt.datum.Goals > average_goals,  
            alt.value('steelblue'), 
            alt.value('red')  
        )
    ).properties(
        width=600,
        height=500,
        title=f'Goals scored by each team in {league_chosen}'
    )
    
    our_Chart = alt.layer(bar, referenceLine, label)

    css = """
    <style>
        div.vega-embed > div {
            transition: transform 0.2s ease-in-out; 
        }
        div.vega-embed > div:hover {
            transform: scale(1.15); 
            z-index: 10; 
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

    return st.altair_chart(our_Chart)

