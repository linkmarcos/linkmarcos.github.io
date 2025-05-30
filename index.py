from flask import  Flask, render_template, jsonify, request
import time, sqlite3

app = Flask(__name__)
"""
@app.route('/')
def principal():
    return 'Bienvenido a mi app con python!'

@app.route('/contacto')
def comentarios():
    return 'Contactos de la app'
"""
@app.route('/')
def principal():
    num= time.asctime()
    conn = sqlite3.connect('proyecto sqlite3/Saludos.db')
    cursor = conn.cursor()
    datos = cursor.execute('SELECT Resto FROM Saludos').fetchall()
    cursor.close()
    conn.close()
    
    return render_template('index.html', num=num, dato=datos)

@app.route('/contacto')
def comentarios():
    return render_template('contacto.html')

@app.route('/get_time')
def get_time():
    current_time = time.strftime('%H:%M:%S')
    return jsonify({'time': current_time})

@app.route('/Saludos')
def Saludos():
    dat = request.form.get('texto')
    conn = sqlite3.connect('proyecto sqlite3/Saludos.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Saludos SET Resto = ? where ID = 0', (dat,))
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('index.html',)
if  __name__ == '__main__':
    app.run(host='127.0.0.1', debug=False, port=2000)
