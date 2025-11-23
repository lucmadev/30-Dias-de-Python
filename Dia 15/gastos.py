import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Previamente: pip install streamlit pandas matplotlib

# --- Configuración inicial ---
st.set_page_config(page_title="Dashboard de Gastos", layout="wide")

st.title(" Dashboard de Gastos")
st.write("Agregá tus gastos y visualizá tus finanzas en tiempo real.")

# --- Cargar / Inicializar datos ---
if "gastos" not in st.session_state:
    st.session_state.gastos = pd.DataFrame(columns=["Categoría", "Monto"])

# --- Formulario para agregar gastos ---
with st.form("form_gasto"):
    categoria = st.selectbox("Categoría", ["Comida", "Transporte", "Entretenimiento", "Otros"])
    monto = st.number_input("Monto ($)", min_value=1.0, step=1.0)
    enviar = st.form_submit_button("Agregar")

    if enviar:
        nuevo = {"Categoría": categoria, "Monto": monto}
        st.session_state.gastos = pd.concat(
            [st.session_state.gastos, pd.DataFrame([nuevo])],
            ignore_index=True
        )
        st.success(f"Gasto agregado: {categoria} - ${monto}")

# --- Mostrar tabla ---
st.subheader(" Lista de gastos")
st.dataframe(st.session_state.gastos, width='stretch')

# --- Gráficos ---
if not st.session_state.gastos.empty:
    st.subheader(" Visualización de gastos")

    # Gastos por categoría
    gastos_cat = st.session_state.gastos.groupby("Categoría")["Monto"].sum()

    col1, col2 = st.columns(2)

    with col1:
        st.bar_chart(gastos_cat)

    with col2:
        fig, ax = plt.subplots()
        ax.pie(gastos_cat, labels=gastos_cat.index, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

# --- Total ---
st.subheader(" Total gastado")
st.metric("Total", f"${st.session_state.gastos['Monto'].sum():,.2f}")
