import plotly.express as px


def bar_chart(
    dataframe,
    x,
    y,
    title,
    color="#3B82F6"
):

    fig = px.bar(
        dataframe,
        x=x,
        y=y,
        text_auto=".2s",
        title=title
    )

    fig.update_traces(

        marker_color=color,

        marker_line_width=0,

        textposition="outside",

        hovertemplate=
        "<b>%{x}</b><br>" +
        "%{y:,.0f}<extra></extra>"
    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="#0B1120",

        plot_bgcolor="#0B1120",

        height=470,

        title=dict(

            x=0.02,

            font=dict(
                size=24
            )

        ),

        font=dict(
            family="Segoe UI"
        ),

        margin=dict(

            l=20,

            r=20,

            t=60,

            b=20

        ),

        xaxis=dict(

            showgrid=False,

            zeroline=False

        ),

        yaxis=dict(

            gridcolor="rgba(255,255,255,.08)",

            zeroline=False

        )

    )

    return fig


def pie_chart(
    dataframe,
    names,
    values,
    title
):

    fig = px.pie(

        dataframe,

        names=names,

        values=values,

        hole=.55,

        title=title,

        color_discrete_sequence=px.colors.sequential.Blues_r

    )

    fig.update_traces(

        textinfo="percent+label",

        hovertemplate=
        "<b>%{label}</b><br>" +
        "%{value:,.0f}<br>" +
        "%{percent}<extra></extra>"
    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="#0B1120",

        height=470,

        title=dict(

            x=0.02,

            font=dict(
                size=24
            )

        ),

        font=dict(
            family="Segoe UI"
        ),

        margin=dict(

            l=20,

            r=20,

            t=60,

            b=20

        )

    )

    return fig