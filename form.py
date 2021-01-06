from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import Form

class IrisDatasetForm(FlaskForm):
  SepalLength = StringField('Sepal Length',  [validators.DataRequired()])
  SepalWidth = StringField('Sepal Width', [validators.DataRequired()])
  PetalWidth = StringField('Petal Width', [validators.DataRequired()])
  PetalWidth = StringField('Petal Width', [validators.DataRequired()])
                 
  submit = SubmitField('Predict')