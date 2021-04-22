import streamlit as st
import pickle
# %% writefile app.py


# defining the function which will make the prediction using the data which the user inputs
def prediction():

    #st.title("Iris Flower species Classification")

    # loading the trained model
    pickle_in = open('models/DTree98.88.pkl', 'rb')
    model = pickle.load(pickle_in)


# this is the main function in which we define our webpage

    # front end elements of the web page
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Iris Flower species Classification</h1>
    </div>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    l = []
    sl = st.number_input('Enter sepal length : ')
    l.append(sl)
    sw = st.number_input('Enter sepal width  : ')
    l.append(sw)
    pl = st.number_input('Enter petal length : ')
    l.append(pl)
    pw = st.number_input('Enter petal width  : ')
    l.append(pw)

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        pred_result = model.predict([l])
        st.success(f'Iris Classified as : {pred_result[0]}')
