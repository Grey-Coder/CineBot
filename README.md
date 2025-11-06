#  CineBot – AI Movie Recommendation Chatbot

CineBot is an intelligent **AI-powered movie and cinema recommendation chatbot** built using **Rasa** and **Flask**, designed to help users discover films through natural, conversational interaction.  
It features a clean, responsive **HTML chat interface**, **real-time REST API integration**, and can even be accessed publicly using **ngrok**.

---

##  Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Folder Structure](#folder-structure)
- [Features](#features)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Ngrok Public Access](#ngrok-public-access)
- [API Communication](#api-communication)
- [File Descriptions](#file-descriptions)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

---

##  Overview

CineBot connects **Rasa’s NLP engine** with a **Flask backend** to deliver dynamic, personalized movie recommendations in real time.  
Users can chat naturally through a simple web interface to get curated suggestions, discover trending films, or find information about specific genres or actors.

It’s a great starting point for understanding how to build **Conversational AI** systems that blend natural language understanding, backend logic, and a user-friendly frontend.

We have this bot in two different languages i.e. English (en) and Bengali (bn). This README file is properly calibrated with 'en' version.

---

##  Architecture

### **System Components**
| Component | Description |
|------------|-------------|
| **Frontend (HTML/JS)** | Interactive chat interface for users to communicate with CineBot. |
| **Flask Server (app.py)** | Handles web routes, connects Rasa API with the frontend, and manages chat sessions. |
| **Rasa Backend** | Processes user messages, performs intent recognition, and generates responses. |
| **Custom Action Server (optional)** | Handles advanced logic, like API-based movie lookups or database queries. |

### **Workflow**
1. The user types a message in the web chat UI.  
2. Flask forwards the message to Rasa’s REST API endpoint.  
3. Rasa processes the text, identifies the intent, and generates a reply.  
4. Flask receives and displays the response instantly on the UI.  

---

##  Folder Structure

```
en_CineBot/
│
├── .rasa/                        
│
├── actions/                      
│   ├── __pycache__/              
│   ├── __init__.py               
│   └── actions.py                # Contains custom logic for movie recommendations
│
├── data/                         # Training data for Rasa NLU and stories
│   ├── nlu.yml                   # Intent examples and entity definitions
│   ├── rules.yml                 # Conversation rules
│   └── stories.yml               # Story-based dialogue training data
│
├── models/                       # Trained Rasa model files
│   ├── 20250227-065508-resultant-cevian.tar
│   ├── 20250227-072139-dry-bocce.tar
│   └── 20250227-075259-mute-actress.tar
│
├── static/                       
│   └── index.html                # Main chatbot interface (UI)
│  
│
├── tests/                        
│   └── test_stories.yml          # Test stories for conversation flow validation
│
├── app.py                        # Flask app file integrating with Rasa REST API
│
├── config.yml                    # Rasa pipeline & policy configuration
├── credentials.yml               # API connectors (e.g., REST channel)
├── domain.yml                    # Intents, entities, slots, and responses
├── endpoints.yml                 # Action and model server configuration
│
└── requirements.txt              # Python dependencies for project setup
```


---

##  Features
-  Movie & cinema recommendation chatbot powered by Rasa.  
-  Intent recognition and NLP understanding via Rasa pipelines.  
-  Flask backend with REST API integration.  
-  Responsive HTML/JS chat interface.  
-  Optional public access through ngrok.  
-  Custom Rasa actions for API-driven movie data retrieval.  
-  Modular structure for easy customization and enhancement.

---

##  Installation

### **1️ Clone the Repository**
```bash
git clone https://github.com/Grey-Coder/cinebot.git
cd cinebot
```

### **2️ Create and Activate Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate        # Windows
```

### **3️ Install Dependencies**
```bash
pip install -r requirements.txt
```
If no requirements file exists:
```bash
pip install rasa flask requests
```

---

##  Running the Project

### **Step 1: Start Rasa Server**
```bash
cd rasa
rasa run --enable-api --cors "*" --debug
```

### **Step 2: Start Action Server (if used)**
```bash
rasa run actions
```

### **Step 3: Start Flask Application**
In another terminal:
```bash
python app.py
```

Now visit  [http://localhost:5000](http://localhost:5000) to start chatting with CineBot!

---

##  Ngrok Public Access

To share CineBot publicly:
```bash
ngrok http 5000
```
Copy the public link (e.g., `https://yourname.ngrok.io`) and share it for demo access.

---

##  API Communication

### **Flask → Rasa Endpoint**
**Endpoint:** `/webhooks/rest/webhook`  
**Method:** `POST`

**Request Example:**
```json
{
  "sender": "user",
  "message": "Recommend me a sci-fi movie"
}
```

**Response Example:**
```json
[
  {
    "recipient_id": "user",
    "text": "You might love 'Interstellar'! It's a classic science fiction masterpiece."
  }
]
```

---

##  File Descriptions

| File | Description |
|------|--------------|
| `app.py` | Flask web server handling chat routing and API calls. |
| `index.html` | Chat interface served to the browser. |
| `domain.yml` | Defines intents, entities, slots, and responses. |
| `nlu.yml` | Contains user message examples and intents. |
| `stories.yml` | Defines dialogue flows. |
| `actions.py` | Custom Python actions for movie recommendation logic. |
| `requirements.txt` | Python dependencies for the environment. |

---

##  Technologies Used
- **Python 3.8+**
- **Rasa** – NLP and dialogue management  
- **Flask** – Backend server framework  
- **HTML / CSS / JavaScript** – Frontend chat interface  
- **Ngrok** – Public access tunneling tool  

---

##  Future Enhancements
-  Integrate with TMDb or IMDb APIs for real movie data.  
-  Deploy CineBot on Render, Railway, or AWS.  
-  Add chat session storage using SQLite or MongoDB.  
-  Add voice interaction (speech-to-text).  
-  Support for personalized recommendations using ML models.  

---

##  Contributing
Contributions are welcome!  
To contribute:  
1. Fork the repository  
2. Create a feature branch (`feature-branch`)  
3. Commit your changes  
4. Open a Pull Request  

---

##  Author
**Amit Acharjee**  
 *amitacharjee06@gmail.com*  
 [[Amit Acharjee | LinkedIn](https://www.linkedin.com/in/amit--acharjee/)]
 [[Amit Acharjee | Profile](https://www.amitacharjee.tech)]

---

##  License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

### ⭐ If you find CineBot helpful, don’t forget to **star** the repository on GitHub!

