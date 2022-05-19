# importing libraries
from flask import Flask, request
import joblib
import numpy

# uploading the files
mod_path = "mlmodels/model.pkl"
scale_x_path = "mlmodels/scale_x.pkl"
scale_y_path = "mlmodels/scale_y.pkl"

mod_path_final = "mlmodels/model_cat.pkl"
scale_x_path_final = "mlmodels/scale_x_cat.pkl"
scale_y_path_final = "mlmodels/scale_y_cat.pkl"

app = Flask(__name__)

@app.route('/predict_price', methods = ['GET'])

# function definition
def predict():
    args = request.args
    mod = args.get('model', default=-1, type=int)
    rooms = args.get('rooms', default=-1, type=int)
    area = args.get('area', default=-1, type=float)
    floor = args.get('floor', default=-1, type=int)
    open_plan = args.get('open_plan', default=-1, type=int)
    renovation = args.get('renovation', default=-1, type=int)

# For the 1st model
    if mod == 1:

        mod1 = joblib.load(mod_path)
        sc_x1 = joblib.load(scale_x_path)
        sc_y1 = joblib.load(scale_y_path)
        x1 = numpy.array([open_plan, rooms, area, renovation]).reshape(1, -1)
        x1 = sc_x1.transform(x1)
        res1 = mod1.predict(x1)
        res1 = sc_y1.inverse_transform(res1.reshape(1, -1))

        return str(res1[0][0])

# For the 2nd model
    if mod == 2:

        mod2 = joblib.load(mod_path_final)
        sc_x2 = joblib.load(scale_x_path_final)
        sc_y2 = joblib.load(scale_y_path_final)
        x2 = numpy.array([floor, open_plan, rooms, area]).reshape(1, -1)
        x2 = sc_x2.transform(x2)
        res2 = mod2.predict(x2)
        res2 = sc_y2.inverse_transform(res2.reshape(1, -1))

        return str(res2[0][0])

    else:
        return "please indicate model 1 or 2"

if __name__ == '__main__':
    app.run(debug=True, port=5444, host='0.0.0.0')