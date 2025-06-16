from flask import Flask, request, send_file, render_template
import qrcode
from io import BytesIO

# Initialize the Flask application
app = Flask(__name__)

# Route for the homepage with the form
@app.route('/')
def home():
    # Render the HTML form for user input
    return render_template('index.html')

# Route to handle form submission and generate QR code
@app.route('/generate', methods=['POST'])
def generate_qr():
    # Get the user input from the form
    data = request.form['data']

    # If no data is provided, return an error
    if not data:
        return 'Please enter text or a URL.', 400

    # Generate a QR code image from the input data
    img = qrcode.make(data)

    # Create an in-memory buffer to save the image
    buf = BytesIO()
    
    # Save the QR code image to the buffer
    img.save(buf)

    # Rewind the buffer to the beginning
    buf.seek(0)

    # Return the image as a downloadable/displayable response
    return send_file(buf, mimetype='image/png')

# Run the app in debug mode if executed directly
if __name__ == '__main__':
    app.run(debug=True)
