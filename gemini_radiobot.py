import os
import subprocess
import sys
import time
import re
import threading
from gtts import gTTS

class LoadingSpinner:
    def __init__(self, message="Loading"):
        self.message = message
        self.is_running = False
        self.spinner_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.thread = None
    
    def spin(self):
        i = 0
        while self.is_running:
            sys.stdout.write(f"\r{self.spinner_chars[i % len(self.spinner_chars)]} {self.message}")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
    
    def start(self):
        self.is_running = True
        self.thread = threading.Thread(target=self.spin)
        self.thread.start()
    
    def stop(self, success_message=""):
        self.is_running = False
        if self.thread:
            self.thread.join()
        sys.stdout.write("\r" + " " * 60 + "\r")
        if success_message:
            sys.stdout.write(f"✅ {success_message}\n")
        sys.stdout.flush()

def print_banner():
    print("\n" + "=" * 70)
    print("🎙️  AI RADIO BOT ")
    print("=" * 70)
    print("🚀 Starting your daily dose of inspiration...")
    print("=" * 70 + "\n")

def print_step(step_number, message):
    print(f"📍 STEP {step_number}: {message}")
    print("-" * 50)

def play_audio(filename):
    try:
        import winsound
        winsound.PlaySound(filename, winsound.SND_FILENAME)
        print("🎵 Audio played successfully!")
        return True
    except Exception as e:
        print(f"⚠️  Could not play audio: {e}")
        print(f"📁 Audio saved as: {filename}")
        return False

def get_quote_from_gemini():
    """Get a motivational quote from Gemini CLI"""
    try:
        spinner = LoadingSpinner("🤖 Connecting to Gemini AI...")
        spinner.start()
        
        # Gemini CLI process with shell=True for Windows
        process = subprocess.Popen(
            'gemini',
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            shell=True
        )
        
        time.sleep(3)
        spinner.stop("Connected to Gemini AI!")
        
        spinner = LoadingSpinner("📝 Sending quote request...")
        spinner.start()
        
        prompt = "Give me a short inspiring motivational quote to start the day under 30 words. And eveytime give me different motivational quote.\n"
        process.stdin.write(prompt)
        process.stdin.flush()
        
        spinner.stop("Request sent!")
        
        spinner = LoadingSpinner("🧠 Gemini is thinking...")
        spinner.start()
        time.sleep(12) 
        
        process.stdin.write("exit\n")
        process.stdin.flush()
        
        output, error = process.communicate(timeout=20)
        spinner.stop("Response received!")
        
        if error:
            print(f"⚠️  Gemini stderr: {error}")
        
        lines = output.split('\n')
        quote = None
        
        print("🔍 Extracting quote from response...")
        
        for line in lines:
            line = line.strip()
            # lines that contain quotes or motivational content
            if ('"' in line and len(line) > 10 and len(line) < 150) or \
               ('✦' in line and len(line) > 10):
                # Clean up the line
                quote = line.replace('✦', '').strip()
                quote = quote.strip('"').strip("'")  # Remove surrounding quotes
                break
        
        if not quote:
            for line in lines:
                line = line.strip()
                if len(line) > 20 and len(line) < 150 and not line.startswith('>') and not line.startswith('│'):
                    quote = line
                    break
        
        if quote:
            print("✅ Quote successfully extracted!")
            return quote.strip()
        else:
            print("⚠️  Using fallback quote...")
            return "Every day is a new opportunity to grow and succeed!"
            
    except Exception as e:
        print(f"❌ Error getting quote from Gemini: {e}")
        print("⚠️  Using fallback quote...")
        return "Believe in yourself and make today amazing!"

def main():
    print_banner()
    
    print_step(1, "INITIALIZING AI RADIO BOT")
    time.sleep(1)
    print("✅ Bot initialized successfully!")
    print()
    
    print_step(2, "GENERATING MOTIVATIONAL QUOTE")
    quote = get_quote_from_gemini()
    print()
    
    print_step(3, "QUOTE GENERATED!")
    print("✨ TODAY'S MOTIVATIONAL QUOTE ✨")
    print(f"\n💬 \"{quote}\"\n")
    
    print_step(4, "CONVERTING TO AUDIO")
    
    try:
        spinner = LoadingSpinner("🔊 Converting text to speech...")
        spinner.start()
        
        tts = gTTS(text=quote, lang='en', slow=False)
        audio_file = "motivational_quote.mp3"
        tts.save(audio_file)
        
        spinner.stop("Audio conversion complete!")
        print(f"💾 Audio saved as: {audio_file}")
        print()
        
        print_step(5, "PLAYING AUDIO")
        print("🎧 Playing your motivational quote...")
        print("🔊 Listen up! 🔊")
        
        audio_played = play_audio(audio_file)
        print()
        
        print("=" * 70)
        print("🎉 AI RADIO BOT SESSION COMPLETE! 🎉")
        print("=" * 70)
        print(f"📝 Quote: \"{quote}\"")
        print(f"📁 Audio file: {audio_file}")
        if audio_played:
            print("🎵 Audio played successfully!")
        print("💪 You're ready to conquer the day!")
        print("=" * 70)
        
    except Exception as e:
        print(f"❌ Error with text-to-speech: {e}")
        print(f"💬 But here's your quote anyway: \"{quote}\"")
        print("📱 You can manually play the audio file if it was created.")

if __name__ == "__main__":
    main()