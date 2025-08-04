###🏠 Hostel and PG Recommendation System Using Sentiment Analysis


---

**Overview**
This project is a location-based Hostel and PG Recommendation System that utilizes sentiment analysis of user reviews to assist students and working professionals in selecting the best-suited accommodations. The system incorporates multiple sentiment analysis models including TextBlob, VADER, BERT, RoBERTa, and RNN to provide accurate sentiment-based rankings.

---
**Features**
---

🔍 Location-based Hostel and PG Listing

💬 Sentiment Analysis on User Reviews

📊 Graphical Representation of Sentiment Distribution and Model Accuracy

🏆 Recommendation Based on Cost Efficiency and User Sentiments

🔐 User Authentication: Registration and Login

⚙️ Dynamic Model Selection (TextBlob, VADER, BERT, RoBERTa, RNN)

---

**Technologies Used**
---

Frontend: `HTML`  `CSS`  `JavaScript (Templates using Flask)`

Backend: `Python` `Flask`

Database: `MySQL (phpMyAdmin)`

Machine Learning Models used for Sentiment Analysis:

`TextBlob`

`VADER`

`BERT`

`RoBERTa`

`Recurrent Neural Networks (RNN)`

**System Architecture**
---

- Users provide reviews and ratings for hostels and PGs.

- The system preprocesses the text data.

- Sentiment analysis is performed using selected models.

- Recommendations are generated based on sentiment scores and cost efficiency.

- Results are displayed through dynamic web pages and graphical summaries.

**Installation and Setup**


Clone the repository:

```bash
git clone https://github.com/smaranng/Hostel-PGRecommender.git
```

- Install the required Python packages:

- Set up the MySQL database and import the provided SQL dump.

- Run the Flask server:


```bash


python app.py
```

Access the application at:

```
http://localhost:5000
```

**Folder Structure**
---
```

├── templates/
│   ├── index.html
│   ├── analysis.html
├── static/
├── sent.py(Streamlit)
├── app.py(Flask)
├── README.md
└── pghms.sql
```

**Usage**
---

- Register or log in to the system.

- Search hostels and PGs based on location.

- View sentiment analysis graphs and recommended options.

- Select the best accommodation based on reviews and cost.

**Future Enhancements**
---

- Integration of real-time review updates.

- Mobile application support.

- Advanced NLP models for multi-language support.

- Incorporation of user preferences and filters.
---

**Contributing**


Contributions are welcome. Please create a pull request or open an issue for suggestions.


