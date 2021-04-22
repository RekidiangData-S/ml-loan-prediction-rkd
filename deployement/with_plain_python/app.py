###--PREDICTION--################################################################
import pickle

def main():
    '''
        Accept features values from the user and classify on base of those features 
        if the iris flower spece (setosa, virginica, versicolor) 
    '''
    print("============WELCOME TO=============")
    print("    Iris Flower Classification     ")
    print("===================================")
    print(" ")
    # Load Model
    model = pickle.load(open('models/DTree98.88.pkl', "rb"))
    
    print("Please Enter Predictor variables")
    print("--------------------------------")
    l=[]
    l.append(float(input('Enter sepal length : ')))
    l.append(float(input('Enter sepal width  : ')))
    l.append(float(input('Enter petal length : ')))
    l.append(float(input('Enter petal width  : ')))
    print("--------------------------------")
    print("")      
    #arr = pd.DataFrame([l])
    #arr = np.asarray([l])
         
    pred_result = model.predict([l])
    print("===================================")
    print(f'Iris Classified as : {pred_result[0]}')
    print("============THANK YOU=============")
    
if __name__ == "__main__":
    main()
    
    
    
    