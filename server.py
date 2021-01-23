
from flask import Flask
from flask import render_template ,url_for, request , redirect
from flask_caching import Cache
import os
import sys
import VpnHunter
from flask import jsonify
cache = Cache()
cachetime= 600

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)



def iphunt(ip_input):
#  try:
  res= None
  #print(ip_input)
  x ,res = VpnHunter.ip4(ip_input)
  print(x, res)
  if(x == 0):
      print("Doing ASN based Analysis")
      asn= VpnHunter.asnFind(ip_input)
      print(asn)
      x, res = VpnHunter.asn(asn)
      print(x,res)
      if(x == 1):
          VpnHunter.ip4LocalAdd(ip_input)
      return jsonify(VPN=x, Description=res)
  return jsonify(VPN=x, Description=res)
#  except:
#      return jsonify(Description="Error occurred" , VPN= -1)


@app.route("/")
@cache.memoize(timeout=cachetime)
def index():
  return render_template("index.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
    query= request.form['search_query']
    print("Query made --> ", query)
    x= iphunt(query)
    return(x)


@app.route("/ip/<string:ip_input>")
@cache.memoize(timeout=cachetime)
def ipapi1(ip_input):
    x= iphunt(ip_input)
    return(x)

  
#404 error redirect 
@app.route('/<path:subpath>')
@cache.memoize(timeout=cachetime)
def pagenotfound(subpath):
    return redirect (url_for('index'))
#    return index()


if __name__ == "__main__":
#    port = int(os.environ.get('PORT', 5000))
#    app.run(host='0.0.0.0', port=port)
    app.run()