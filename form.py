from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm

class IrisDatasetForm(FlaskForm):
  SepalLength = StringField('Sepal Length',  [validators.DataRequired()])
  SepalWidth = StringField('Sepal Width', [validators.DataRequired()])
  PetalLength = StringField('Petal Length', [validators.DataRequired()])
  PetalWidth = StringField('Petal Width', [validators.DataRequired()])
                 
  submit = SubmitField('Predict')