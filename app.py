from flask import Flask,render_template,request
from detector import check
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
  result=None
  reasons=[]
  score=0
  if request.method=="POST":
    url=request.form["url"]
    result,score,reasons=check(url)
  return render_template(
      "index.html",
      result=result,
      score=score,
      reasons=reasons
    )
if __name__=="__main__":
    app.run(debug=True)