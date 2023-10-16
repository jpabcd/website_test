from flask import Flask,render_template,jsonify
app=Flask(__name__)
Jobs=[{'id':1,'title':"Python Developer","location":"New York","salary":"$100k"},
{'id':2,'title':"Java Developer","location":"San Francisco","salary":"$120k"},
{'id':3,'title':".Net Developer","location":"San Francisco","salary":"$110k"}]
@app.route('/')
def hello_world():
  return render_template('home.html',jobs=Jobs,company_name='Jovian')
  
@app.route('/api/jobs')
def list_jobs():
  return jsonify(Jobs)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)