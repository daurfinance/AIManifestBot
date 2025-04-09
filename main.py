from telegram_interface import TelegramBot
from apscheduler.schedulers.background import BackgroundScheduler
from self_improve import self_improve

if __name__ == "__main__":
    bot = TelegramBot()
    scheduler = BackgroundScheduler()
    scheduler.add_job(self_improve, 'interval', hours=1)  # Запуск self_improve каждый час
    scheduler.start()
    bot.run()
