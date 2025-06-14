from flask import Flask, render_template, request, jsonify
import mysql.connector # type: ignore

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",  # Replace with your MySQL password
        database="pghms"
    )

# Route to render index.html template
@app.route('/')
def index():
    return render_template('list.html')

# Route to handle search request
@app.route('/search', methods=['POST'])
def search():
    location = request.json['location']
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT name, lat, lon, location, map_embed_url, image_url, avg_rating 
    FROM hostels
    WHERE location LIKE %s
    OR location LIKE %s
    OR location LIKE %s
    ORDER BY avg_rating DESC
    """
    cursor.execute(query, (location + '%', '% ' + location + '%', '%-' + location + '%'))
    hostels = cursor.fetchall()

    cursor.close()
    conn.close()

    if not hostels:
        return jsonify({'error': 'No hostels found in this location'})

    return jsonify({'hostels': hostels})

if __name__ == '__main__':
    app.run(debug=True)
