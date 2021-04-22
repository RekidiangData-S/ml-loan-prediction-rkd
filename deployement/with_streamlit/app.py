import pickle
import streamlit as st
from PIL import Image
from prediction import prediction
from analysis import analysis
from about import about


image = Image.open('accessoirs/data_logo_resized.png')
st.image(image, use_column_width=True)
############# set subtitle ############


#st.title("Iris Flower species Classification")


def main():
    activities = ['Prediction', 'About The Project', 'Data Analysis']
    option = st.sidebar.selectbox('Selection Option', activities)
    if option == 'Prediction':
        prediction()
    if option == 'Data Analysis':
        analysis()

    if option == 'About The Project':
        about()


if __name__ == "__main__":
    main()

############# Load dataset ############
