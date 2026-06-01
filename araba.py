import streamlit as st
import numpy as np
import joblib

# Modeli Yükle
model = joblib.load("car_price_model.pkl")

st.title("🚗 Araç Fiyatı Tahmin Sistemi")
st.write("Aracın teknik özelliklerini girerek tahmini piyasa değerini hesaplayın.")

# Kullanıcı Giriş Alanları (Modeldeki sıraya göre)
wheelbase = st.number_input("Tekerlek Mesihi (Wheelbase)", min_value=80.0, max_value=130.0, value=98.0)
carlength = st.number_input("Araç Uzunluğu (Length)", min_value=140.0, max_value=220.0, value=174.0)
carwidth = st.number_input("Araç Genişliği (Width)", min_value=60.0, max_value=80.0, value=65.0)
curbweight = st.number_input("Boş Ağırlık (Curb Weight - lbs)", min_value=1500, max_value=5000, value=2500)
enginesize = st.number_input("Motor Hacmi (Engine Size)", min_value=50, max_value=400, value=120)
horsepower = st.number_input("Beygir Gücü (Horsepower)", min_value=40, max_value=300, value=100)
citympg = st.number_input("Şehir İçi Yakıt Tüketimi (City MPG)", min_value=10, max_value=60, value=25)
highwaympg = st.number_input("Şehir Dışı Yakıt Tüketimi (Highway MPG)", min_value=10, max_value=60, value=30)

# Tahmin Butonu
if st.button("Fiyatı Tahmin Et"):
    # Girdileri modelin beklediği formata getir
    input_data = np.array([[wheelbase, carlength, carwidth, curbweight, 
                            enginesize, horsepower, citympg, highwaympg]])
    
    # Tahmin gerçekleştir
    prediction = model.predict(input_data)[0]
    
    # Sonucu ekrana yazdır
    st.success(f"💰 Tahmini Araç Fiyatı: **${prediction:,.2f}**")

