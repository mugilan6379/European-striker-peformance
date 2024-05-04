import altair as alt


def scatter_plot(file,x,y,title):
     return alt.Chart(file,title=title).mark_circle(size=100).encode(
        x=x,
        y=y,
        tooltip=[x,y,'Player Names']
    ).interactive()

