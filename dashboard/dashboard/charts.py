import plotly.express as px


def bar_chart(df, x, y, title):

    fig = px.bar(
        df,
        x=x,
        y=y,
        title=title,
        text_auto=True
    )

    fig.update_layout(
        template="plotly_dark",
        height=450,
        title_x=0.02,
        margin=dict(l=20, r=20, t=60, b=20),
        paper_bgcolor="#0E1117",
        plot_bgcolor="#0E1117"
    )

    return fig


def pie_chart(df, names, values, title):

    fig = px.pie(
        df,
        names=names,
        values=values,
        hole=0.55
    )

    fig.update_layout(
        title=title,
        template="plotly_dark",
        height=450,
        margin=dict(l=20, r=20, t=60, b=20),
        paper_bgcolor="#0E1117"
    )

    return fig