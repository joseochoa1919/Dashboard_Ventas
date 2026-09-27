import streamlit as st
import pandas as pd
import plotly.express as px

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
# DISEÑO CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #F5F7FB;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #1F2937 100%);
    min-width: 280px;
}

section[data-testid="stSidebar"] * {
    color: #F9FAFB !important;
}

.block-container {
    max-width: 1500px;
    padding: 1.5rem 2rem 2rem 2rem;
}

/* HEADER */

.dashboard-header {
    background: linear-gradient(135deg, #111827 0%, #2563EB 100%);
    padding: 28px 32px;
    border-radius: 18px;
    color: white;
    margin-bottom: 22px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.10);
}

.dashboard-header h1 {
    margin: 0;
    font-size: 32px;
    font-weight: 700;
}

.dashboard-header p {
    margin: 7px 0 0 0;
    font-size: 15px;
    opacity: 0.90;
}

/* KPI */

.kpi-card {
    background: white;
    border-radius: 16px;
    padding: 20px;
    min-height: 145px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06);
    border: 1px solid #E5E7EB;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.kpi-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.10);
}

.kpi-icon {
    width: 45px;
    height: 45px;
    border-radius: 12px;
    background: #EFF6FF;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 23px;
    margin-bottom: 10px;
}

.kpi-title {
    color: #6B7280;
    font-size: 14px;
    margin-bottom: 6px;
    font-weight: 500;
}

.kpi-value {
    color: #111827;
    font-size: 26px;
    font-weight: 700;
}

/* TÍTULOS */

.section-title {
    color: #111827;
    font-size: 20px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 10px;
}

/* SIDEBAR */

.sidebar-title {
    font-size: 23px;
    font-weight: 700;
    color: white !important;
    margin-bottom: 4px;
}

.sidebar-text {
    font-size: 13px;
    color: #D1D5DB !important;
    margin-bottom: 18px;
}

/* BOTÓN DESCARGA */

div[data-testid="stDownloadButton"] button {
    width: 100%;
    min-height: 45px;
    border-radius: 10px;
    font-weight: 600;
}

/* TABLA */

[data-testid="stDataFrame"] {
    width: 100%;
}

/* RESPONSIVE TABLET */

@media (max-width: 992px) {

    .block-container {
        padding: 1rem;
    }

    .dashboard-header {
        padding: 22px 20px;
    }

    .dashboard-header h1 {
        font-size: 27px;
    }

    .kpi-value {
        font-size: 24px;
    }

    section[data-testid="stSidebar"] {
        min-width: 280px;
        max-width: 85vw;
    }
}

/* RESPONSIVE CELULAR */

@media (max-width: 768px) {

    .block-container {
        padding: 0.8rem 0.7rem 1.5rem 0.7rem;
    }

    .dashboard-header {
        padding: 18px 16px;
        border-radius: 12px;
    }

    .dashboard-header h1 {
        font-size: 22px;
        line-height: 1.2;
    }

    .dashboard-header p {
        font-size: 12px;
    }

    .kpi-card {
        padding: 15px;
        min-height: 125px;
    }

    .kpi-icon {
        width: 38px;
        height: 38px;
        font-size: 19px;
        border-radius: 10px;
    }

    .kpi-title {
        font-size: 12px;
    }

    .kpi-value {
        font-size: 19px;
    }

    .section-title {
        font-size: 17px;
    }

    section[data-testid="stSidebar"] {
        min-width: 280px;
        max-width: 88vw;
    }

    .stPlotlyChart {
        width: 100% !important;
    }
}

/* CELULARES PEQUEÑOS */

@media (max-width: 480px) {

    .dashboard-header h1 {
        font-size: 20px;
    }

    .dashboard-header p {
        font-size: 11px;
    }

    .kpi-card {
        padding: 12px;
        min-height: 115px;
    }

    .kpi-icon {
        width: 34px;
        height: 34px;
        font-size: 17px;
    }

    .kpi-value {
        font-size: 17px;
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

    df["Fecha"] = pd.to_datetime(
        df["Fecha"],
        errors="coerce"
    )

    df["Mes"] = df["Fecha"].dt.strftime("%B")
    df["Mes_Numero"] = df["Fecha"].dt.month

    return df


df = cargar_datos()

# ============================================================
# SIDEBAR - FILTROS
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">📊 Sales Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-text">Panel ejecutivo de análisis comercial</div>',
        unsafe_allow_html=True
    )

    st.markdown("### 🔎 FILTROS")

    ciudades = st.multiselect(
        "Ciudad",
        sorted(df["Ciudad"].dropna().unique()),
        default=sorted(df["Ciudad"].dropna().unique())
    )

    categorias = st.multiselect(
        "Categoría",
        sorted(df["Categoria"].dropna().unique()),
        default=sorted(df["Categoria"].dropna().unique())
    )

    vendedores = st.multiselect(
        "Vendedor",
        sorted(df["Vendedor"].dropna().unique()),
        default=sorted(df["Vendedor"].dropna().unique())
    )

    medios = st.multiselect(
        "Medio de pago",
        sorted(df["Medio_Pago"].dropna().unique()),
        default=sorted(df["Medio_Pago"].dropna().unique())
    )

    st.markdown("---")

    st.caption("Periodo: Enero - Septiembre 2026")

# ============================================================
# FILTRAR DATOS
# ============================================================

df_filtrado = df[
    df["Ciudad"].isin(ciudades)
    & df["Categoria"].isin(categorias)
    & df["Vendedor"].isin(vendedores)
    & df["Medio_Pago"].isin(medios)
].copy()

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="dashboard-header">

    <h1>📊 Dashboard Ejecutivo de Ventas</h1>

    <p>
        Sales Intelligence · Análisis comercial · Perú · 2026
    </p>

</div>
""", unsafe_allow_html=True)

# ============================================================
# KPIs
# ============================================================

ventas_totales = df_filtrado["Venta_Total_Soles"].sum()

transacciones = len(df_filtrado)

unidades = df_filtrado["Cantidad"].sum()

ticket_promedio = (
    ventas_totales / transacciones
    if transacciones > 0
    else 0
)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:

    st.markdown(
        f"""
        <div class="kpi-card">

            <div class="kpi-icon">
                💰
            </div>

            <div class="kpi-title">
                Ventas Totales
            </div>

            <div class="kpi-value">
                S/ {ventas_totales:,.2f}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with kpi2:

    st.markdown(
        f"""
        <div class="kpi-card">

            <div class="kpi-icon">
                🧾
            </div>

            <div class="kpi-title">
                Transacciones
            </div>

            <div class="kpi-value">
                {transacciones:,}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with kpi3:

    st.markdown(
        f"""
        <div class="kpi-card">

            <div class="kpi-icon">
                📦
            </div>

            <div class="kpi-title">
                Unidades Vendidas
            </div>

            <div class="kpi-value">
                {unidades:,}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with kpi4:

    st.markdown(
        f"""
        <div class="kpi-card">

            <div class="kpi-icon">
                🎫
            </div>

            <div class="kpi-title">
                Ticket Promedio
            </div>

            <div class="kpi-value">
                S/ {ticket_promedio:,.2f}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# EVOLUCIÓN MENSUAL
# ============================================================

st.markdown(
    '<div class="section-title">📈 Evolución de Ventas Mensuales</div>',
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
    labels={
        "Mes": "Mes",
        "Venta_Total_Soles": "Ventas (S/)"
    }
)

fig_mes.update_layout(
    template="plotly_white",
    margin=dict(
        l=20,
        r=20,
        t=20,
        b=20
    ),
    height=400
)

st.plotly_chart(
    fig_mes,
    use_container_width=True
)

# ============================================================
# CATEGORÍA Y CIUDAD
# ============================================================

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        '<div class="section-title">🏷️ Ventas por Categoría</div>',
        unsafe_allow_html=True
    )

    ventas_categoria = (
        df_filtrado
        .groupby(
            "Categoria",
            as_index=False
        )["Venta_Total_Soles"]
        .sum()
        .sort_values(
            "Venta_Total_Soles",
            ascending=False
        )
    )

    fig_categoria = px.bar(
        ventas_categoria,
        x="Categoria",
        y="Venta_Total_Soles",
        labels={
            "Categoria": "Categoría",
            "Venta_Total_Soles": "Ventas (S/)"
        },
        text_auto=".2s"
    )

    fig_categoria.update_layout(
        template="plotly_white",
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),
        height=380
    )

    st.plotly_chart(
        fig_categoria,
        use_container_width=True
    )

with col2:

    st.markdown(
        '<div class="section-title">🏙️ Ventas por Ciudad</div>',
        unsafe_allow_html=True
    )

    ventas_ciudad = (
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
        ventas_ciudad,
        x="Ciudad",
        y="Venta_Total_Soles",
        labels={
            "Ciudad": "Ciudad",
            "Venta_Total_Soles": "Ventas (S/)"
        },
        text_auto=".2s"
    )

    fig_ciudad.update_layout(
        template="plotly_white",
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),
        height=380
    )

    st.plotly_chart(
        fig_ciudad,
        use_container_width=True
    )

# ============================================================
# VENDEDORES Y MEDIOS DE PAGO
# ============================================================

col3, col4 = st.columns(2)

with col3:

    st.markdown(
        '<div class="section-title">🏆 Ranking de Vendedores</div>',
        unsafe_allow_html=True
    )

    ranking_vendedores = (
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

    fig_vendedores = px.bar(
        ranking_vendedores,
        x="Venta_Total_Soles",
        y="Vendedor",
        orientation="h",
        labels={
            "Vendedor": "Vendedor",
            "Venta_Total_Soles": "Ventas (S/)"
        },
        text_auto=".2s"
    )

    fig_vendedores.update_layout(
        template="plotly_white",
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),
        height=420,
        yaxis=dict(
            categoryorder="total ascending"
        )
    )

    st.plotly_chart(
        fig_vendedores,
        use_container_width=True
    )

with col4:

    st.markdown(
        '<div class="section-title">💳 Ventas por Medio de Pago</div>',
        unsafe_allow_html=True
    )

    ventas_pago = (
        df_filtrado
        .groupby(
            "Medio_Pago",
            as_index=False
        )["Venta_Total_Soles"]
        .sum()
    )

    fig_pago = px.pie(
        ventas_pago,
        names="Medio_Pago",
        values="Venta_Total_Soles",
        hole=0.45
    )

    fig_pago.update_layout(
        template="plotly_white",
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),
        height=420
    )

    st.plotly_chart(
        fig_pago,
        use_container_width=True
    )

# ============================================================
# DETALLE DE VENTAS
# ============================================================

st.markdown(
    '<div class="section-title">📋 Detalle de Ventas</div>',
    unsafe_allow_html=True
)

columnas_detalle = [
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

df_detalle = df_filtrado[
    columnas_detalle
].copy()

st.dataframe(
    df_detalle,
    use_container_width=True,
    hide_index=True
)

# ============================================================
# DESCARGA
# ============================================================

csv = df_detalle.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Descargar ventas filtradas",
    data=csv,
    file_name="ventas_filtradas.csv",
    mime="text/csv"
)

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div style="
    text-align:center;
    color:#6B7280;
    font-size:12px;
    margin-top:30px;
    padding-bottom:10px;
">
    Dashboard Ejecutivo de Ventas · Sales Intelligence · Perú 2026
</div>
""", unsafe_allow_html=True)
