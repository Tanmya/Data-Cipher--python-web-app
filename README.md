# Data-Cipher--python-web-app

Introduction

This Python web application is built using the Flask framework and the cryptography library. It allows users to encrypt or decrypt small files using custom keys. The application has two routes: /encrypt and /decrypt. The /encrypt route takes a custom key and a file input from the user, and returns the encrypted file to the user. The /decrypt route takes a custom key and an encrypted file input from the user, and returns the decrypted file to the user.

Dependencies

The application requires the following Python packages to be installed:

1. Flask
2. cryptography

These can be installed using pip by running the following command:
  pip install flask cryptography

Running the application
To run the application, navigate to the directory where the app.py file is located and run the following command:
  python app.py
This will start the Flask web server, and the application will be accessible at http://localhost:5000.

Routes
The application has two routes: /encrypt and /decrypt.

/encrypt
The /encrypt route is a POST route that takes the following parameters:

key: A custom key to use for encrypting the file.
file: The file to be encrypted.
On submission of the form, the route reads the contents of the file, encrypts it using the custom key provided, and returns the encrypted file to the user as a download.

/decrypt
The /decrypt route is a POST route that takes the following parameters:

key: The custom key used to encrypt the file.
file: The encrypted file to be decrypted.
On submission of the form, the route reads the contents of the encrypted file, decrypts it using the custom key provided, and returns the decrypted file to the user as a download.

Security Considerations

This application does not include any authentication or authorization mechanisms, so it should only be used for personal or experimental purposes.

Additionally, this application is only suitable for encrypting and decrypting small files, as it loads the entire contents of the file into memory at once. For larger files, it may be necessary to process the file in smaller chunks to avoid running out of memory.

It's also important to note that while the cryptography library is a widely used and respected library for encryption, it's still possible to misuse it and create vulnerabilities. Therefore, it's recommended to follow best practices for key management and encryption, and to consult with a security expert if necessary.

Conclusion

This Python web application provides a simple way for users to encrypt or decrypt small files using custom keys. It can be used for personal or experimental purposes, but should not be used for sensitive or production use cases without proper authentication and authorization mechanisms.
