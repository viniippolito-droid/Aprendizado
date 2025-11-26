import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Cálculo de Viga Biapoiada com Carga no Meio")

L = st.number_input("Comprimento L (m)", min_value=0.1, value=5.0)
P = st.number_input("Carga P (kN)", min_value=0.1, value=10.0)

R1 = P / 2
R2 = P / 2
Mmax = P * L / 4
Vmax = P / 2

st.subheader("Resultados")
st.write(f"Reação no apoio esquerdo: {R1:.2f} kN")
st.write(f"Reação no apoio direito: {R2:.2f} kN")
st.write(f"Momento máximo: {Mmax:.2f} kN.m")
st.write(f"Esforço cortante máximo: {Vmax:.2f} kN")

x = np.linspace(0, L, 200)
V = np.where(x <= L/2, P/2, -P/2)
M = np.where(x <= L/2, (P/2)*x, (P/2)*(L - x))

st.subheader("Diagrama de Cortante (V)")
fig1, ax1 = plt.subplots()
ax1.plot(x, V)
ax1.set_xlabel("x (m)")
ax1.set_ylabel("V (kN)")
ax1.grid(True)
st.pyplot(fig1)

st.subheader("Diagrama de Momento (M)")
fig2, ax2 = plt.subplots()
ax2.plot(x, M)
ax2.set_xlabel("x (m)")
ax2.set_ylabel("M (kN.m)")
ax2.grid(True)
st.pyplot(fig2)
