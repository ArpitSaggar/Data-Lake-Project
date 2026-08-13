import streamlit as st

def load_css():

    st.markdown("""

<style>

/* -----------------------------
Main Background
------------------------------*/

.stApp{
    background:#0B1120;
}

/* -----------------------------
Container
------------------------------*/

.block-container{
    padding-top:1.5rem;
    padding-bottom:2rem;
    max-width:1400px;
}

/* -----------------------------
Header
------------------------------*/

.header-box{

background:linear-gradient(
135deg,
#2563EB,
#1D4ED8,
#0F172A
);

padding:35px;

border-radius:22px;

box-shadow:
0px 10px 40px rgba(37,99,235,.35);

margin-bottom:30px;

}

.header-title{

font-size:42px;

font-weight:800;

color:white;

text-align:center;

}

.header-subtitle{

font-size:18px;

color:#E2E8F0;

text-align:center;

margin-top:15px;

}

/* -----------------------------
Section Titles
------------------------------*/

.section-title{

font-size:30px;

font-weight:700;

color:white;

margin-top:15px;

margin-bottom:20px;

}

/* -----------------------------
Metric Cards
------------------------------*/

.metric-card{

background:linear-gradient(
145deg,
#111827,
#1F2937
);

padding:22px;

border-radius:18px;

border:1px solid rgba(255,255,255,.08);

transition:.35s;

box-shadow:
0px 12px 30px rgba(0,0,0,.35);

}

.metric-card:hover{

transform:translateY(-6px);

border:1px solid #2563EB;

box-shadow:
0px 20px 35px rgba(37,99,235,.35);

}

.metric-title{

color:#CBD5E1;

font-size:14px;

font-weight:600;

text-align:center;

letter-spacing:1px;

margin-bottom:10px;

}

.metric-value{

color:white;

font-size:34px;

font-weight:800;

text-align:center;

}

/* -----------------------------
Sidebar
------------------------------*/

section[data-testid="stSidebar"]{

background:#111827;

}

/* -----------------------------
Buttons
------------------------------*/

.stButton>button{

background:#2563EB;

color:white;

border-radius:10px;

border:none;

padding:.6rem 1rem;

font-weight:600;

}

.stButton>button:hover{

background:#1D4ED8;

}

/* -----------------------------
Tables
------------------------------*/

[data-testid="stDataFrame"]{

border-radius:14px;

overflow:hidden;

}

/* -----------------------------
Footer
------------------------------*/

.footer{

text-align:center;

padding:25px;

font-size:14px;

color:#94A3B8;

}

</style>

""", unsafe_allow_html=True)