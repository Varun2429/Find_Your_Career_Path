import math
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
app = Flask(__name__)
cors = CORS(app)
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
data = pd.read_csv('Mini.csv')
@app.route('/')
def Enter():
    return render_template('home.html')
@app.route('/index')
def index():
    schools = sorted(data['school'].unique())
    courses = sorted(data['course'].unique())
    groups = sorted(data['group'].unique())
    degrees = sorted(data['degree'].unique())
    branches = sorted(data['branch'].unique())
    schools.insert(0, 'Select Secondary Education')
    return render_template('index.html', schools=schools, courses=courses, groups=groups, degrees=degrees,
                           branches=branches)
@app.route('/predict', methods=['POST'])
def predict():
    schools = request.form.get('schools')
    courses = request.form.get('courses')
    groups = request.form.get('groups')
    degrees = request.form.get('degrees')
    branches = request.form.get('branches')
    prediction = model.predict(
        pd.DataFrame([[schools, courses, groups, degrees, branches]], columns=['school', 'course',
                                                                               'group', 'degree',
                                                                               'branch']))
    prediction = math.floor(prediction)
    df = pd.read_csv('C:/Users/Deva Adithya/Downloads/Career project semi/Career project/output.csv')
    df2 = df.loc[df['in'] == prediction, 'out'].iloc[0]
    return df2


if __name__ == '__main__':
    app.run(debug=True)
