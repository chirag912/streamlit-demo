import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a dummy DataFrame with random data
data = {
    'City': ['City A', 'City B', 'City C', 'City D'],
    'SO': np.random.randint(0, 100, 4),
    'NO': np.random.randint(0, 100, 4),
    'CO': np.random.randint(0, 100, 4),
    'PM2.5': np.random.randint(0, 100, 4),
    'PM10': np.random.randint(0, 100, 4),
}
df = pd.DataFrame(data)

st.title('Air Quality Visualization App')

# Sidebar with user inputs
selected_city = st.sidebar.selectbox('Select a City:', df['City'])
st.sidebar.markdown('---')
st.sidebar.write('User Inputs:')
so_input = st.sidebar.slider('SO', min_value=0, max_value=100, value=50)
no_input = st.sidebar.slider('NO', min_value=0, max_value=100, value=50)
co_input = st.sidebar.slider('CO', min_value=0, max_value=100, value=50)
pm25_input = st.sidebar.slider('PM2.5', min_value=0, max_value=100, value=50)
pm10_input = st.sidebar.slider('PM10', min_value=0, max_value=100, value=50)

# Filter the DataFrame based on the selected city
filtered_df = df[df['City'] == selected_city]

# Display the filtered data
st.write(f"Data for {selected_city}:")
st.write(filtered_df)

# Create a bar chart for the selected city
fig, ax = plt.subplots(figsize=(10, 6))
params = ['SO', 'NO', 'CO', 'PM2.5', 'PM10']
values = [so_input, no_input, co_input, pm25_input, pm10_input]
ax.bar(params, values, color='b', alpha=0.7)
ax.set_title(f'{selected_city} Air Quality Parameters')
ax.set_ylabel('Values')
st.pyplot(fig)
