from flask import Flask, render_template, flash
from form import SetTotp
import onetimepass
import pyqrcode
import base64


app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/", methods=['GET','POST'])
@app.route("/index", methods=['GET','POST'])
def index():
    label = "FV Example"
    mail = "fvillalobos@medioclick.com"
    #TODO: Con la Herramineta totp, se puede genera un secret aleatoriio, pero se deja fijo para realizar pruebas.
    secret = "JBSWY3DPEHPK3PXP"
    issuer = "FV Example"
    chl = "otpauth://totp/{0}:{1}?secret={2}&issuer={3}".format(label,mail,secret,issuer)

    secret = chl
    # var_url = "https://chart.googleapis.com/chart?chs=200x200&chld=M|0&cht=qr&chl="+ chl.encode('ascii', 'xmlcharrefreplace') # se podria reemplazar por data.encode('ascii', 'xmlcharrefreplace')
    var_url = pyqrcode.create(chl)
    var_url.svg('static/uca.svg', scale=4)
    # var_url.svg('uca-url.svg', scale=8)

    # totp = ROTP::TOTP.new(secret, issuer: issuer)
    topt = onetimepass.get_totp(b'JBSWY3DPEHPK3PXP', 3)

    result = ""

    form = SetTotp()


    if form.validate_on_submit():
        if onetimepass.valid_totp(form.totp_code(), secret):
            result = "Correcto"
        else:
            result = "Incorrecto"
    else:
        result = "ERROR: REVISAR CODIGO"

    return render_template('totp.html', form=form, var_url=var_url, secret=secret, result=result,topt=topt)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
