# 1. Library imports
import uvicorn
from fastapi import FastAPI
from clickAds import ClickAd
import pickle

# 2. Create the app object
app = FastAPI()
pickle_in = open("ANN_Model.pkl", "rb")
classifier = pickle.load(pickle_in)


# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, All'}


#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Hello': f'{name}'}


# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_click(data: ClickAd):
    data = data.dict()
    timespent = data['TimeSpent']
    age = data['Age']
    areaincome = data['AreaIncome']
    internetusage = data['InternetUsage']
    male = data['Male']
    # print(classifier.predict([[timespent, age, areaincome, internetusage, male]]]))
    prediction = classifier.predict([[timespent, age, areaincome, internetusage, male]])
    if prediction[0] > 0.5:
        prediction = "Ad Not Clicked"
    else:
        prediction = "Ad Clicked"
    return {
        'prediction': prediction
    }


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
