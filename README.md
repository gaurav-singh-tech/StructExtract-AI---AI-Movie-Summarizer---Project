<div align="center">

# 🎬 StructExtract-AI
### AI-Powered Movie Information Extractor 

> **Turn unstructured movie text → clean, structured insights — in seconds.**

<p align="center">
  <a href="#-quickstart">
    <img src="https://img.shields.io/badge/🚀_Quickstart-Start_Here-111827?style=for-the-badge" alt="Quickstart">
  </a>
  <a href="https://github.com/gaurav-singh-tech/StructExtract-AI---AI-Movie-Summarizer---Project">
    <img src="https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/LangChain-Core-1C3A5E?style=for-the-badge" alt="LangChain">
  <img src="https://img.shields.io/badge/Mistral_AI-mistral--small--2506-FFA500?style=for-the-badge" alt="Mistral AI">
  <img src="https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge" alt="License">
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/gaurav-singh-tech/StructExtract-AI---AI-Movie-Summarizer---Project?style=social" alt="Stars">
  <img src="https://img.shields.io/github/forks/gaurav-singh-tech/StructExtract-AI---AI-Movie-Summarizer---Project?style=social" alt="Forks">
</p>

</div>

---

## 📖 What is StructExtract-AI?

**StructExtract-AI** is a lightweight AI pipeline that reads any free-form paragraph describing a movie and extracts a set of structured fields — automatically — using **Mistral AI** (via LangChain).


Live App Link : https://structextract-ai---ai-movie-summarizer---project-nbmbjfpwgm4we.streamlit.app/

It ships with **two interfaces**:

| Interface | File | Best for |
|---|---|---|
| 🖥️ **Streamlit Web App** | `UI_movie_summarizer.py` | Interactive browser UI |
| 💻 **CLI Script** | `movie_summarizer_code.py` | Terminal / automation |

Both use the same **LangChain `ChatPromptTemplate` → Mistral AI** pipeline, producing clean structured output every time.

---

## ✨ Features (verified from source)

- 🔍 **8-field extraction** — Movie Name, Director, Genre, Main Cast, Story Premise, Setting/Location, Key Themes, Central Conflict
- 📝 **Auto-summary** — 2–3 sentence concise summary generated alongside extracted fields
- 🛡️ **Hallucination guard** — model is instructed to output `"Not specified"` for any field not present in the input
- 🤖 **Mistral AI powered** — uses `mistral-small-2506` via `langchain-mistralai`
- 🎨 **Streamlit UI** — wide layout, spinner feedback, sidebar about-panel, real-time extraction
- 🔑 **Flexible key management** — `.env` via `python-dotenv` (CLI) or Streamlit Secrets (UI)

---

## 🗺️ Architecture (Mermaid Mindmap)

```mermaid
mindmap
  root((StructExtract-AI))
    Interface
      Streamlit UI
        UI_movie_summarizer.py
        Wide layout
        Spinner + error states
        Sidebar about panel
      CLI Script
        movie_summarizer_code.py
        input() prompt
        print response
    LangChain Pipeline
      ChatPromptTemplate
        SystemMessage
          8-field extraction rules
          Hallucination guard
          Summary instruction
        HumanMessage
          paragraph placeholder
      ChatMistralAI
        mistral-small-2506
        API key via env / secrets
    Output
      Movie Name
      Director
      Genre
      Main Cast
      Story Premise
      Setting / Location
      Key Themes
      Central Conflict
      Quick Summary
    Configuration
      MISTRAL_API_KEY
      .env file (CLI)
      Streamlit Secrets (UI)
```

---

## 📊 Infographic: How It Works

```text
╔══════════════════════════════════════════════════════════════════╗
║                     🎬  StructExtract-AI                        ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   INPUT                                                          ║
║   ┌─────────────────────────────────────────────────────────┐   ║
║   │  "Inception is a 2010 sci-fi thriller directed by        │   ║
║   │   Christopher Nolan. Leonardo DiCaprio stars as a        │   ║
║   │   thief who enters people's dreams..."                   │   ║
║   └────────────────────────┬────────────────────────────────┘   ║
║                            │                                     ║
║                            ▼                                     ║
║   LANGCHAIN PIPELINE                                             ║
║   ┌─────────────────────────────────────────────────────────┐   ║
║   │  ChatPromptTemplate                                      │   ║
║   │  ├─ SystemMessage  (extraction rules + format)          │   ║
║   │  └─ HumanMessage   ({paragraph} input)                  │   ║
║   └────────────────────────┬────────────────────────────────┘   ║
║                            │                                     ║
║                            ▼                                     ║
║   MISTRAL AI  (mistral-small-2506)                               ║
║   ┌─────────────────────────────────────────────────────────┐   ║
║   │  Processes prompt → generates structured response       │   ║
║   └────────────────────────┬────────────────────────────────┘   ║
║                            │                                     ║
║                            ▼                                     ║
║   OUTPUT                                                         ║
║   ┌─────────────────────────────────────────────────────────┐   ║
║   │  Movie Name:      Inception                              │   ║
║   │  Director:        Christopher Nolan                      │   ║
║   │  Genre:           Sci-Fi / Thriller                      │   ║
║   │  Main Cast:       Leonardo DiCaprio                      │   ║
║   │  Story Premise:   Thief enters dreams to plant ideas     │   ║
║   │  Setting:         Dreams / Various cities                │   ║
║   │  Key Themes:      Reality, Memory, Subconscious          │   ║
║   │  Central Conflict: Completing the inception mission      │   ║
║   │  Quick Summary:   2–3 sentence auto-generated summary    │   ║
║   └─────────────────────────────────────────────────────────┘   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 📁 Repository Structure

| File / Folder | Type | Purpose |
|---|---|---|
| `UI_movie_summarizer.py` | Python | Streamlit web app — paste text, click button, see structured output |
| `movie_summarizer_code.py` | Python | CLI script — terminal input/output via LangChain + Mistral |
| `requirements.txt` | Text | All Python dependencies |
| `README.md` | Markdown | This file |

---

## ⚙️ Configuration & Environment Variables

Both the CLI script and Streamlit app need a **Mistral API key**.

| Variable | Required | Used by |
|---|---|---|
| `MISTRAL_API_KEY` | ✅ Yes | `UI_movie_summarizer.py` + `movie_summarizer_code.py` |

### CLI — use a `.env` file
Create `.env` in the project root:
```dotenv
MISTRAL_API_KEY=your_mistral_api_key_here
```
> The CLI script loads this automatically via `load_dotenv()`.

### Streamlit — use Streamlit Secrets
Add to `.streamlit/secrets.toml` (local) or the Secrets panel in Streamlit Cloud:
```toml
MISTRAL_API_KEY = "your_mistral_api_key_here"
```
> The Streamlit app reads it via `os.getenv("MISTRAL_API_KEY")`.

**Get a free Mistral API key:** [https://console.mistral.ai/](https://console.mistral.ai/)

---

## 🚀 Quickstart

### Prerequisites
- Python 3.10+
- A Mistral AI API key ([get one free](https://console.mistral.ai/))

### 1 — Clone & install
```bash
git clone https://github.com/gaurav-singh-tech/StructExtract-AI---AI-Movie-Summarizer---Project.git
cd StructExtract-AI---AI-Movie-Summarizer---Project

python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

### 2 — Set your API key

**For CLI:**
```bash
echo "MISTRAL_API_KEY=your_key_here" > .env
```

**For Streamlit:**
```bash
mkdir -p .streamlit
echo 'MISTRAL_API_KEY = "your_key_here"' > .streamlit/secrets.toml
```

---

## ▶️ Run the App

### Option A — Streamlit Web UI
```bash
streamlit run UI_movie_summarizer.py
```
Opens at `http://localhost:8501`

- Paste any movie description into the text area
- Click **"Extract Information"**
- See structured fields + summary rendered on screen

### Option B — CLI Script
```bash
python movie_summarizer_code.py
```
- You are prompted: `Enter a paragraph about a movie:`
- Paste or type the text, press Enter
- Structured output is printed to the terminal

---

## 💡 Usage / Examples

**Input:**
```
The Dark Knight is a 2008 superhero film directed by Christopher Nolan.
Christian Bale stars as Batman, who faces the Joker, played by Heath Ledger,
a criminal mastermind who plunges Gotham City into anarchy. The film explores
themes of chaos, justice, and moral ambiguity.
```

**Expected output:**
```
Movie Name:       The Dark Knight
Director:         Christopher Nolan
Genre:            Superhero / Thriller
Main Cast:        Christian Bale, Heath Ledger
Story Premise:    Batman faces the Joker, a criminal who brings chaos to Gotham
Setting/Location: Gotham City
Key Themes:       Chaos, Justice, Moral Ambiguity
Central Conflict: Batman vs. the Joker's anarchic campaign

Quick Summary:
The Dark Knight (2008) pits Batman against the Joker, a villain who exploits
Gotham's systems to spread chaos. Directed by Christopher Nolan, the film
earned widespread acclaim for its exploration of justice and moral complexity.
Heath Ledger's portrayal of the Joker is widely considered iconic.
```

---

## 🃏 Flashcards

**Q1: What LangChain class builds the prompt?**
> `ChatPromptTemplate.from_messages([...])` — combines a system message (instructions) and a human message (the paragraph).

**Q2: Which model is used?**
> `mistral-small-2506` via `ChatMistralAI` from `langchain-mistralai`.

**Q3: How does the app prevent hallucination?**
> The system prompt instructs the model: *"Do NOT hallucinate. If any field is missing → write 'Not specified'."*

**Q4: How is the API key provided to the Streamlit app?**
> Via `os.getenv("MISTRAL_API_KEY")` — loaded from environment variables or Streamlit Secrets at runtime.

**Q5: What is `prompt.invoke({"paragraph": ...})`?**
> It fills the `{paragraph}` placeholder in the prompt template, producing a ready-to-send list of messages.

**Q6: What does `model.invoke(final_prompt)` return?**
> An AI message object; the text content is in `.content`.

**Q7: What fields are always extracted?**
> Movie Name, Director, Genre, Main Cast, Story Premise, Setting/Location, Key Themes, Central Conflict, and a Quick Summary.

**Q8: What happens if a field isn't in the input?**
> The model outputs `"Not specified"` for that field — no guessing, no fabrication.

---

## 🧯 Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| `Add MISTRAL_API_KEY in Streamlit Secrets` error | Key not set | Add `MISTRAL_API_KEY` to your `.streamlit/secrets.toml` or environment |
| `AuthenticationError` or 401 from Mistral | Invalid / expired key | Regenerate key at [console.mistral.ai](https://console.mistral.ai/) |
| CLI hangs at `Enter a paragraph…` | Waiting for input | Type or paste your text and press Enter |
| `ModuleNotFoundError: langchain_mistralai` | Package not installed | Run `pip install -r requirements.txt` inside the virtualenv |
| Streamlit page not loading | Port conflict | Try `streamlit run UI_movie_summarizer.py --server.port 8502` |
| Empty / partial extraction | Very short input | Provide a more detailed paragraph (at least 2–3 sentences) |

---

## 👤 Author

**Gaurav Singh** — AI / ML Engineer

<p>
  <a href="https://www.linkedin.com/in/contact-gauravsingh/">
    <img src="https://img.shields.io/badge/LinkedIn-Gaurav_Singh-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://github.com/gaurav-singh-tech">
    <img src="https://img.shields.io/badge/GitHub-gaurav--singh--tech-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="https://www.gaurav-singh-portfolio.me/">
    <img src="https://img.shields.io/badge/Portfolio-gaurav--singh--portfolio.me-22C55E?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Portfolio">
  </a>
</p>

---

<div align="center">

### ⭐ If StructExtract-AI is useful to you, give it a star — it helps more builders discover it!

[![GitHub stars](https://img.shields.io/github/stars/gaurav-singh-tech/StructExtract-AI---AI-Movie-Summarizer---Project?style=social)](https://github.com/gaurav-singh-tech/StructExtract-AI---AI-Movie-Summarizer---Project)

</div>
