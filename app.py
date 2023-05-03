from flask import Flask,  render_template, request
import os
import openai


app = Flask(__name__)


openai.api_key = "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"
model_engine = "text-davinci-003"
#citation =[]

@app.route('/', methods = ["POST","GET"])
def index():
    if request.method == "POST":
        typ = request.form.get('type')
        personne  = request.form.get('personn')
        tone = request.form.get('tone')
        relation = request.form.get('relation')
        ajout = request.form.get('ajout')
        cita = gerateur(typ,personne,relation,tone,ajout)
        
        return render_template ('generateur.html', gene = cita)
       
    
    
    return render_template ('index.html')





def gerateur (ty,person,relat,to,ajo):
    prompt = f"Genere moi une citation de type {ty} a {person} qui est mon {relat} en utilisant un ton {to}. {ajo}"
    response = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      temperature=0.9,
      max_tokens=60,
       top_p=1,
      n=1,
      stop=None,
      )
    return response.choices[0]['text'] 
   





if __name__=='__main__':
    app.run(debug=True)