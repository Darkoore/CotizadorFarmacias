from flask import Flask, render_template, request, send_file

app = Flask(__name__, template_folder='paginaWeb', static_folder='paginaWeb/Diseños')

@app.route('/')
def test():
    #return render_template('index.html')
    ip_address = request.remote_addr
    return f'<img src="/imagen"><br>IP address: {ip_address}'
@app.route('/imagen')
def imagen():
    return send_file('paginaWeb/Diseños/Imagenes/Memingo.jpg', mimetype='image/jpg')

if __name__ == '__main__':
    app.run(debug=True)