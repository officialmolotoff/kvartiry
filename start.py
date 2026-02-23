#стартовая страница

import streamlit as st  
import pandas as pd
import requests #библиотека для работы с HTTP-запросами
import streamlit.components.v1 as components

YANDEX_API_KEY = "65b4de15-5d42-4294-a619-5423375fa8a9"  

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

           """Генерирует HTML/JS компонент с Яндекс.Картой"""
           html_code = f"""
             <div id="map" style="width: 100%; height: 400px; border-radius: 10px;"></div>
             <script src="https://api-maps.yandex.ru/2.1/?apikey={YANDEX_API_KEY}&lang=ru_RU" type="text/javascript"></script>
             <script type="text/javascript">
            ymaps.ready(init);
            function init() {{
                var myMap = new ymaps.Map("map", {{
                    center: [{building_details['Широта']}, {building_details['Долгота']}],
                    zoom: 16
                }});
                var myPlacemark = new ymaps.Placemark([{building_details['Широта']}, {building_details['Долгота']}], {{
                    balloonContent: '{df['FullAddress']}'
                }});
                myMap.geoObjects.add(myPlacemark);
            }}
                </script>
               """
           components.html(html_code, height=410)
           
           st.write(f"**Год постройки:** {building_details['Год_постройки']}")
           st.write(f"**Этажность:** {building_details['Этажность']}")
           # Проверка на возможное пустое значение для Потолка
           if pd.notna(building_details['Потолок']):
             st.write(f"**Высота потолков:** {building_details['Потолок']} м")
           else:
             st.write("**Высота потолков:** неизвестно")
           st.write(f"**Расстояние до центра:** {building_details['Расстояние_до_центра']} км")
            

           
