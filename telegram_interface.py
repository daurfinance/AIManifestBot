import os
from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, Filters
from github_interface import GitHubInterface
from gpt_engine import GPT
from gtts import gTTS
from speech_recognition import Recognizer, AudioFile
import tempfile

load_dotenv()

class TelegramBot:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_TOKEN")
        if not self.token:
            raise ValueError("TELEGRAM_TOKEN is not set in the environment variables.")
        self.application = Application.builder().token(self.token).build()
        self.github = GitHubInterface()
        self.gpt = GPT()
        self.recognizer = Recognizer()

        self.application.add_handler(CommandHandler("ai_prompt", self.ai_prompt))
        self.application.add_handler(CommandHandler("status", self.status))
        self.application.add_handler(CommandHandler("logs", self.logs))
        self.application.add_handler(CommandHandler("summary", self.summary))
        self.application.add_handler(MessageHandler(Filters.voice, self.handle_voice))
        self.application.add_handler(MessageHandler(Filters.video, self.handle_video))
        self.application.add_handler(MessageHandler(Filters.text, self.handle_text))

    def ai_prompt(self, update: Update, context: CallbackContext):
        prompt = " ".join(context.args)
        result = self.gpt.generate_code(prompt)
        self.github.commit_changes(
            file_path="auto_generated.py",  # Пример файла
            content=result,
            message=f"Auto-generated changes based on prompt: {prompt}"
        )
        update.message.reply_text("✅ Задача выполнена!")

    def status(self, update: Update, context: CallbackContext):
        status = "Работает"  # Заглушка для статуса
        update.message.reply_text(f"🛠️ Статус: {status}")

    def logs(self, update: Update, context: CallbackContext):
        logs = "Логи недоступны"  # Заглушка для логов
        update.message.reply_text(f"📜 Логи:\n{logs}")

    def summary(self, update: Update, context: CallbackContext):
        summary = "Сводка недоступна"  # Заглушка для сводки
        update.message.reply_text(f"📊 Сводка:\n{summary}")

    def handle_voice(self, update: Update, context: CallbackContext):
        file = update.message.voice.get_file()
        with tempfile.NamedTemporaryFile(delete=True) as temp_audio:
            file.download(temp_audio.name)
            with AudioFile(temp_audio.name) as source:
                audio_data = self.recognizer.record(source)
                try:
                    text = self.recognizer.recognize_google(audio_data)
                    response = self.gpt.generate_code(text)
                    update.message.reply_text(f"\u2705 Распознанный текст: {text}\nОтвет: {response}")
                except Exception as e:
                    update.message.reply_text(f"\u26a0 Ошибка распознавания: {e}")

    def handle_video(self, update: Update, context: CallbackContext):
        update.message.reply_text("\u26a0 Обработка видео пока не поддерживается.")

    def handle_text(self, update: Update, context: CallbackContext):
        prompt = update.message.text
        response = self.gpt.generate_code(prompt)
        tts = gTTS(response, lang='en')
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as temp_audio:
            tts.save(temp_audio.name)
            update.message.reply_audio(audio=open(temp_audio.name, 'rb'))

    def run(self):
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)