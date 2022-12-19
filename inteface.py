from flask import Flask, jsonify, render_template, request, redirect
import config
from utils import FishSpecies

app = Flask(__name__)
@app.route('/',methods=['GET', "POST"])
def hello():    
    return render_template("index1.html")

@app.route('/predict',methods = ['GET', "POST"])
def prediction():
    if request.method == 'GET':       
        Weight = eval(request.args.get("Weight"))
        Length1 = eval(request.args.get("Length1"))
        Length2 = eval(request.args.get("Length2"))
        Length3 = eval(request.args.get("Length3"))
        Height = eval(request.args.get("Height"))
        Width = eval(request.args.get("Width"))
        print('value',Weight,Length1,Length2,Length3,Height,Width)
        med_dbs = FishSpecies(Weight,Length1,Length2,Length3,Height,Width)
        pred_class = med_dbs.get_predicted_outcome()
        print("::::::::::",pred_class)      
        return render_template("index1.html", prediction = pred_class)
if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5004)
    app.run()
