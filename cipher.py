from flask import Flask, render_template, request, redirect, send_file
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    key = request.form['key']
    file = request.files['file']
    f = Fernet(key.encode())
    encrypted_data = f.encrypt(file.read())
    return send_file(encrypted_data, attachment_filename=file.filename+'.enc', as_attachment=True)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    key = request.form['key']
    file = request.files['file']
    f = Fernet(key.encode())
    decrypted_data = f.decrypt(file.read())
    return send_file(decrypted_data, attachment_filename=file.filename.replace('.enc', ''), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
