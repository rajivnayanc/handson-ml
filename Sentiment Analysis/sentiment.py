from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def sentiment():  
    return render_template("formSentiment.html")  
 
@app.route('/predicting', methods = ['POST'])  
def result():  
    if request.method == 'POST':  
        #f = request.form[{{text}}] 
        #f.save(f.filename)  
        text=request.form['text']
        
        import pickle
        model=pickel.load(open('naive.pkl','rb'))
        result=model.predict([[text]])
        
        sentiment=['Positive','Negative']
        return render_template("predicting.html",cls=sentiment[result[0]])  
  
if __name__ == '__main__':  
    app.run(debug = True)
