# 🎙️ AI Radio Bot - Motivation On Demand

A Python-powered radio bot that generates personalized motivational quotes using **Google's Gemini CLI** and converts them to speech for your daily inspiration! This project showcases the integration of Google's powerful Gemini AI model through their command-line interface with Python automation.

## ✨ Features

- 🤖 **AI-Powered Quotes**: Uses Google Gemini CLI to generate unique motivational quotes
- 🛠️ **Gemini CLI Integration**: Seamlessly integrates with Google's official Gemini command-line interface
- 🔊 **Text-to-Speech**: Converts quotes to audio using Google Text-to-Speech (gTTS)
- 🎵 **Auto-Play**: Automatically plays the generated audio
- 🌈 **Beautiful Terminal UI**: Features loading spinners, step-by-step progress, and colorful output
- 💾 **Audio Saving**: Saves generated quotes as MP3 files for later listening
- 🔄 **Dynamic Content**: Requests different motivational quotes each time you run it

## 🚀 Demo

```
======================================================================
🎙️  AI RADIO BOT 
======================================================================
🚀 Starting your daily dose of inspiration...
======================================================================

📍 STEP 1: INITIALIZING AI RADIO BOT
📍 STEP 2: GENERATING MOTIVATIONAL QUOTE
📍 STEP 3: QUOTE GENERATED!
✨ TODAY'S MOTIVATIONAL QUOTE ✨

💬 "The best way to predict the future is to create it."

📍 STEP 4: CONVERTING TO AUDIO
📍 STEP 5: PLAYING AUDIO
🎉 AI RADIO BOT SESSION COMPLETE! 🎉
```

## 📋 Prerequisites

- **Python 3.7+** - Main programming language
- **Node.js and npm** - Required for Gemini CLI installation
- **Google Gemini CLI** - Official command-line interface for Google's Gemini AI
- **Internet connection** - For AI communication and TTS services

### About Gemini CLI

The [Google Gemini CLI](https://www.npmjs.com/package/@google/gemini-cli) is Google's official command-line interface for interacting with their Gemini AI models. It provides:
- Direct access to Gemini 2.5 Pro and other models
- Interactive chat sessions
- File processing capabilities
- Web search integration
- Customizable AI interactions

**Learn more:**
- 📖 [Official Google Blog: Introducing Gemini CLI](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)
- 💻 [Gemini CLI GitHub Repository](https://github.com/google-gemini/gemini-cli)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aditya7248/ai-radio-bot.git
   cd ai-radio-bot
   ```

2. **Install Python dependencies**
   ```bash
   pip install gtts
   ```

3. **Install Google Gemini CLI**
   ```bash
   npm install -g @google/gemini-cli
   ```
   
   **Verify installation:**
   ```bash
   gemini --version
   ```

4. **Set up Gemini CLI** (First time setup)
   ```bash
   gemini config
   ```
   Follow the prompts to authenticate with your Google account.

## 🎯 Usage

Simply run the script:

```bash
python radio_bot.py
```

The bot will:
1. Connect to Gemini AI
2. Generate a unique motivational quote
3. Convert it to speech
4. Play the audio
5. Save the MP3 file for later

## 📁 Files

- `radio_bot.py` - Main script with all functionality
- `motivational_quote.mp3` - Generated audio file (created after first run)

## 🎨 Features Breakdown

### Loading Spinners
Beautiful animated spinners show real-time progress:
- 🤖 Connecting to Gemini AI...
- 📝 Sending quote request...
- 🧠 Gemini is thinking...
- 🔊 Converting text to speech...

### Quote Generation
- Uses Google Gemini AI through the official CLI for unique, personalized quotes
- Leverages Gemini's advanced language understanding and creativity
- Subprocess communication with the Gemini CLI for seamless integration
- Requests different quotes each time to ensure variety
- Intelligent response parsing to extract clean quotes
- Fallback quotes if AI is unavailable
- Smart quote extraction from AI response

### Audio Features
- High-quality text-to-speech using Google TTS
- Automatic playback on Windows (using winsound)
- MP3 file saving for offline listening
- Error handling for audio issues

## 🔧 Customization

You can modify the prompt in `get_quote_from_gemini()` function:

```python
prompt = "Give me a short inspiring motivational quote to start the day under 30 words. And eveytime give me different motivational quote.\n"
```

## 🐛 Troubleshooting

### Common Issues:

1. **"gemini command not found"**
   - Ensure Gemini CLI is installed: `npm install -g @google/gemini-cli`
   - Check if it's in PATH: `gemini --version`
   - On Windows, restart your terminal after installation

2. **Gemini CLI authentication issues**
   - Run `gemini config` to set up authentication
   - Ensure you have a valid Google account
   - Check internet connection

3. **"No module named 'gtts'"**
   - Install gTTS: `pip install gtts`
   - Use the correct Python version if you have multiple installed

3. **Audio not playing**
   - The MP3 file is still saved in the directory
   - Check your system audio settings

4. **Timeout errors**
   - Check your internet connection
   - Gemini AI might be temporarily slow

## 🤝 Contributing

Feel free to fork this project and submit pull requests! Some ideas for improvements:

- Add more TTS language options
- Create a GUI version
- Add quote categories (fitness, business, etc.)
- Integration with other AI models
- Scheduling for daily quotes

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Google Gemini AI & CLI** - For providing powerful AI capabilities and excellent command-line tools
- **Google Text-to-Speech** - For high-quality audio conversion
- **The Python community** - For excellent libraries and subprocess handling
- **npm community** - For seamless package management

## 🔗 Useful Links

### Official Google Resources
- 📖 [Google Blog: Introducing Gemini CLI - Open Source AI Agent](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)
- 💻 [Gemini CLI Official GitHub Repository](https://github.com/google-gemini/gemini-cli)
- 📦 [Gemini CLI npm Package](https://www.npmjs.com/package/@google/gemini-cli)

### Documentation
- 📚 [Google Text-to-Speech Documentation](https://gtts.readthedocs.io/)
- 🐍 [Python subprocess Documentation](https://docs.python.org/3/library/subprocess.html)

---

**Made with ❤️ for daily motivation!**

*Start every day with inspiration! 🌟*
