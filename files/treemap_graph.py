import streamlit as st
import plotly.express as px

def draw_treemap(main_file,league_chosen):
    st.write('')
    st.write("This interactive treemap visualization showcases goal scoring statistics by top players, grouped by their clubs. Each segment represents a player and is sized by their goal tally, with details displayed on hover. The graph provides a visual comparison of players' performances within clubs and across leagues. Additionally, an expandable section titled 'Check the data for top scorer each team' allows for deeper exploration of each team’s leading scorers, enhancing user engagement with dynamic, responsive visual insights.")
    treemap = main_file[["League","Club","Goals","Player Names"]].groupby(by = ["League","Club","Player Names"])["Goals"].sum().reset_index()
    fig4 = px.treemap(treemap, path = ["Club","Player Names"], values = "Goals",
                  hover_name = "Goals",
                  hover_data = ["Goals"],
                  color = "Club", height = 700, width = 600)
    fig4.update_traces(textinfo="label+value")
    st.plotly_chart(fig4,use_container_width=True)
    expander = st.expander("Check the data for top scorer each team")
    expander.write(treemap)
