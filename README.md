# 🎯 Voice Assistant local with Python and Ollama

> Program voice assistant dengan pyhton dan ollama , kita menggunakan model qwen2.5:0.5b karena model yang ringan sehingga dapat menjawab dibawah 3 detik

## ✨ Alur kerja
- 🔥 **Pilih Karakter AI**: Gunakan karakter unik dengan kepribadian berbeda atau yang sudah tersedia.
- 🗣️ **Speech-to-Text**: User Berbicara lalu ubah suara menjadi teks.
- 🎙️ **Model Chat**: Text tersebut digunakan untuk percakapan user dengan model.
- 🗣️ **Text-to-Speech**: Response dari model di ubah ke suara.

## 📌 Teknologi yang Digunakan
- 🐍 Python  
- 🎭 SpeechRecognition  
- 🔊 pyttsx3 (Text-to-Speech)  
- ⚡ Ollama 

## 🚀 Step by step
1. **Download Ollama**
   download Ollama di
   https://ollama.com


2. **Download model**
   Intsall model mu di cmd
   ollama run your-model


3. **Buat Venv**
   ```Venv
   python -m venv env
   env/Script/activate

4. **Instal package**
   ```package
   pip install requirements.txt

5. **Run Program**
   ```Run program
   python main.py