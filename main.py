# https://streamlit.io/
# streamlit run D:\streamlit_app\main.py [ARGUMENTS]

"""
Пример приложения streamlit
"""

import streamlit as st
import time

if "uploaded_photo" not in st.session_state:
    st.session_state["uploaded_photo"] = "not done"

if "camera_photo" not in st.session_state:
    st.session_state["camera_photo"] = "not done"

col1, col2, col3 = st.columns([3, 1, 3])

col1.markdown(" ##### Вы на страничке проекта streamlit!")
col1.markdown("------")
col1.markdown(
    " ###### Данная страница является примером использования некоторых возможностей приложения для обработки данных и обмена.")
col1.markdown("------")
col1.markdown("Можно выделить следующие полезные особенности: ")
col1.markdown("* Размещение данных в столбцах")
col1.markdown("* Поддержка Marcdown")
col1.markdown("* Возможность загрузки файлов")
col1.markdown("* Получение фото с веб-камеры")
col1.markdown("* Обратная связь")
col1.markdown("* Отображение работы в фоновом режиме")
col1.markdown("* Показ метрик")
col1.markdown("* Расширитель текста")
col1.markdown("* Добавление в выпадающий список изображений")

col2.metric(label="Температура:", value="25 °C", delta="3 °C")


def upload_photo_state():
    st.session_state["uploaded_photo"] = "done"


def camera_photo_state():
    st.session_state["camera_photo"] = "done"


col3.markdown("------")
uploaded_photo = col3.file_uploader("Загрузить фото", on_change=upload_photo_state)

if st.session_state["uploaded_photo"] == "done":

    progress_bar = col3.progress(0)

    for perc_completed in range(100):
        time.sleep(0.005)
        progress_bar.progress(perc_completed + 1)

    col3.success("Фото загружено!")

col3.markdown("------")
camera_photo = col3.camera_input("Сделать фото", on_change=camera_photo_state)

if st.session_state["camera_photo"] == "done":

    progress_bar = col3.progress(0)

    for perc_completed in range(100):
        time.sleep(0.005)
        progress_bar.progress(perc_completed + 1)

    col3.success("Фото сделано!")

with st.expander("Кликните чтобы узнать больше..."):
    st.write("Привет, здесь может быть отражена дополнительная информация о приложении.")

    if uploaded_photo:
        st.image(uploaded_photo)
    if camera_photo:
        st.image(camera_photo)
    else:
        st.write("... Ни одного фото пока не загружено ...")
