from fastapi import FastAPI
import uvicorn
import pickle
from model import Human
model=pickle.load(open("model.pkl","rb"))
app=FastAPI()
@app.get("/{name}")
def greet(name:str):
    return {"Hello {} Welcome to Stroke Prediction API!!".format(name)}


@app.get("/")
def greetings():
    return {"Hello there Welcome to Stroke Prediction API"}


@app.post("/predict")
def predict(request:Human):
    age=request.age
    hypertension = request.hypertension
    heart_disease=request.heart_disease
    avg_glucose_level=request.avg_glucose_level
    bmi=request.bmi
    isMale=request.isMale
    isOther=request.isOther
    ever_married_Yes=request.ever_married_Yes
    work_type_Never_worked=request.work_type_Never_worked
    work_type_Private=request.work_type_Private
    work_type_Self_employed=request.work_type_Self_employed
    work_type_children=request.work_type_children
    Residence_type_Urban=request.Residence_type_Urban
    smoking_status_formerly_smoked=request.smoking_status_formerly_smoked
    smoking_status_never_smoked=request.smoking_status_never_smoked
    smoking_status_smokes=request.smoking_status_smokes
    dic=list([age,hypertension,heart_disease,avg_glucose_level,bmi,isMale,isOther,ever_married_Yes,work_type_Never_worked,work_type_Private,work_type_Self_employed,work_type_children,
    Residence_type_Urban,
    smoking_status_formerly_smoked,
    smoking_status_never_smoked,
    smoking_status_smokes
    ])
    predict=model.predict_proba([dic])
    return {"There are {} of getting Stroke.Stay Safe".format(predict[0][1]*100)}

if __name__=="__main__":
    uvicorn.run(app)

##*uvicorn <filename>:<appname> --reload
