# ToolHunt 🔍
*Advanced Cybersecurity Arsenal Discovery Platform*

<!-- PROJECT LOGO -->
![ToolHunt Logo](https://github.com/cyberytti/ToolHunt/blob/main/docs/logo/ToolHunt_logo.png)


[![License: GNU](https://img.shields.io/badge/License-GNU-green.svg)](https://opensource.org/licenses/GNU)
[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/flask-2.0+-red.svg)](https://flask.palletsprojects.com/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

## Overview 🌟

ToolHunt is a comprehensive cybersecurity tool discovery platform featuring over 3,000 security tools in a searchable database. Built with semantic search capabilities, it helps security professionals, penetration testers, and researchers quickly find the right tools for their specific needs using natural language queries.

## Key Features 🚀

- **🔍 Semantic Search Engine**: Advanced search using sentence transformers and FAISS vector similarity for intelligent tool discovery
- **🗃️ Comprehensive Database**: 3,000+ cybersecurity tools across multiple categories including network scanning, vulnerability assessment, password cracking, and digital forensics
- **⚡ Hybrid Search Algorithm**: Combines semantic search with BM25 keyword matching for optimal result relevance
- **🎮 Cyberpunk-Themed Interface**: Terminal-inspired dark UI with animated backgrounds and responsive design
- **⚡ Real-time Results**: Fast Flask-powered backend with instant search results and tool categorization
- **☁️ Google Colab Support**: Integrated notebook for easy cloud deployment with ngrok tunneling

## Live Demo 🎥

<!-- DEMO VIDEO -->
[![Demo Video](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)
*Replace VIDEO_ID with your YouTube video ID. For local videos, use:*
```markdown
![Demo Video](docs/demo.mp4)
```

## Screenshots 📸

<!-- SCREENSHOT 1 - Main Interface -->
![Main Search Interface](https://github.com/cyberytti/ToolHunt/blob/main/docs/showcase_images/Screenshot%20from%202025-09-04%2015-57-39.png)
*Main search interface with cyberpunk styling.*

<!-- SCREENSHOT 2 - Search Results -->
![Search Results Display](https://github.com/cyberytti/ToolHunt/blob/main/docs/showcase_images/Screenshot%20from%202025-09-04%2015-58-40.png)
*Tool search results with categorization and descriptions.*


## Technology Stack 🛠️

### Frontend
- **🎨 HTML5/CSS3** - Responsive cyberpunk-themed interface
- **⚡ Vanilla JavaScript** - Dynamic search functionality and UI interactions
- **✨ Font Awesome** - Security-themed icons and visual elements

### Backend
- **🐍 [Flask](https://flask.palletsprojects.com/)** - Lightweight web framework
- **🐍 [Python 3.12+](https://python.org)** - Core application language

### Search Engine
- **⛓️ [LangChain](https://langchain.com/)** - used in similarity search
- **🤗 [HuggingFace Transformers](https://huggingface.co/sentence-transformers)** - Sentence embedding models
- **🔍 [FAISS](https://faiss.ai/)** - Vector similarity search
- **📊 [BM25](https://en.wikipedia.org/wiki/Okapi_BM25)** - Keyword-based retrieval

### Data Storage
- **💾 CSV Database** - Tool information storage with structured data

### Deployment
- **☁️ [Google Colab](https://colab.research.google.com/)** - Cloud notebook environment
- **🚇 [ngrok](https://ngrok.com/)** - Secure tunnel for public access

## Project Structure 📁

```
ToolHunt/
├── app.py                      # Main Flask application entry point
├── backend/                    # Core search functionality
│   ├── main.py                # Search orchestration and CSV processing
│   ├── semantic_search.py     # Hybrid search implementation
│   └── database/              # Tool database storage
│       └── tool_list_database.csv  # 3000+ cybersecurity tools
├── templates/                 # Frontend templates
│   └── index.html            # Main application interface
├── toolhunt_in_colab.py      # Google Colab deployment script
├── pyproject.toml            # Python project configuration
├── uv.lock                   # Dependency lock file
├── LICENSE                   # MIT license
└── README.md                 # Project documentation
```

## Quick Start 🚀

### Prerequisites
- Python 3.12 or higher
- pip package manager
- [To be determined - specific system requirements]

### Local Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ToolHunt.git
cd ToolHunt

# Install dependencies
pip install flask langchain langchain-huggingface langchain-community faiss-cpu rank_bm25 sentence-transformers

# Run the application
python app.py
```

The application will start at `http://localhost:5000`

### Google Colab Deployment

1. Open the provided Colab notebook: `toolhunt_in_colab.py`
2. Replace the ngrok authentication token with your own
3. Run all cells to deploy with public URL access
4. Access your ToolHunt instance via the generated ngrok URL

## Usage 🔍

### Basic Search
Navigate to the main interface and enter search queries using natural language:

```
Example searches:
- "network scanner"
- "sql injection tools" 
- "password cracking utilities"
- "vulnerability assessment"
- "digital forensics analysis"
```

### Search Features
- **🧠 Semantic Understanding**: Searches understand context and intent
- **📂 Category Filtering**: Tools are automatically categorized
- **📊 Relevance Scoring**: Results ranked by similarity and keyword matching
- **ℹ️ Tool Information**: Each result includes description, category, and direct links

## Database 💾

The tool database contains 3,000+ cybersecurity tools with the following structure:
- **Tool Name**: Official tool name
- **Description**: Detailed functionality description  
- **Link**: Official download/documentation URL

## Search Algorithm 🤖

ToolHunt uses a hybrid search approach:

1. **🔍 Semantic Search**: Uses HuggingFace sentence transformers to create embeddings
2. **📐 Vector Similarity**: FAISS performs fast similarity matching
3. **🔤 Keyword Matching**: BM25 handles exact keyword queries
4. **🔄 Result Fusion**: Combines both approaches for optimal relevance

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following the existing code style
4. Test your changes locally
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Guidelines
- Follow PEP 8 Python style guidelines
- Maintain the cyberpunk aesthetic for UI changes
- Test search functionality with various queries
- Update documentation for new features

## Ethical Use ⚖️

ToolHunt is designed for legitimate cybersecurity professionals, researchers, and educational purposes. Users are responsible for:
- Complying with all applicable laws and regulations
- Using tools only on systems they own or have explicit permission to test
- Following responsible disclosure practices
- Respecting terms of service for included tools

## License 📄

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.
