import streamlit as st

# CONFIGURAÇÕES DA PÁGINA
st.set_page_config(page_title="Cálculo Qualidade", page_icon="🌱", layout="centered")


# TÍTULO PRINCIPAL
st.markdown("<h2 style='text-align: center; color: #4CAF50;'>Cálculo de Qualidade Têxtil</h2>", unsafe_allow_html=True)
st.markdown("---")

# ENCOLHIMENTO
with st.container():
    st.subheader("🔻 Cálculo de Encolhimento")
    enc = st.number_input("Digite o valor de Encolhimento (%)", min_value=0.0, step=0.1)
    
    if st.button("Calcular Encolhimento"):
        resultado = (50 - enc) * 2
        st.success(f"✅ Resultado do encolhimento: {resultado:.2f}%")

# SEPARADOR
st.markdown("---")

# TORÇÃO
with st.container():
    st.subheader("🔄 Cálculo de Torção")
    tor = st.number_input("Digite o valor de Torção", min_value=0.0, step=0.1)
    
    if st.button("Calcular Torção"):
        resultado = 100 * tor / 50
        st.info(f"ℹ️ Resultado da torção: {resultado:.2f}%")

# RODAPÉ
st.markdown("---")
st.caption("Desenvolvido por Moisés • powered by Streamlit 🚀")
