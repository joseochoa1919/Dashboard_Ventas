import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ============================================================
# CONFIGURACIÓN
# ============================================================
st.set_page_config(
    page_title="Sales Intelligence | Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# ESTILOS PROFESIONALES + RESPONSIVE
# ============================================================
st.markdown("""
<style>

    /* ========================================================
       FONDO GENERAL
       ======================================================== */
    .stApp {
        background: #F5F7FB;
    }

    /* ========================================================
       SIDEBAR
       ======================================================== */
    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #111827 0%,
            #1F2937 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: #F9FAFB !important;
    }

    /* ========================================================
       OCULTAR ELEMENTOS DE STREAMLIT
       ======================================================== */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* ========================================================
       CONTENEDOR PRINCIPAL
       ======================================================== */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1500px;
    }

    /* ========================================================
       HEADER
       ======================================================== */
    .dashboard-header {
        background: linear-gradient(
            135deg,
            #111827 0%,
            #2563EB 100%
        );

        padding: 28px 32px;
        border-radius: 18px;
        margin-bottom: 24px;

        box-shadow:
            0 10px 30px rgba(17, 24, 39, 0.15);
    }

    .dashboard-title {
        color: white;
        font-size: 34px;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.8px;
    }

    .dashboard-subtitle {
        color: #DBEAFE;
        font-size: 15px;
        margin-top: 7px;
    }

    /* ========================================================
       KPI CARDS
       ======================================================== */
    .kpi-card {
        background: white;

        padding: 20px 22px;

        border-radius: 16px;

        border: 1px solid #E5E7EB;

        box-shadow:
            0 5px 18px rgba(15, 23, 42, 0.06);

        min-height: 125px;
    }

    .kpi-label {
        color: #6B7280;
        font-size: 13px;
        font-weight: 600;

        text-transform: uppercase;

        letter-spacing: 0.5px;
    }

    .kpi-value {
        color: #111827;
        font-size: 27px;
        font-weight: 800;

        margin-top: 8px;
    }

    .kpi-icon {
        font-size: 25px;
        float: right;
    }

    /* ========================================================
       SECCIONES
       ======================================================== */
    .section-title {
        color: #111827;

        font-size: 21px;

        font-weight: 750;

        margin: 26px 0 12px 0;
    }

    /* ========================================================
       INFORMACIÓN
       ======================================================== */
    .info-card {
        background: white;

        border: 1px solid #E5E7EB;

        border-radius: 14px;

        padding: 18px 20px;

        box-shadow:
            0 4px 14px rgba(15, 23, 42, 0.05);
    }

    /* ========================================================
       SIDEBAR
       ======================================================== */
    .sidebar-title {
        color: white;

        font-size: 22px;

        font-weight: 800;

        margin-bottom: 5px;
    }

    .sidebar-text {
        color: #CBD5E1;

        font-size: 13px;

        margin-bottom: 25px;
    }

    /* ========================================================
       DATAFRAME
       ======================================================== */
    div[data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
    }

    /* ========================================================
       BOTÓN DESCARGA
       ======================================================== */
    .stDownloadButton button {
        width: 100%;

        border-radius: 10px;

        font-weight: 600;
    }

    /* ========================================================
       RESPONSIVE - TABLETS
       ======================================================== */
    @media (max-width: 992px) {

        .block-container {
            padding-left: 20px !important;
            padding-right: 20px !important;
        }

        .dashboard-title {
            font-size: 29px;
        }

        .kpi-value {
            font-size: 24px;
        }

    }

    /* ========================================================
       RESPONSIVE - CELULARES
       ======================================================== */
    @media (max-width: 768px) {

        /* -----------------------------------------------
           CONTENEDOR
           ----------------------------------------------- */
        .block-container {
            padding-top: 1rem !important;
            padding-left: 12px !important;
            padding-right: 12px !important;
            padding-bottom: 1rem !important;
        }

        /* -----------------------------------------------
           HEADER
           ----------------------------------------------- */
        .dashboard-header {
            padding: 20px 18px;

            border-radius: 14px;

            margin-bottom: 16px;
        }

        .dashboard-title {
            font-size: 24px;

            line-height: 1.2;
        }

        .dashboard-subtitle {
            font-size: 13px;

            line-height: 1.4;
        }

        /* -----------------------------------------------
           KPI
           ----------------------------------------------- */
        .kpi-card {
            min-height: 95px;

            padding: 15px 16px;

            margin-bottom: 10px;

            border-radius: 13px;
        }

        .kpi-label {
            font-size: 11px;
        }

        .kpi-value {
            font-size: 22px;

            margin-top: 6px;
        }

        .kpi-icon {
            font-size: 20px;
        }

        /* -----------------------------------------------
           TÍTULOS
           ----------------------------------------------- */
        .section-title {
            font-size: 18px;

            margin-top: 20px;

            margin-bottom: 10px;
        }

        /* -----------------------------------------------
           SIDEBAR EN CELULAR
           ----------------------------------------------- */
        section[data-testid="stSidebar"] {

            min-width: 280px !important;

            max-width: 85vw !important;
        }

        /* -----------------------------------------------
           MULTISELECT
           ----------------------------------------------- */
        section[data-testid="stSidebar"]
        div[data-baseweb="select"] {

            width: 100% !important;
        }

        /* -----------------------------------------------
           GRÁFICOS
           ----------------------------------------------- */
        .js-plotly-plot {

            width: 100% !important;

            max-width: 100% !important;
        }

        /* -----------------------------------------------
           TABLA
           ----------------------------------------------- */
        div[data-testid="stDataFrame"] {

            width: 100% !important;

            overflow-x: auto !important;
        }

        /* -----------------------------------------------
           BOTÓN
           ----------------------------------------------- */
        .stDownloadButton button {

            min-height: 45px;

            font-size: 14px;
        }

    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# CARGAR DATOS
# ============================================================
@st.cache_data
def cargar_datos():

    df = pd.read_csv("base_datos_ventas.csv")

    df["Fecha"] = pd.to_datetime(df["Fecha"])

    df["Mes"] = df["Fecha"].dt.strftime("%b")

    df["Mes_Numero"] = df["Fecha"].dt.month

    return df


df = cargar_datos()


# ============================================================
# SIDEBAR / FILTROS
# ============================================================
with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">📊 Sales Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-text">'
        'Panel ejecutivo de análisis comercial'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("### 🔎 FILTROS")

    # --------------------------------------------------------
    # CIUDAD
    # --------------------------------------------------------
    ciudades = st.multiselect(
        "Ciudad",
        options=sorted(df["Ciudad"].unique()),
        default=sorted(df["Ciudad"].unique())
    )

    # --------------------------------------------------------
    # CATEGORÍA
    # --------------------------------------------------------
    categorias = st.multiselect(
        "Categoría",
        options=sorted(df["Categoria"].unique()),
        default=sorted(df["Categoria"].unique())
    )

    # --------------------------------------------------------
    # VENDEDOR
    # --------------------------------------------------------
    vendedores = st.multiselect(
        "Vendedor",
        options=sorted(df["Vendedor"].unique()),
        default=sorted(df["Vendedor"].unique())
    )

    # --------------------------------------------------------
    # MEDIO DE PAGO
    # --------------------------------------------------------
    medios = st.multiselect(
        "Medio de pago",
        options=sorted(df["Medio_Pago"].unique()),
        default=sorted(df["Medio_Pago"].unique())
    )

    st.markdown("---")

    st.caption("Periodo: Enero - Septiembre 2026")


# ============================================================
# FILTRAR DATOS
# ============================================================
df_filtrado = df[
    df["Ciudad"].isin(ciudades)
    &
    df["Categoria"].isin(categorias)
    &
    df["Vendedor"].isin(vendedores)
    &
    df["Medio_Pago"].isin(medios)
].copy()


# ============================================================
# HEADER
# ============================================================
st.markdown("""
<div class="dashboard-header">

    <div class="dashboard-title">
        📊 Dashboard Ejecutivo de Ventas
    </div>

    <div class="dashboard-subtitle">
        Sales Intelligence · Análisis comercial · Perú · 2026
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# KPIs
# ============================================================
ventas = df_filtrado["Venta_Total_Soles"].sum()

transacciones = len(df_filtrado)

unidades = df_filtrado["Cantidad"].sum()

ticket = (
    ventas / transacciones
    if transacciones
    else 0
)


# ------------------------------------------------------------
# COLUMNAS KPI
# ------------------------------------------------------------
k1, k2, k3, k4 = st.columns(4)


kpis = [

    (
        k1,
        "💰",
        "Ventas Totales",
        f"S/ {ventas:,.0f}"
    ),

    (
        k2,
        "🧾",
        "Transacciones",
        f"{transacciones:,}"
    ),

    (
        k3,
        "📦",
        "Unidades Vendidas",
        f"{unidades:,}"
    ),

    (
        k4,
        "🎫",
        "Ticket Promedio",
        f"S/ {ticket:,.0f}"
    )

]


for col, icon, label, value in kpis:

    with col:

        st.markdown(
            f"""
            <div class="kpi-card">

                <span class="kpi-icon">
                    {icon}
                </span>

                <div class="kpi-label">
                    {label}
                </div>

                <div class="kpi-value">
                    {value}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# EVOLUCIÓN MENSUAL
# ============================================================
st.markdown(
    '<div class="section-title">'
    '📈 Evolución de ventas'
    '</div>',
    unsafe_allow_html=True
)


ventas_mes = (

    df_filtrado

    .groupby(
        ["Mes_Numero", "Mes"],
        as_index=False
    )["Venta_Total_Soles"]

    .sum()

    .sort_values("Mes_Numero")

)


fig_mes = px.area(

    ventas_mes,

    x="Mes",

    y="Venta_Total_Soles",

    markers=True,

    template="plotly_white"

)


fig_mes.update_traces(

    line=dict(width=3),

    hovertemplate=
    "Ventas: S/ %{y:,.0f}<extra></extra>"

)


fig_mes.update_layout(

    height=360,

    margin=dict(
        l=10,
        r=10,
        t=15,
        b=10
    ),

    xaxis_title="",

    yaxis_title="Ventas (S/)",

    hovermode="x unified"

)


st.plotly_chart(

    fig_mes,

    use_container_width=True

)


# ============================================================
# CATEGORÍA Y CIUDAD
# ============================================================
col1, col2 = st.columns(2)


# ============================================================
# VENTAS POR CATEGORÍA
# ============================================================
with col1:

    st.markdown(
        '<div class="section-title">'
        '🏷️ Ventas por categoría'
        '</div>',
        unsafe_allow_html=True
    )


    cat = (

        df_filtrado

        .groupby(
            "Categoria",
            as_index=False
        )["Venta_Total_Soles"]

        .sum()

        .sort_values(
            "Venta_Total_Soles",
            ascending=True
        )

    )


    fig_cat = px.bar(

        cat,

        x="Venta_Total_Soles",

        y="Categoria",

        orientation="h",

        text="Venta_Total_Soles",

        template="plotly_white"

    )


    fig_cat.update_traces(

        texttemplate="S/ %{text:,.0f}",

        textposition="outside",

        hovertemplate=
        "S/ %{x:,.0f}<extra></extra>"

    )


    fig_cat.update_layout(

        height=340,

        margin=dict(
            l=10,
            r=50,
            t=10,
            b=10
        ),

        xaxis_title="Ventas (S/)",

        yaxis_title=""

    )


    st.plotly_chart(

        fig_cat,

        use_container_width=True

    )


# ============================================================
# VENTAS POR CIUDAD
# ============================================================
with col2:

    st.markdown(
        '<div class="section-title">'
        '🏙️ Ventas por ciudad'
        '</div>',
        unsafe_allow_html=True
    )


    ciudad = (

        df_filtrado

        .groupby(
            "Ciudad",
            as_index=False
        )["Venta_Total_Soles"]

        .sum()

        .sort_values(
            "Venta_Total_Soles",
            ascending=False
        )

    )


    fig_ciudad = px.bar(

        ciudad,

        x="Ciudad",

        y="Venta_Total_Soles",

        text="Venta_Total_Soles",

        template="plotly_white"

    )


    fig_ciudad.update_traces(

        texttemplate="S/ %{text:,.0f}",

        textposition="outside",

        hovertemplate=
        "S/ %{y:,.0f}<extra></extra>"

    )


    fig_ciudad.update_layout(

        height=340,

        margin=dict(
            l=10,
            r=10,
            t=10,
            b=10
        ),

        xaxis_title="",

        yaxis_title="Ventas (S/)"

    )


    st.plotly_chart(

        fig_ciudad,

        use_container_width=True

    )


# ============================================================
# VENDEDORES Y MEDIOS DE PAGO
# ============================================================
col3, col4 = st.columns(2)


# ============================================================
# RANKING VENDEDORES
# ============================================================
with col3:

    st.markdown(
        '<div class="section-title">'
        '👨‍💼 Ranking de vendedores'
        '</div>',
        unsafe_allow_html=True
    )


    vend = (

        df_filtrado

        .groupby(
            "Vendedor",
            as_index=False
        )["Venta_Total_Soles"]

        .sum()

        .sort_values(
            "Venta_Total_Soles",
            ascending=False
        )

    )


    fig_vend = px.bar(

        vend,

        x="Vendedor",

        y="Venta_Total_Soles",

        text="Venta_Total_Soles",

        template="plotly_white"

    )


    fig_vend.update_traces(

        texttemplate="S/ %{text:,.0f}",

        textposition="outside",

        hovertemplate=
        "S/ %{y:,.0f}<extra></extra>"

    )


    fig_vend.update_layout(

        height=340,

        margin=dict(
            l=10,
            r=10,
            t=10,
            b=10
        ),

        xaxis_title="",

        yaxis_title="Ventas (S/)"

    )


    st.plotly_chart(

        fig_vend,

        use_container_width=True

    )


# ============================================================
# MEDIOS DE PAGO
# ============================================================
with col4:

    st.markdown(
        '<div class="section-title">'
        '💳 Medios de pago'
        '</div>',
        unsafe_allow_html=True
    )


    pago = (

        df_filtrado

        .groupby(
            "Medio_Pago",
            as_index=False
        )["Venta_Total_Soles"]

        .sum()

    )


    fig_pago = px.pie(

        pago,

        names="Medio_Pago",

        values="Venta_Total_Soles",

        hole=0.55,

        template="plotly_white"

    )


    fig_pago.update_traces(

        textinfo="percent+label",

        hovertemplate=
        "%{label}: S/ %{value:,.0f}"
        "<extra></extra>"

    )


    fig_pago.update_layout(

        height=340,

        margin=dict(
            l=10,
            r=10,
            t=10,
            b=10
        ),

        showlegend=True

    )


    st.plotly_chart(

        fig_pago,

        use_container_width=True

    )


# ============================================================
# TABLA
# ============================================================
st.markdown(
    '<div class="section-title">'
    '📋 Detalle de ventas'
    '</div>',
    unsafe_allow_html=True
)


columnas = [

    "ID_Venta",
    "Fecha",
    "Cliente",
    "Ciudad",
    "Categoria",
    "Producto",
    "Vendedor",
    "Medio_Pago",
    "Cantidad",
    "Precio_Unitario_Soles",
    "Venta_Total_Soles"

]


tabla = (

    df_filtrado[columnas]

    .sort_values(
        "Fecha",
        ascending=False
    )

    .copy()

)


tabla["Fecha"] = (

    tabla["Fecha"]

    .dt.strftime("%d/%m/%Y")

)


st.dataframe(

    tabla,

    use_container_width=True,

    hide_index=True,

    column_config={

        "Venta_Total_Soles":

        st.column_config.NumberColumn(

            "Venta Total",

            format="S/ %.2f"

        ),

        "Precio_Unitario_Soles":

        st.column_config.NumberColumn(

            "Precio Unitario",

            format="S/ %.2f"

        ),

        "Cantidad":

        st.column_config.NumberColumn(

            "Cantidad",

            format="%d"

        )

    }

)


# ============================================================
# DESCARGA
# ============================================================
csv = (

    df_filtrado

    .to_csv(index=False)

    .encode("utf-8-sig")

)


st.download_button(

    label="⬇️ Descargar datos filtrados",

    data=csv,

    file_name="ventas_filtradas.csv",

    mime="text/csv"

)


# ============================================================
# FOOTER
# ============================================================
st.markdown("---")

st.markdown(

    "<center>"
    "<small>"
    "Dashboard desarrollado con Python · Pandas · Plotly · Streamlit"
    "</small>"
    "</center>",

    unsafe_allow_html=True

)
