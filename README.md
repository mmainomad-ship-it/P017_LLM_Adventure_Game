# 🗺️ P017: Text-Based Adventure Game (LLM Driven)

## 💡 Description
This project demonstrates the integration of a **local Large Language Model (LLM)**, using the Ollama Python library, into a structured, text-based adventure game. The Python script manages the game loop and state, while the LLM dynamically generates the narrative, location descriptions, and the consequences of player choices on every turn. This shows how to use an LLM for creative content generation within a fixed control structure.

## ✨ Key Features & Constraints
* **Dynamic Narrative:** All location descriptions and story outcomes are generated live by the LLM.
* **State Management:** The Python code strictly parses the LLM output to extract and update the **current location** (`current_location`) state variable.
* **Fixed Choices:** The game only accepts choices 1, 2, or 3, which is enforced by the main loop.
* **Local Execution:** Uses the Ollama library to run models entirely on local hardware (e.g., RTX 3090).

## 💻 Technology Stack
* **Language:** Python 3
* **LLM Interface:** `ollama` Python library
* **Environment:** `venv`
* **Model:** Any Ollama-compatible model (e.g., Llama 3, Mistral, Gemma).

## 🚀 Setup Instructions
1.  **Clone the Repository (or navigate to the directory):**
    ```bash
    git clone [REPO_URL]
    cd P017-LLM-Adventure-Game
    ```
2.  **Create and Activate Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Ensure Ollama Server is Running:** You must have the Ollama service running in the background and have a model (like `llama3`) pulled and ready to go.
    ```bash
    ollama run llama3
    # Use Ctrl+C to exit the chat, but keep the Ollama server running.
    ```
5.  **Run the Game:**
    ```bash
    python adventure_game.py
    ```

---

## ✍️ Author
* **Author:** mmainomad-ship-it
* **GitHub:** https://github.com/mmainomad-ship-it