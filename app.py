import pickle
import streamlit as st
import pandas as pd

st.title('Food Recommender System')

food_list = pickle.load(open('food_list.pkl','rb'))
data = pd.DataFrame(food_list)

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(food):
    food_index = data[data["Food_Name"] == food].index[0]
    distances = similarity[food_index]
    food_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:11]

    recommended_foods= []
    for i in food_list:
        recommended_foods.append(data.iloc[i[0]].Food_Name)
    return recommended_foods

selected_food = st.selectbox('What would you like to have?', food_list)
if st.button('Recommend'):
    recommendations = recommend(selected_food)
    st.subheader("You should also try this")
    for i in recommendations:
        st.write(i)

st.snow()