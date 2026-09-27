import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Sales Intelligence | Dashboard Ejecutivo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# ESTILOS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #F4F7FB;
}

/* CONTENEDOR */
.block-container {
    max-width: 1500px;
    padding: 1.4rem 2rem 2rem 2rem;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0F172A 0%,
        #1E293B 100%
    );

    min-width: 285px;
}

section[data-testid="stSidebar"] * {
    color: #F8FAFC !important;
}

.sidebar-title {
    font-size: 23px;
    font-weight: 800;
    color: white !important;
    margin-bottom: 3px;
}

.sidebar-subtitle {
    font-size: 12px;
    color: #CBD5E1 !important;
    margin-bottom: 20px;
}

.filter-title {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    color: #94A3B8 !important;
    margin-top: 10px;
    margin-bottom: 10px;
}


/* ============================================================
   HEADER
   ============================================================ */

.dashboard-header {
    background: linear-gradient(
        135deg,
        #0F172A 0%,
        #1D4ED8 100%
    );

    padding: 28px 32px;
    border-radius: 18px;
    color: white;
    margin-bottom: 22px;

    box-shadow:
        0 8px 25px rgba(15, 23, 42, 0.14);
}

.dashboard-header h1 {
    margin: 0;
    font-size: 31px;
    font-weight: 800;
    letter-spacing: -0.5px;
}

.dashboard-header p {
    margin: 8px 0 0 0;
    font-size: 14px;
    opacity: 0.90;
}


/* ============================================================
   KPI
   ============================================================ */

.kpi-box {
    background: white;

    border-radius: 16px;

    padding: 18px 20px;

    min-height: 145px;

    border: 1px solid #E2E8F0;

    box-shadow:
        0 4px 15px rgba(15, 23, 42, 0.06);

    transition: all 0.2s ease;
}

.kpi-box:hover {
    transform: translateY(-3px);

    box-shadow:
        0 10px 25px rgba(15, 23, 42, 0.10);
}

.kpi-icon {
    font-size: 27px;
    margin-bottom: 8px;
}

.kpi-label {
    color: #64748B;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 6px;
}

.kpi-number {
    color: #0F172A;
    font-size: 24px;
    font-weight: 800;
}

.kpi-description {
    color: #94A3B8;
    font-size: 11px;
    margin-top: 6px;
}


/* ============================================================
   FILTROS ACTIVOS
   ============================================================ */

.filter-status {
    background: #EFF6FF;

    border: 1px solid #BFDBFE;

    color: #1D4ED8;

    padding: 9px 13px;

    border-radius: 9px;

    font-size: 12px;

    font-weight: 600;

    margin-bottom: 16px;
}


/* ============================================================
   TÍTULOS
   ============================================================ */

.section-title {
    color: #0F172A;

    font-size: 19px;

    font-weight: 800;

    margin-top: 25px;

    margin-bottom: 10px;
}


/* ============================================================
   BOTÓN DESCARGA
   ============================================================ */

div[data-testid="stDownloadButton"] button {

    width: 100%;

    min-height: 45px;

    border-radius: 10px;

    font-weight: 700;
}


/* ============================================================
   TABLA
   ============================================================ */

[data-testid="stDataFrame"] {
    width: 100%;
}


/* ============================================================
   GRÁFICOS
   ============================================================ */

.stPlotlyChart {
    width: 100% !important;
}


/* ============================================================
   TABLET
   ============================================================ */

@media (max-width: 992px) {

    .block-container {
        padding: 1rem;
    }

    .dashboard-header {
        padding: 22px 20px;
    }

    .dashboard-header h1 {
        font-size: 26px;
    }

    .kpi-number {
        font-size: 21px;
    }

    section[data-testid="stSidebar"] {
        min-width: 280px;
        max-width: 85vw;
    }
}


/* ============================================================
   CELULAR
   ============================================================ */

@media (max-width: 768px) {

    .block-container {
        padding: 0.7rem 0.6rem 1.5rem 0.6rem;
    }

    .dashboard-header {
        padding: 18px 16px;
        border-radius: 13px;
    }

    .dashboard-header h1 {
        font-size: 20px;
        line-height: 1.25;
    }

    .dashboard-header p {
        font-size: 11px;
    }

    .kpi-box {
        padding: 12px;
        min-height: 112px;
    }

    .kpi-icon {
        font-size: 21px;
    }

    .kpi-label {
        font-size: 10px;
    }

    .kpi-number {
        font-size: 17px;
    }

    .kpi-description {
        font-size: 9px;
    }

    .section-title {
        font-size: 16px;
    }

    section[data-testid="stSidebar"] {
        min-width: 280px;
        max-width: 88vw;
    }
}


/* ============================================================
   CELULAR PEQUEÑO
   ============================================================ */

@media (max-width: 480px) {

    .dashboard-header h1 {
        font-size: 18px;
    }

    .dashboard-header p {
        font-size: 10px;
    }

    .kpi-box {
        padding: 10px;
        min-height: 105px;
    }

    .kpi-icon {
        font-size: 19px;
    }

    .kpi-number {
        font-size: 15px;
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
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-title">
            📊 Sales Intelligence
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sidebar-subtitle">
            Dashboard Ejecutivo de Ventas
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="filter-title">
            🔎 FILTROS DE ANÁLISIS
        </div>
        """,
        unsafe_allow_html=True
    )

    # CIUDAD
    ciudades = st.multiselect(
        "Ciudad",
        sorted(
            df["Ciudad"]
            .dropna()
            .unique()
        ),
        default=sorted(
            df["Ciudad"]
            .dropna()
            .unique()
        )
    )

    # CATEGORÍA
    categorias = st.multiselect(
        "Categoría",
        sorted(
            df["Categoria"]
            .dropna()
            .unique()
        ),
        default=sorted(
            df["Categoria"]
            .dropna()
            .unique()
        )
    )

    # VENDEDORES
    vendedores = st.multiselect(
        "Vendedor",
        sorted(
            df["Vendedor"]
            .dropna()
            .unique()
        ),
        default=sorted(
            df["Vendedor"]
            .dropna()
            .unique()
        )
    )

    # MEDIO DE PAGO
    medios = st.multiselect(
        "Medio de pago",
        sorted(
            df["Medio_Pago"]
            .dropna()
            .unique()
        ),
        default=sorted(
            df["Medio_Pago"]
            .dropna()
            .unique()
        )
    )

    st.markdown("---")

    st.caption(
        "Periodo: Enero - Septiembre 2026"
    )


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

st.markdown(
    """
    <div class="dashboard-header">

        <h1>
            📊 Dashboard Ejecutivo de Ventas
        </h1>

        <p>
            Sales Intelligence · Análisis Comercial · Perú · 2026
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FILTROS ACTIVOS
# ============================================================

filtros_activos = (
    len(ciudades)
    +
    len(categorias)
    +
    len(vendedores)
    +
    len(medios)
)

st.markdown(
    f"""
    <div class="filter-status">

        🔎 Filtros activos ·
        {filtros_activos} selecciones ·
        {len(df_filtrado):,} registros analizados

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# CÁLCULO DE KPIs
# ============================================================

ventas_totales = df_filtrado[
    "Venta_Total_Soles"
].sum()

transacciones = len(
    df_filtrado
)

unidades = df_filtrado[
    "Cantidad"
].sum()

if transacciones > 0:

    ticket_promedio = (
        ventas_totales /
        transacciones
    )

else:

    ticket_promedio = 0


# ============================================================
# KPIs
# ============================================================

kpi1, kpi2, kpi3, kpi4 = st.columns(4)


# ============================================================
# KPI 1 - VENTAS TOTALES
# ============================================================

with kpi1:

    st.markdown(
        f"""
        <div class="kpi-box">

            <div class="kpi-icon">
                💰
            </div>

            <div class="kpi-label">
                VENTAS TOTALES
            </div>

            <div class="kpi-number">
                S/ {ventas_totales:,.2f}
            </div>

            <div class="kpi-description">
                Facturación acumulada
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# KPI 2 - TRANSACCIONES
# ============================================================

with kpi2:

    st.markdown(
        f"""
        <div class="kpi-box">

            <div class="kpi-icon">
                🧾
            </div>

            <div class="kpi-label">
                TRANSACCIONES
            </div>

            <div class="kpi-number">
                {transacciones:,}
            </div>

            <div class="kpi-description">
                Operaciones registradas
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# KPI 3 - UNIDADES
# ============================================================

with kpi3:

    st.markdown(
        f"""
        <div class="kpi-box">

            <div class="kpi-icon">
                📦
            </div>

            <div class="kpi-label">
                UNIDADES VENDIDAS
            </div>

            <div class="kpi-number">
                {unidades:,}
            </div>

            <div class="kpi-description">
                Productos vendidos
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# KPI 4 - TICKET PROMEDIO
# ============================================================

with kpi4:

    st.markdown(
        f"""
        <div class="kpi-box">

            <div class="kpi-icon">
                🎫
            </div>

            <div class="kpi-label">
                TICKET PROMEDIO
            </div>

            <div class="kpi-number">
                S/ {ticket_promedio:,.2f}
            </div>

            <div class="kpi-description">
                Venta promedio por operación
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# EVOLUCIÓN MENSUAL
# ============================================================

st.markdown(
    """
    <div class="section-title">
        📈 Evolución de Ventas Mensuales
    </div>
    """,
    unsafe_allow_html=True
)


ventas_mes = (
    df_filtrado
    .groupby(
        ["Mes_Numero", "Mes"],
        as_index=False
    )["Venta_Total_Soles"]
    .sum()
    .sort_values(
        "Mes_Numero"
    )
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


fig_mes.update_traces(
    hovertemplate=
    "<b>%{x}</b><br>"
    "Ventas: S/ %{y:,.2f}"
    "<extra></extra>"
)


fig_mes.update_layout(
    template="plotly_white",
    margin=dict(
        l=15,
        r=15,
        t=15,
        b=15
    ),
    height=390,
    hovermode="x unified"
)


st.plotly_chart(
    fig_mes,
    use_container_width=True
)


# ============================================================
# VENTAS POR CATEGORÍA / CIUDAD
# ============================================================

col1, col2 = st.columns(2)


# ============================================================
# CATEGORÍA
# ============================================================

with col1:

    st.markdown(
        """
        <div class="section-title">
            🏷️ Ventas por Categoría
        </div>
        """,
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

    fig_categoria.update_traces(
        hovertemplate=
        "<b>%{x}</b><br>"
        "Ventas: S/ %{y:,.2f}"
        "<extra></extra>"
    )

    fig_categoria.update_layout(
        template="plotly_white",
        margin=dict(
            l=15,
            r=15,
            t=15,
            b=15
        ),
        height=380
    )

    st.plotly_chart(
        fig_categoria,
        use_container_width=True
    )


# ============================================================
# CIUDAD
# ============================================================

with col2:

    st.markdown(
        """
        <div class="section-title">
            🏙️ Ventas por Ciudad
        </div>
        """,
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

    fig_ciudad.update_traces(
        hovertemplate=
        "<b>%{x}</b><br>"
        "Ventas: S/ %{y:,.2f}"
        "<extra></extra>"
    )

    fig_ciudad.update_layout(
        template="plotly_white",
        margin=dict(
            l=15,
            r=15,
            t=15,
            b=15
        ),
        height=380
    )

    st.plotly_chart(
        fig_ciudad,
        use_container_width=True
    )


# ============================================================
# VENDEDORES / MEDIO DE PAGO
# ============================================================

col3, col4 = st.columns(2)


# ============================================================
# RANKING VENDEDORES
# ============================================================

with col3:

    st.markdown(
        """
        <div class="section-title">
            🏆 Ranking de Vendedores
        </div>
        """,
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

    fig_vendedores.update_traces(
        hovertemplate=
        "<b>%{y}</b><br>"
        "Ventas: S/ %{x:,.2f}"
        "<extra></extra>"
    )

    fig_vendedores.update_layout(
        template="plotly_white",
        margin=dict(
            l=15,
            r=15,
            t=15,
            b=15
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


# ============================================================
# MEDIO DE PAGO
# ============================================================

with col4:

    st.markdown(
        """
        <div class="section-title">
            💳 Ventas por Medio de Pago
        </div>
        """,
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
        hole=0.48
    )

    fig_pago.update_traces(
        textposition="inside",
        textinfo="percent",

        hovertemplate=
        "<b>%{label}</b><br>"
        "Ventas: S/ %{value:,.2f}<br>"
        "%{percent}"
        "<extra></extra>"
    )

    fig_pago.update_layout(
        template="plotly_white",
        margin=dict(
            l=15,
            r=15,
            t=15,
            b=15
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
    """
    <div class="section-title">
        📋 Detalle de Ventas
    </div>
    """,
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
# DESCARGAR CSV
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

st.markdown(
    """
    <div style="
        text-align:center;
        color:#64748B;
        font-size:11px;
        margin-top:32px;
        padding:15px 0 8px 0;
    ">
        Sales Intelligence · Dashboard Ejecutivo de Ventas · Perú 2026
    </div>
    """,
    unsafe_allow_html=True
)
