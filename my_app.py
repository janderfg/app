# Imports
import streamlit as st
import seaborn as sns
import pandas as pd
# from PIL import Image
import numpy as np

# Write a page title
st.title('Hello World. This is a Title')

# Subheader
st.subheader('Aqui, a subtítulo')

# Text
st.text('Texto texto texto texto texto texto texto texto texto texto')

# Using st.write
st.write('This is can be used for text and other features.')

# Load Dataset
df = sns.load_dataset('tips')

# Page Title
st.title('Examples of what st.write() can do')

# Text + emoji
st.write('Hello :sunglasses: :heart: ')

# Calculations
st.write(1+1)

# Variables
a = 2**2
st.write(a)

# Table
st.write(df.head(2))

# Multiple
st.write('st.write("text", df)', df.head(3))


# Insert a picture
# First, read it with PIL
# image = Image.open('/home/jander/Dropbox/Linux - FCD/Streamlit_Logo.png')
# Load Image in the App
# st.image(image)


# Add Lat Long
latlong = {'NY': {'lat': 40.730610, 'lon': -73.935242},
           'London': {'lat': 51.509865,'lon': -0.118092},
           'Paris': {'lat': 48.864716, 'lon':2.349014},
           'Sao Paulo': {'lat': -23.533773,'lon': -46.625290},
           'Rome': {'lat': 41.902782,'lon': 12.496366}
           }

city = ['Paris', 'London', 'NY', 'Sao Paulo', 'Rome']
city_random = np.random.choice(city, 244)

# Add Cols
df['city'] = city_random
df['lat'] = [latlong[city]['lat'] for city in city_random]
df['lon'] = [latlong[city]['lon'] for city in city_random]

# Map
map_df = df[['lat', 'lon']]
st.map(map_df, zoom=1)

# Radio Button
st.radio('Choose your option', options=('Option 1', 'Option 2', 'Option 3'))

# Slider
st.slider('<-- Slide to the sides -->', min_value=0, max_value=10, value=5, step=1)

# Multiselect
st.text('Checkbox')
st.multiselect('What are your favorite colors',
            ['Green', 'Yellow', 'Red', 'Blue'],
            ['Blue', 'Green']) # Pre-selected

# Selectbox
st.selectbox('Select Box', options=('Option 1', 'Option 2', 'Option 3'))

# Text input
title = st.text_input('My App Text Input', 'Write Something...')
st.write('You wrote: ', title)

# Adding a text in the sidebar
st.sidebar.text('Your Text Here')

# Add a radio button
st.sidebar.radio('Escolha a opção desejada: ', options=['Opção 1', 'Opção 2'])

# The other gadgets follow the same syntax.
