
from flask import Flask
from flask import render_template ,url_for, request , redirect
from flask_caching import Cache
import os
import sys
import VpnHunter
from flask import jsonify
cache = Cache()
cachetime= 6000

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)



@app.route("/")
@cache.memoize(timeout=cachetime)
def index():
  return render_template("index.html")


@app.route("/ip/<string:ip_input>")
@cache.memoize(timeout=cachetime)
def ipapi1(ip_input):
  try:
      res= None
      print(ip_input)
      x ,res = VpnHunter.ip4(ip_input)
      if(x != 0):
          print("Doing ASN based Analysis")
          asn= VpnHunter.asnFind(ip_input)
          print(asn)
          x, res = VpnHunter.asn(asn)
          print(x,res)
          return jsonify(VPN=x, Description=res)
      return jsonify(VPN=x, Description=res)
  except:
      return jsonify(VPN= -1, Description="Error occurred")
  
#404 error redirect 
@app.route('/<path:subpath>')
@cache.memoize(timeout=cachetime)
def pagenotfound(subpath):
    return redirect (url_for('index'))
#    return index()


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run()