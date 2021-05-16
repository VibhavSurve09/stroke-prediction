from pydantic import BaseModel

class Human(BaseModel):
    age:int
    hypertension:int
    heart_disease:int
    avg_glucose_level:int
    bmi:int
    isMale:int
    isOther:int
    ever_married_Yes:int
    work_type_Never_worked:int
    work_type_Private:int
    work_type_Self_employed:int
    work_type_children:int
    Residence_type_Urban:int
    smoking_status_formerly_smoked:int
    smoking_status_never_smoked:int
    smoking_status_smokes:int