from flask import Flask, request, send_file
import pdfkit
import io

app = Flask(__name__)

@app.route('/html-to-pdf', methods=['POST'])
def html_to_pdf():
    data = request.get_json()
    html = data.get('html')
    
    if not html:
        return {"error": "No HTML provided"}, 400

    # Convert HTML to PDF in memory
    pdf = pdfkit.from_string(html, False)

    return send_file(
        io.BytesIO(pdf),
        mimetype='application/pdf',
        as_attachment=True,
        download_name='invoice.pdf'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
