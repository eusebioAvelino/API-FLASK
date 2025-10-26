from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/encabezados', methods=['GET'])
def saludo():
    PaginaHtl={'page_title': 'Calculo_Matematicos',
               'page_h1':'Pagina para calcular',
              'page_p':'Solo calculo',
             'page_footer' : "© 2025 Eusebio Avelino Guante — Todos los derechos reservados",
              'error-datos':'Error de datos' ,
              'page_error_h1':'Error en los datos ingresados',
              'page_error_p':'Por favor, asegúrate de ingresar solo números válidos.'

              }

    return jsonify(PaginaHtl)

@app.route('/calcular', methods=['POST'])
def calcular():
    datos = request.get_json()
    try:
        a = float(datos['a'])
        b = float(datos['b'])
        operacion = datos['operacion']
        
        if operacion == 'suma':
            resultado = a + b
        elif operacion == 'resta':
            resultado = a - b
        elif operacion == 'multiplicacion':
            resultado = a * b
        elif operacion == 'division':
            resultado = a / b if b != 0 else 'Error: división por cero'
        elif operacion == 'modulo':
            resultado = a % b
        elif operacion == 'potencia':
            resultado = a ** b
        else:
            return jsonify({'error': 'Operación no válida'}), 400

        return jsonify({'resultado': resultado})
    except (KeyError, ValueError, TypeError):
        return jsonify({'error': 'Datos inválidos'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
