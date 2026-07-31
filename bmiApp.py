import streamlit as st

st.markdown("# :red[แอปพลิเคชั่นคำนวณ BMI]")
st.write("กรอกข้อมูลน้ำหนักส่วนสูงของคุณ เพื่อคำนวณ BMI")

weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):")
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซ็นติเมตร):")

if st.button("คำนวณค่า BMI"):
   # แปลงส่วนสูงจาก cm เป็น เมตร แล้วคำนวณ BMI
   height_m = height_cm / 100
   bmi = weight / (height_m ** 2)

   st.write("___")
   st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

 if bmi < 18.5:
        st.warning("⚠️ คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
    elif 18.5 <= bmi < 23.0:
        st.success("🎉 คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
    elif 23.0 <= bmi < 25.0:
        st.info("💡 คุณมีน้ำหนักเกินเกณฑ์ (ท้วม)")
    else:
        st.error("🚨 คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย")

st.divider()
st.write("นายณัฐภัทร สาภู เลขที่ 25 ม.4/6")
