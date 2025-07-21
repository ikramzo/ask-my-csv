# 🌞 YANCCA: Yet Another CSV Chatbot Assistant

A powerful and intuitive web application that lets you chat with your CSV data using natural language. Built with LangChain, Streamlit, and OpenAI's GPT models.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-latest-red.svg)
![LangChain](https://img.shields.io/badge/langchain-latest-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- 📊 **Interactive CSV Analysis** - Upload any CSV file and analyze it with natural language
- 🌍 **Multi-language Support** - Get responses in English, French, Spanish, German, Italian, or Portuguese
- 💬 **Chat Interface** - Persistent conversation history with your data
- 🔄 **Session Persistence** - Your files and settings are remembered throughout the session
- 📈 **Smart Agent** - Powered by LangChain's pandas DataFrame agent
- 🎯 **Sample Questions** - Pre-built queries to get you started quickly
- 🧹 **Session Management** - Clear file and chat controls

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))
- UV package manager ([install here](https://docs.astral.sh/uv/getting-started/installation/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/csv-chat-assistant.git
   cd csv-chat-assistant
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

4. **Run the application**
   ```bash
   uv run streamlit run app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_TEMPERATURE=0.0
MAX_FILE_SIZE_MB=200
DEBUG=False
```

### Supported Languages

- 🇺🇸 English
- 🇫🇷 French (Français)
- 🇪🇸 Spanish (Español)
- 🇩🇪 German (Deutsch)
- 🇮🇹 Italian (Italiano)
- 🇵🇹 Portuguese (Português)

## 📖 Usage

### 1. Upload Your Data
- Click "Choose a CSV file" and upload your data
- The app will automatically load and preview your file
- File persists throughout your session

### 2. Select Language
- Choose your preferred response language from the sidebar
- All AI responses will be in your selected language

### 3. Ask Questions
- Type natural language questions about your data
- Use sample questions for inspiration
- View your conversation history

### Example Questions

```
"What are the basic statistics of this dataset?"
"Show me the first 10 rows"
"Are there any missing values?"
"What's the correlation between sales and price?"
"Create a summary grouped by region"
"Plot a histogram of the age column"
```

## 🏗️ Project Structure

```
csv-chat-assistant/
├── src/
│   ├── config/
│   │   └── config.py          # Configuration management
│   ├── constants.py           # Language prompts and constants
│   └── csv_assistant/         # Future modules
├── app.py                     # Main Streamlit application
├── pyproject.toml            # UV project configuration
├── .env.example              # Environment variables template
├── README.md                 # This file
└── sample_data/              # Sample CSV files
```

## 🧪 Development

### Adding New Languages

1. Edit `src/constants.py`:
   ```python
   LANGUAGE_PROMPTS = {
       # ... existing languages
       "Japanese": "あなたはデータアナリストです。明確な洞察を提供してください。",
   }
   ```

2. The language will automatically appear in the sidebar selector

### Running Tests

```bash
uv run pytest tests/
```

### Code Formatting

```bash
uv run black .
uv run flake8 .
```

## 🚀 Deployment

### Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Connect your repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Add your environment variables in the Streamlit Cloud dashboard
4. Deploy with one click!

### Docker

```bash
# Build the image
docker build -t csv-chat-assistant .

# Run the container
docker run -p 8501:8501 csv-chat-assistant
```

### Other Platforms

- **Heroku**: Use the included `Procfile`
- **Railway**: Connect your GitHub repository
- **Render**: Deploy as a web service

## 💰 Usage Costs

- **OpenAI API**: ~$0.001 per 1K tokens (very affordable for CSV analysis)
- **Deployment**: Free tier available on most platforms
- **Recommended**: Start with $5 in OpenAI credits (lasts very long)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the powerful AI framework
- [Streamlit](https://streamlit.io/) for the amazing web app framework
- [OpenAI](https://openai.com/) for the language models
- [UV](https://docs.astral.sh/uv/) for fast Python package management

## 📞 Support

If you have any questions or issues:

1. Check the [Issues](https://github.com/yourusername/csv-chat-assistant/issues) page
2. Create a new issue if needed
3. Star ⭐ the repository if you find it helpful!

---

**Made with ❤️ and lots of ☕**