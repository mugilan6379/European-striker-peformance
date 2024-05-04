import streamlit as st
import altair as alt
import ScatterPlot
import pandas as pd

def expectation(main_file):
    exp=1
    ref_data=pd.DataFrame({'x':[exp],'label':'Expectation = 1'})
    ref_line=alt.Chart(ref_data).mark_rule(color='steelblue', strokeDash=[10, 10]).encode(
        x='x:Q'
    )
    label=alt.Chart(ref_data).mark_text(
        align='right',
        baseline='bottom',
        dx=5).encode(
        x='x:Q',
        text='label:N'
    )
    s_plot=alt.Chart(main_file,title='Expectation of the Striker').mark_circle(size=100).encode(
        x='Goals/xG',
        y='Shots',
        tooltip=['Goals/xG','Shots','Player Names'],
        color=alt.condition(
            alt.datum['Goals/xG']>1,
            alt.value('steelblue'), 
            alt.value('red')  
        )
    ).interactive()
    #s_plot=ScatterPlot.scatter_plot(main_file,'Goals/xG','Shots','Expectation of the Striker')
    our_chart=alt.layer(s_plot,ref_line,label)

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
    return st.altair_chart(our_chart)
