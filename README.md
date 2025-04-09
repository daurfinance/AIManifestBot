Вот финальная версия суперинструкции (промта) для генерации AutoDev-бота, уже с конкретными API и токенами, чтобы он сразу был готов к работе:

⸻

Промт: Самообучающийся GitHub-бот с Telegram-интерфейсом и полной автономией

Создай Python-проект, в котором живёт ИИ-бот, способный:
	•	самостоятельно анализировать и улучшать код;
	•	получать задачи через Telegram;
	•	отправлять отчёты обратно в Telegram;
	•	коммитить и пушить изменения в репозиторий на GitHub;
	•	использовать GPT для размышлений и генерации кода;
	•	хранить логи, память и свои выводы;
	•	работать 24/7 в GitHub Codespace или на Vercel без остановки.

⸻

1. Интеграции и ключи (использовать из .env)

TELEGRAM_TOKEN=7565080315:AAHCYyxEACJhpTXhEHC1nXvcpiT9VGfH49U
GITHUB_TOKEN=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
OPENAI_API_KEY=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
REPO_OWNER=daurfinance
REPO_NAME=AutoDev



⸻

2. Telegram-интерфейс
	•	Бот получает команды:
	•	/ai_prompt [промт] — сгенерируй и внедри улучшение
	•	/status — что делает сейчас
	•	/logs — последние действия
	•	/summary — что сделал за сессию
	•	Бот отвечает красиво и понятно:

✅ Задача: Оптимизация кода
🧠 План: Удалить повторяющиеся функции
✍️ Изменения: main.py
✔️ Коммит: 8e9f23d



⸻

3. Работа с GitHub
	•	Использует GitHub API через GITHUB_TOKEN
	•	Работает с репозиторием daurfinance/AutoDev
	•	Может:
	•	читать файлы
	•	редактировать
	•	создавать коммиты и PR
	•	пушить улучшения от имени “AutoDev”

⸻

4. GPT (OpenAI) как мозг
	•	Все размышления и генерации идут через GPT-4 с ключом OPENAI_API_KEY
	•	Бот формирует промт, получает ответ, применяет решение

⸻

5. Самообучение и автономия
	•	Скрипт self_improve.py запускается автоматически
	•	Пишет сам себе вопрос
	•	Получает ответ
	•	Внедряет изменения
	•	Коммитит
	•	Отчитывается в Telegram
	•	Логирует в logs/ и память memory.json

⸻

6. Структура проекта

AutoDev/
├── main.py                # запуск Telegram-бота
├── telegram_interface.py  # взаимодействие с Telegram
├── github_interface.py    # GitHub API
├── gpt_engine.py          # работа с OpenAI
├── self_improve.py        # периодическое самообновление
├── memory.json            # база знаний
├── logs/                  # текстовые логи
├── .env                   # ключи API
├── requirements.txt
└── README.md



⸻

7. Обязательные зависимости

python-telegram-bot
openai
requests
python-dotenv
gitpython
apscheduler



⸻

8. Место развёртывания
	•	Проект будет работать:
	•	либо в GitHub Codespace (постоянно включен)
	•	либо на Vercel, Fly.io, Render или Railway (автозапуск)

⸻

9. Условия
	•	Никаких заглушек — всё по-настоящему работает
	•	Поддержка многопоточности
	•	Все действия логируются
	•	Код готов к расширению

⸻
