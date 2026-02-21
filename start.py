#стартовая страница

import streamlit as st  
import pandas as pd

#@st.cache_data #функция кэширует данные из Excel (файл не будет перечитываться при каждом нажатии кнопки, что делает поиск мгновенным)

st.title("Квартиры")

st.write("Данный сайт представляет собой прогноз стоимости квартиры по введённым параметрам.")

number_of_rooms = st.number_input("Количество комнат:",
                    min_value = 1,
                    value = 1,
                    step = 1)

floor = st.number_input("Этаж:",
                    min_value = 1,
                    value = 1,
                    step = 1)

total_area = st.number_input("Общая площадь (в кв. м.):",
                              min_value = 0.01,
                              value = 0.01,
                              step = 0.01)

# и т. д. (площадь кухни, тип комнат, ...) 

# данные из Excel
df = pd.read_excel(kvartiry/houses.xlsx)
# полный адрес для удобства поиска
df['FullAddress'] = df['Тип улицы'].astype(str) + " " + df['Адрес'].astype(str)
address_list = df['FullAddress'].tolist()
# Поисковое поле с предложениями
# index=None делает поле изначально пустым
selected_address = st.selectbox(
            "Начните вводить адрес:",
            options = address_list,
            index = None,
            placeholder = "Например: ул. Омская, д. 21",
        )
# Вывод результата
if selected_address:
  st.success(f"Вы выбрали: **{selected_address}**")
