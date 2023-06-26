from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np



model = pickle.load(open('Random_Forest.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    bedrooms=int(request.form.get('Bedrooms'))
    bathrooms=int(request.form.get('Bathrooms'))
    sqft_living=int(request.form.get('Living'))
    sqft_lot=int(request.form.get('Lot'))
    floors=int(request.form.get('Floors'))
    waterfront=int(request.form.get('Waterfront'))
    view=int(request.form.get('View'))
    condition=int(request.form.get('Condition'))
    sqft_above=int(request.form.get('Above'))
    sqft_basement=int(request.form.get('Basement'))
    yr_built=int(request.form.get('Built Year'))
    yr_renovated=int(request.form.get('Renovation year'))
    street=int(request.form.get('Street'))
    city=int(request.form.get('City'))
    statezip=int(request.form.get('State Zip'))
    country=int(request.form.get('Country'))


    results = model.predict(np.array([bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, sqft_above, sqft_basement, yr_built, yr_renovated,street, city, statezip, country]).reshape(1,16))
    return render_template('index.html',result= results)

if __name__== '__main__':
    app.run(debug=True)

    
   