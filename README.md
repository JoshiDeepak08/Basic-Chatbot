# AI Chat Assistant — FastAPI + Gemini + React

A minimal, fast, full-stack AI chatbot built with **FastAPI**, **Google Gemini (2.0 Flash)**, and a **React + Vite** frontend.
The backend exposes a simple `/chat` API that streams user prompts to Gemini and returns AI-generated responses.
link- https://basic-chatbot-xi.vercel.app/

This project is ideal for:

* Learning FastAPI + modern frontend integration
* Understanding how to connect LLMs with a custom UI
* Building your own AI assistant, RAG system, or chatbot product

---

##  Features

### **Backend (FastAPI)**

* Gemini 2.0 Flash model integration
* Clean and scalable FastAPI structure
* CORS enabled for frontend communication
* Environment-based API key loading
* Error handling and validation using Pydantic

### **Frontend (React + Vite)**

* Modern chat UI
* User + bot message styling
* Local chat history persistence
* Auto-scroll + typing indicators
* Fully responsive and customizable layout

---

##  Folder Structure

```
root/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── main.jsx
    │   └── App.css
    ├── index.html
    └── package.json
```

---

## Environment Variables

Create a `.env` file inside the **backend** folder:

```
GOOGLE_API_KEY=your_api_key_here
```

You can get a Gemini API key from:
[https://ai.google.dev/gemini-api](https://ai.google.dev/gemini-api)

---

##  Backend Setup (FastAPI)

### 1. Install dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Run the FastAPI server

```bash
uvicorn main:app --reload
```

Backend will start at:

```
http://localhost:8000
```

### 🌐 API Endpoints

#### **GET /** — Health Check

Returns `{ "status": "ok" }`

#### **POST /chat**

Request body:

```json
{
  "user_message": "Hello!"
}
```

Response:

```json
{
  "response": "Hello! How can I help you today?"
}
```

---

##  Frontend Setup (React + Vite)

### 1. Install dependencies

```bash
cd frontend
npm install
```

### 2. Run development server

```bash
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

Ensure CORS settings in backend allow your frontend URL.

---

##  Deploying

### **Backend (FastAPI)**

You can deploy using:

* Render
* Railway
* Fly.io
* AWS / GCP / Azure

Just install dependencies and run:

```
uvicorn main:app --host 0.0.0.0 --port 8000
```

### **Frontend (React)**

Build the production bundle:

```bash
npm run build
```

Deploy `dist/` to:

* Vercel
* Netlify
* Cloudflare Pages

---

##  Contributing

Pull requests are welcome!
If you want to extend this project with:

* RAG (retrieval augmented generation)
* Vector DB (Qdrant, Pinecone, FAISS)
* File uploads
* Streaming responses
* Authentication
  …feel free to fork and build on top of it.

---

##  License

This project is licensed under the MIT License — free to use, modify, and distribute.


