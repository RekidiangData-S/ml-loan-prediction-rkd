import streamlit as st
from PIL import Image


def about():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:green;padding:7px"> 
    <h1 style ="color:black;text-align:center;">Iris Flower species Classification</h1> 
    </div> 

    #  Problem Definition

    > Automate the classification of iris flower species as [virginica, setosa or versicolor] based on sepal length, sepal width
     petal length, petal width provided by online user.

    # INSPIRATION
    + https://www.analyticsvidhya.com/blog/2020/12/deploying-machine-learning-models-using-streamlit-an-introductory-guide-to-model-deployment/#:~:text=Streamlit%20is%20a%20popular%20open-source%20framework%20used%20for,prediction%20model%20and%20then%20deploy%20it%20using%20Streamlit.
    + https://machinelearningmastery.com/how-to-define-your-machine-learning-problem/

    ---
    
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    image = Image.open('accessoirs/my_ethiquette.png')
    st.image(image, use_column_width=True)
