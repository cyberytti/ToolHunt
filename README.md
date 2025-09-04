# ToolHunt 🔍
*Advanced Cybersecurity Arsenal Discovery Platform*

<p align="center">
  <img src="https://github.com/cyberytti/ToolHunt/blob/main/docs/logo/ToolHunt_logo.png" alt="ToolHunt Logo" width="600"/>
</p>

<p align="center">
  <strong>Discover. Deploy. Defend.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Tools-3000+-brightgreen?style=for-the-badge&logo=hammer-screwdriver" alt="3000+ Tools"/>
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python" alt="Python 3.12+"/>
  <img src="https://img.shields.io/badge/Flask-2.0+-red?style=for-the-badge&logo=flask" alt="Flask 2.0+"/>
  <img src="https://img.shields.io/badge/License-GNU-green?style=for-the-badge&logo=gnu" alt="GNU License"/>
</p>

---

## 🌟 Overview

ToolHunt is your ultimate cybersecurity tool discovery platform, featuring **3,000+ security tools** in a searchable database. With advanced semantic search capabilities, it helps security professionals, penetration testers, and researchers quickly find the perfect tools for their specific missions using natural language queries.

---

## 🚀 Key Features

| Feature | Description |
|---------|-------------|
| 🔍 **Semantic Search Engine** | Advanced AI-powered search using sentence transformers and FAISS vector similarity |
| 🗃️ **Comprehensive Database** | 3,000+ cybersecurity tools across multiple categories and specialties |
| ⚡ **Hybrid Search Algorithm** | Combines semantic search with BM25 keyword matching for optimal relevance |
| 🎮 **Cyberpunk Interface** | Immersive terminal-inspired dark UI with animated backgrounds |
| ☁️ **Cloud Deployment** | One-click Google Colab deployment with ngrok tunneling |
| 📱 **Responsive Design** | Works seamlessly on desktop, tablet, and mobile devices |

---

## 🎥 Live Demo

<p align="center">
  <img src="https://github.com/cyberytti/ToolHunt/blob/main/docs/showcase_video/ToolHunt_showcase_video.gif" alt="ToolHunt Demo" width="800"/>
</p>

---

## 📸 Screenshots

### Main Search Interface
![Main Search Interface](https://github.com/cyberytti/ToolHunt/blob/main/docs/showcase_images/Screenshot%20from%202025-09-04%2015-57-39.png)
*Cyberpunk-styled main interface with immersive terminal aesthetic*

### Search Results
![Search Results Display](https://github.com/cyberytti/ToolHunt/blob/main/docs/showcase_images/Screenshot%20from%202025-09-04%2015-58-40.png)
*Intelligent tool categorization with detailed descriptions*

---

## 🛠️ Technology Stack

### Frontend
| Technology | Purpose |
|------------|---------|
| ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) | Structure & Semantics |
| ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) | Cyberpunk Styling |
| ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) | Dynamic Interactions |
| ![Font Awesome](https://img.shields.io/badge/Font_Awesome-528DD7?style=flat-square&logo=font-awesome&logoColor=white) | Security Icons |

### Backend
| Technology | Purpose |
|------------|---------|
| ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) | Web Framework |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | Core Language |

### Search Engine
| Technology | Purpose |
|------------|---------|
| ![LangChain](https://img.shields.io/badge/LangChain-FF6B00?style=flat-square) | Similarity Search |
| ![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black) | Sentence Embeddings |
| ![FAISS](https://img.shields.io/badge/FAISS-00C2FF?style=flat-square) | Vector Similarity |
| ![BM25](https://img.shields.io/badge/BM25-8A2BE2?style=flat-square) | Keyword Matching |

---

## 📁 Project Structure

```plaintext
ToolHunt/
├── 🐍 app.py                      # Main Flask application
├── 🔧 backend/
│   ├── main.py                # Search orchestration
│   ├── semantic_search.py     # Hybrid search implementation
│   └── database/
│       └── tool_list_database.csv  # 3000+ tools database
├── 🎨 templates/
│   └── index.html            # Cyberpunk interface
├── ☁️ toolhunt_in_colab.py      # Google Colab deployment
├── ⚙️ pyproject.toml            # Project configuration
├── 📦 uv.lock                   # Dependency lock
├── 📄 LICENSE                   # GNU License
└── 📖 README.md                 # You are here!
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- pip package manager

### Local Installation

```bash
# Clone the repository
git clone https://github.com/cyberytti/ToolHunt.git
cd ToolHunt

# Install dependencies
pip install -r requirements.txt

# Launch ToolHunt
python app.py
```

Access your local instance at: `http://localhost:5000`

### ☁️ One-Click Cloud Deployment

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cyberytti/ToolHunt/blob/main/toolhunt_in_colab.py)

1. Click the Google Colab badge above
2. Replace the ngrok authentication token
3. Run all cells
4. Access your public ToolHunt instance via the generated URL

---

## 🔍 Usage Examples

| Search Type | Example Queries |
|-------------|-----------------|
| **Network Security** | `"network scanner"`, `"port enumeration tools"` |
| **Web Application** | `"sql injection tools"`, `"web vulnerability scanner"` |
| **Password Attacks** | `"password cracking utilities"`, `"brute force tools"` |
| **Forensics** | `"digital forensics analysis"`, `"memory analysis tools"` |
| **Reconnaissance** | `"OSINT gathering tools"`, `"subdomain enumeration"` |

---

## 💾 Database Schema

The comprehensive database includes:

| Field | Description |
|-------|-------------|
| **Tool Name** | Official tool name |
| **Description** | Detailed functionality description |
| **Category** | Primary cybersecurity category |
| **Link** | Official documentation/download URL |
| **Platform** | Supported operating systems |

---

## 🤖 Search Architecture

```mermaid
graph TD
    A[User Query] --> B(Semantic Embedding)
    A --> C(BM25 Keyword Extraction)
    B --> D[FAISS Vector Search]
    C --> E[Keyword Matching]
    D --> F[Result Fusion]
    E --> F
    F --> G[Ranked Results]
    G --> H[Cyberpunk UI Display]
```

---

## 🤝 Contributing

We welcome contributions from the cybersecurity community!

### Development Process
1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💻 Make your changes
4. ✅ Test thoroughly
5. 📝 Commit your changes (`git commit -m 'Add amazing feature'`)
6. 📤 Push to the branch (`git push origin feature/amazing-feature`)
7. 🔀 Open a Pull Request

### Guidelines
- Follow PEP 8 style guidelines
- Maintain the cyberpunk aesthetic
- Test search functionality with various queries
- Update documentation for new features

---

## ⚖️ Ethical Use

> **Important**: ToolHunt is designed for legitimate cybersecurity purposes only.

**Responsible Usage Guidelines:**
- 🔒 Use only on systems you own or have explicit permission to test
- 📜 Comply with all applicable laws and regulations
- 🤝 Follow responsible disclosure practices
- 📋 Respect terms of service for included tools

---

## 📄 License

This project is licensed under the **GNU License** - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <strong>ToolHunt 🔍 - Empowering Cybersecurity Professionals Worldwide</strong>
</p>

<p align="center">
  <sub>Built with ❤️ by the cybersecurity community</sub>
</p>

<p align="center">
  <a href="https://github.com/cyberytti/ToolHunt/stargazers">
    <img src="https://img.shields.io/github/stars/cyberytti/ToolHunt?style=social" alt="GitHub stars"/>
  </a>
  <a href="https://github.com/cyberytti/ToolHunt/fork">
    <img src="https://img.shields.io/github/forks/cyberytti/ToolHunt?style=social" alt="GitHub forks"/>
  </a>
</p>
