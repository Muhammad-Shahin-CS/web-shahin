# from flask import Flask, render_template, request 

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/portfolio')
# def portfolio():
#     return render_template('templates/portfolio.html')

# @app.route('/projects')
# def projects():
#     return render_template('projects.html')
 
   
# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         contact = request.form.get('contact')
#         message = request.form.get('message') 
#         # Print the values to the console (or you can process them as needed)
#         print(f'Name: {name}')
#         print(f'Contact: {contact}')
#         print(f'Message: {message}') 
#         # You can redirect to a different page or render a template with a success message
#         return render_template('contact.html', message='Submitted Successfully') 
#     return render_template('contact.html')


 

# # # Database connection
# # conn = psycopg2.connect(os.getenv('DATABASE_URL'))
# # cursor = conn.cursor()

# # @app.route('/submit', methods=['POST'])
# # def submit_form():
# #     data = request.json
# #     name = data.get('name')
# #     contact = data.get('contact')
# #     message = data.get('message')
    
# #     # Insert data into PostgreSQL
# #     cursor.execute(
# #         "INSERT INTO form_data (name, contact, message) VALUES (%s, %s, %s)",
# #         (name, contact, message)
# #     )
# #     conn.commit()

# #     return jsonify({'status': 'success'}), 200
 

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
