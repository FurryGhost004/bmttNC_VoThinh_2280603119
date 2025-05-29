from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher 
from cipher.playfair import PlayFairCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()
playfair_cipher = PlayFairCipher()
vigenere_cipher = VigenereCipher()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    plain_text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return f"Text: {plain_text} <br/> Key: {key} <br/> Encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    cipher_text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)  
    return f"Text: {cipher_text} <br/> Key: {key} <br/> Decrypted text: {decrypted_text}"

#vigenere
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt", methods=["POST"])
def vigenere_encrypt():
    plain_text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    encrypted_text = vigenere_cipher.encrypt_text(plain_text, key)
    return f"Text: {plain_text} <br/> Key: {key} <br/> Encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=["POST"])
def vigenere_decrypt():
    cipher_text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    decrypted_text = vigenere_cipher.decrypt_text(cipher_text, key)
    return f"Text: {cipher_text} <br/> Key: {key} <br/> Decrypted text: {decrypted_text}"

#play fair
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/encrypt", methods=["POST"])
def playfair_encrypt():
    plain_text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    encrypted_text = playfair_cipher.encrypt_text(plain_text, key)
    return f"Text: {plain_text} <br/> Key: {key} <br/> Encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=["POST"])
def playfair_decrypt():
    cipher_text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    decrypted_text = playfair_cipher.decrypt_text(cipher_text, key)
    return f"Text: {cipher_text} <br/> Key: {key} <br/> Decrypted text: {decrypted_text}"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

