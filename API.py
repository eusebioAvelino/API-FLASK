from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/saludo', methods=['GET'])
def saludo():
    PaginaHtl={'page_title': 'Calculo_Matematicos',
               'page_h1':'Pagina para calcular',
              'page_p':'Solo calculo',
             'page_footer' : "© 2025 Eusebio Avelino Guante — Todos los derechos reservados"
              }

    return jsonify(PaginaHtl)

@app.route('/sumar', methods=['POST'])
def sumar():
    datos = request.get_json()
    try:
        a = float(datos['a'])
        b = float(datos['b'])
        resultado = a + b
        return jsonify({'resultado': resultado})
    except (KeyError, ValueError, TypeError):
        return jsonify({'error': 'Datos inválidos'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
