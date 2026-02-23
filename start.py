#стартовая страница

import streamlit as st  
import pandas as pd

st.set_page_config(page_title = "Прогнозирование стоимости квартиры", layout = "centered")

st.info("Данный сайт представляет собой прогноз стоимости квартиры по введённым параметрам. \
         Разработан студентами 147 группы мех-мата СГУ Володиным Максимом Сергеевичем и Трибис Инной Александровной.")

with st.expander("Информация о квартире", expanded = True): # expanded=True означает, что по умолчанию вкладка открыта
  number_of_rooms = st.number_input("Укажите количество комнат:",
                    min_value = 1,
                    step = 1)

  floor = st.number_input("Укажите этаж:",
                    min_value = 1,
                    step = 1)

  total_area = st.number_input("Укажите общую площадь (в кв. м.):",
                              min_value = 0.01,
                              step = 0.01)

# и т. д. (площадь кухни, тип комнат, ...) 

#@st.cache_data #функция кэширует данные из Excel (файл не будет перечитываться при каждом нажатии кнопки, что делает поиск мгновенным)
# данные о домах из Excel
df = pd.read_excel("houses.xlsx")
# полный адрес (тип улицы + адрес) для удобства поиска
df['FullAddress'] = df['Тип улицы'].astype(str) + " " + df['Адрес'].astype(str)
address_list = df['FullAddress'].tolist()
with st.expander("Информация о доме", expanded = True): # expanded=False означает, что по умолчанию вкладка закрыта
  # Поисковое поле с предложениями
  # index=None делает поле изначально пустым
  selected_address = st.selectbox(
            "Начните вводить адрес и номер дома:",
            options = address_list,
            index = None,
            placeholder = "Например: улица омская, 21",
          )
  if selected_address:
           # Получаем строку с данными для выбранного адреса
           # .iloc[0] берет первую (и единственную) найденную строку
           building_details = df[df['FullAddress'] == selected_address].iloc[0]
           st.write(f"**Год постройки:** {building_details['Год_постройки']}")
           st.write(f"**Этажность:** {building_details['Этажность']}")
           # Проверка на возможное пустое значение для Потолка
           if pd.notna(building_details['Потолок']):
             st.write(f"**Высота потолков:** {building_details['Потолок']} м")
           else:
             st.write("**Высота потолков:** неизвестно") 
            

           
