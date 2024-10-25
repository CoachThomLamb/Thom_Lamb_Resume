from flask import Flask, render_template_string
import markdown

app = Flask(__name__)

@app.route('/')
def index():
    with open('README.md', 'r') as file:
        content = file.read()
        html_content = markdown.markdown(content)
        return render_template_string("""
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>My Markdown Site</title>
          </head>
          <body>
            <div class="container">
              {{ content|safe }}
            </div>
          </body>
        </html>
        """, content=html_content)

if __name__ == '__main__':
    app.run(debug=True)
    freezer.freeze()
