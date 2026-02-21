#стартовая страница

import streamlit as st  
import pandas as pd  

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

