import asyncio
import os
import logging
import random
import json
import aiohttp
from datetime import datetime
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from deep_translator import GoogleTranslator


# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Загрузка токена из .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()
GEO_API_KEY = os.getenv("GEO_API_KEY")

# Глобальная переменная для таймера
active_timers = {}
# Состояния
#8
class Museum(StatesGroup):
    hall1 = State()
    hall2 = State()
    hall3 = State()
    hall4 = State()
#9
class Quiz(StatesGroup):
    q_process = State()
#10
class GeocoderState(StatesGroup):
    wait_address = State()
#11
class TranslatorState(StatesGroup):
    choosing_direction = State() # Выбор направления
    wait_text = State()          # Ожидание текста для перевода
#GUI 
def get_main_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Время"), KeyboardButton(text="Дата")],
        [KeyboardButton(text="/dice"), KeyboardButton(text="/timer")],
        [KeyboardButton(text="Начать экскурсию"),KeyboardButton(text="Пройти тест")],
        [KeyboardButton(text="Найти на карте"),KeyboardButton(text="Переводчик")]
    ], resize_keyboard=True)

def kb_hall1():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="В зал 2 (Средневековье)")],
        [KeyboardButton(text="Выйти из музея")]
    ], resize_keyboard=True)

def kb_hall2():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="В зал 3 (Новое время)")]
    ], resize_keyboard=True)

def kb_hall3():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="В зал 4 (Современность)")],
        [KeyboardButton(text="Вернуться в зал 1")]
    ], resize_keyboard=True)

def kb_hall4():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Вернуться в зал 1")]
    ], resize_keyboard=True)

def get_dice_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="кинуть один шестигранный кубик")],
        [KeyboardButton(text="кинуть 2 шестигранных кубика одновременно")],
        [KeyboardButton(text="кинуть 20-гранный кубик")],
        [KeyboardButton(text="вернуться назад")]
    ], resize_keyboard=True)

def get_timer_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="30 секунд"), KeyboardButton(text="1 минута")],
        [KeyboardButton(text="5 минут"), KeyboardButton(text="вернуться назад")]
    ], resize_keyboard=True)

def get_close_kb():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/close")]], resize_keyboard=True)

def get_quiz_retry_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Пройти тест снова")],
        [KeyboardButton(text="вернуться назад")]
    ], resize_keyboard=True)

def get_translator_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="🇷🇺 RU -> 🇺🇸 EN")],
        [KeyboardButton(text="🇺🇸 EN -> 🇷🇺 RU")],
        [KeyboardButton(text="вернуться назад")]
    ], resize_keyboard=True)

# Загружаем вопросы из JSON один раз при запуске
current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_json = os.path.join(current_dir, 'test.json')
with open(path_to_json, 'r', encoding='utf-8') as f:
    QUIZ_DATA = json.load(f)['test']

#Логика Переводчика 
@dp.message(F.text == "Переводчик")
async def trans_start(message: types.Message, state: FSMContext):
    logger.info(f"User {message.from_user.id} opened translator")
    await message.answer("Выберите направление перевода:", reply_markup=get_translator_kb())
    await state.set_state(TranslatorState.choosing_direction)

@dp.message(TranslatorState.choosing_direction, F.text.contains("->"))
async def set_direction(message: types.Message, state: FSMContext):
    if "RU" in message.text and "EN" in message.text and message.text.find("RU") < message.text.find("EN"):
        source, target = 'ru', 'en'
        dir_name = "с Русского на Английский"
    else:
        source, target = 'en', 'ru'
        dir_name = "с Английского на Русский"
    await state.update_data(src=source, dest=target)
    await message.answer(
        f"Установлено направление: {dir_name}.\nОтправьте текст для перевода.\n\n(Чтобы сменить язык или выйти, напишите 'назад')", 
        reply_markup=ReplyKeyboardRemove() 
    )
    await state.set_state(TranslatorState.wait_text)

@dp.message(TranslatorState.wait_text)
async def perform_translation(message: types.Message, state: FSMContext):
    # Если пользователь хочет вернуться или сменить язык
    if message.text.lower() == "назад":
        await state.clear() # Очищаем состояние
        await message.answer("Возвращаюсь в главное меню.", reply_markup=get_main_kb())
        return
    user_data = await state.get_data()
    src = user_data.get('src')
    dest = user_data.get('dest')
    logger.info(f"Translating {src}->{dest} for {message.from_user.id}")
    try:
        # Для надежности RU -> EN используем явное указание параметров
        translator = GoogleTranslator(source=src, target=dest)
        translated = translator.translate(message.text)
        if translated:
            await message.answer(f"Перевод ({src.upper()} -> {dest.upper()}):\n\n{translated}")
            await message.answer("Можете отправить следующий текст или написать 'назад' для выхода.")
        else:
            await message.answer("Не удалось получить перевод. Попробуйте другое слово.")
    except Exception as e:
        logger.error(f"Translation error: {e}")
        await message.answer("Ошибка сервиса перевода. Проверьте интернет или попробуйте позже.")

@dp.message(TranslatorState.choosing_direction, F.text == "вернуться назад")
async def trans_back(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Главное меню:", reply_markup=get_main_kb())

#Логика Геокодера
@dp.message(F.text == "Найти на карте")
async def geo_start(message: types.Message, state: FSMContext):
    await message.answer("Введите адрес объекта (например: Москва, Красная площадь):")
    await state.set_state(GeocoderState.wait_address)

@dp.message(GeocoderState.wait_address)
async def process_geo(message: types.Message, state: FSMContext):
    address = message.text
    logger.info(f"User {message.from_user.id} searched for address: {address}")

    async with aiohttp.ClientSession() as session:
        # Попытка найти координаты через Геокодер API
        geo_url = f"https://geocode-maps.yandex.ru/1.x/?apikey={GEO_API_KEY}&geocode={address}&format=json"
        try:
            async with session.get(geo_url) as response:
                if response.status != 200:
                    # Обработка ошибок HTTP с диагностикой
                    await message.answer(f"Ошибка сервера Яндекса (HTTP {response.status}). Попробуйте позже.")
                    return
                json_data = await response.json()
        except Exception as e:
            # Обработка сетевых ошибок
            await message.answer(f"Сетевая ошибка при запросе к API: {e}")
            return
        # Найден ли объект
        features = json_data['response']['GeoObjectCollection']['featureMember']
        if not features:
            # Обработка ситуации "ничего не найдено"
            await message.answer("К сожалению, по вашему запросу ничего не найдено. Проверьте правильность адреса.")
            return
        # Извлекаем данные
        obj = features[0]['GeoObject']
        coords = obj['Point']['pos'].split() # Получаем "долгота широта"
        lon, lat = coords[0], coords[1]
        full_name = obj['metaDataProperty']['GeocoderMetaData']['text']
        # Формируем ссылку на Static Maps API с меткой (pt) в центре
        static_map_url = f"https://static-maps.yandex.ru/1.x/?l=map&ll={lon},{lat}&z=14&pt={lon},{lat},pm2rdm"
        # Отправка фото с аннотацией (caption) одним сообщением
        try:
            await message.answer_photo(
                photo=static_map_url,
                caption=f"Найдено: {full_name}\nКоординаты: {lat}, {lon}"
            )
            await state.clear()
        except Exception as e:
            await message.answer(f"Не удалось загрузить карту: {e}")

#Логика Теста
@dp.message(F.text == "Пройти тест", StateFilter(None))
@dp.message(F.text == "Пройти тест снова")
async def start_quiz(message: types.Message, state: FSMContext):
    # Выбираем 10 случайных вопросов
    sample_questions = random.sample(QUIZ_DATA, min(len(QUIZ_DATA), 10))
    # Сохраняем данные в состояние пользователя
    await state.update_data(
        questions=sample_questions,
        current_idx=0,
        score=0
    )
    await message.answer("Начинаем тест по истории! Введите ответ (только число).")
    await message.answer(f"Вопрос 1: {sample_questions[0]['question']}", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Quiz.q_process)

@dp.message(Command("stop"), Quiz.q_process)
async def stop_quiz(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Тест прерван.", reply_markup=get_main_kb())

@dp.message(Quiz.q_process)
async def handle_quiz_answer(message: types.Message, state: FSMContext):
    data = await state.get_data()
    q_list = data['questions']
    idx = data['current_idx']
    score = data['score']
    # Проверяем ответ (убираем лишние пробелы)
    user_answer = message.text.strip()
    correct_answer = q_list[idx]['response']
    if user_answer == correct_answer:
        score += 1
        await message.answer("Верно!")
    else:
        await message.answer(f"Неверно. Правильный ответ: {correct_answer}")
    idx += 1
    # Проверяем, есть ли еще вопросы
    if idx < len(q_list):
        await state.update_data(current_idx=idx, score=score)
        await message.answer(f"Вопрос {idx + 1}: {q_list[idx]['question']}")
    else:
        # Тест окончен
        await message.answer(f"Тест завершен! \nВаш результат: {score} из {len(q_list)}.", reply_markup=get_quiz_retry_kb())
        await state.clear()

#Логика Экскурсии
@dp.message(F.text == "Начать экскурсию")
async def start_museum(message: types.Message, state: FSMContext):
    logger.info(f"User {message.from_user.id} started excursion")
    await message.answer("Добро пожаловать! Пожалуйста, сдайте верхнюю одежду в гардероб!")
    await message.answer("В данном зале (Зал 1) представлены античные статуи.", reply_markup=kb_hall1())
    await state.set_state(Museum.hall1)

@dp.message(Museum.hall1, F.text == "В зал 2 (Средневековье)")
async def to_h2(message: types.Message, state: FSMContext):
    await message.answer("В данном зале представлены рыцарские доспехи.", reply_markup=kb_hall2())
    await state.set_state(Museum.hall2)

@dp.message(Museum.hall2, F.text == "В зал 3 (Новое время)")
async def to_h3(message: types.Message, state: FSMContext):
    await message.answer("В данном зале представлена живопись Ренессанса.", reply_markup=kb_hall3())
    await state.set_state(Museum.hall3)

@dp.message(Museum.hall3, F.text == "В зал 4 (Современность)")
async def to_h4(message: types.Message, state: FSMContext):
    await message.answer("В данном зале представлены современные инсталляции.", reply_markup=kb_hall4())
    await state.set_state(Museum.hall4)

@dp.message(F.text == "Вернуться в зал 1", StateFilter(Museum.hall3, Museum.hall4))
async def back_to_h1(message: types.Message, state: FSMContext):
    await message.answer("Вы вернулись в зал 1 к статуям.", reply_markup=kb_hall1())
    await state.set_state(Museum.hall1)

@dp.message(Museum.hall1, F.text == "Выйти из музея")
async def exit_museum(message: types.Message, state: FSMContext):
    logger.info(f"User {message.from_user.id} left museum")
    await message.answer("Всего доброго, не забудьте забрать верхнюю одежду в гардеробе!", reply_markup=get_main_kb())
    await state.clear()

#Логика выбора
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    logger.info(f"User {message.from_user.id} started the bot")
    await message.answer("Выберите режим:", reply_markup=get_main_kb())

@dp.message(F.text == "/dice")
@dp.message(Command("dice"))
async def dice_menu(message: types.Message):
    logger.info(f"User {message.from_user.id} opened DICE menu")
    await message.answer("Меню кубиков:", reply_markup=get_dice_kb())

@dp.message(F.text == "/timer")
@dp.message(Command("timer"))
async def timer_menu(message: types.Message):
    logger.info(f"User {message.from_user.id} opened TIMER menu")
    await message.answer("Меню таймера:", reply_markup=get_timer_kb())

@dp.message(F.text == "вернуться назад")
async def back(message: types.Message):
    logger.info(f"User {message.from_user.id} returned to main menu")
    await message.answer("Главное меню:", reply_markup=get_main_kb())

# Логика кубиков
@dp.message(F.text == "кинуть один шестигранный кубик")
async def r1(message: types.Message):
    res = random.randint(1, 6)
    logger.info(f"User {message.from_user.id} rolled 1d6. Result: {res}")
    await message.answer(f"Результат: {res}")

@dp.message(F.text == "кинуть 2 шестигранных кубика одновременно")
async def r2(message: types.Message):
    res1, res2 = random.randint(1, 6), random.randint(1, 6)
    logger.info(f"User {message.from_user.id} rolled 2d6. Result: {res1}, {res2}")
    await message.answer(f"Результат: {res1} и {res2}")

@dp.message(F.text == "кинуть 20-гранный кубик")
async def r3(message: types.Message):
    res = random.randint(1, 20)
    logger.info(f"User {message.from_user.id} rolled 1d20. Result: {res}")
    await message.answer(f"Результат: {res}")

# Логика таймера
async def timer_task(message: types.Message, seconds: int, t_str: str):
    try:
        await asyncio.sleep(seconds)
        logger.info(f"Timer for user {message.from_user.id} ({t_str}) finished")
        await message.answer(f"{t_str} истекло", reply_markup=get_timer_kb())
        active_timers.pop(message.from_user.id, None)
    except asyncio.CancelledError:
        logger.info(f"Timer for user {message.from_user.id} was cancelled")

@dp.message(F.text.in_({"30 секунд", "1 минута", "5 минут"}))
async def start_t(message: types.Message):
    tm = {"30 секунд": 30, "1 минута": 60, "5 минут": 300}
    uid = message.from_user.id
    if uid in active_timers: active_timers[uid].cancel()
    logger.info(f"User {uid} started timer for {message.text}")
    await message.answer(f"засек {message.text}", reply_markup=get_close_kb())
    active_timers[uid] = asyncio.create_task(timer_task(message, tm[message.text], message.text))

@dp.message(F.text == "/close")
async def stop_t(message: types.Message):
    uid = message.from_user.id
    if uid in active_timers:
        logger.info(f"User {uid} manually closed timer")
        active_timers[uid].cancel()
        del active_timers[uid]
        await message.answer("Таймер сброшен", reply_markup=get_timer_kb())

#Логика time date 
@dp.message(Command("time"))
@dp.message(F.text == "Время")
async def get_time(message: types.Message):
    current_time = datetime.now().strftime("%H:%M:%S")
    logger.info(f"User {message.from_user.id} requested TIME")
    await message.answer(f"Текущее время: {current_time}")

@dp.message(Command("date"))
@dp.message(F.text == "Дата")
async def get_date(message: types.Message):
    current_date = datetime.now().strftime("%d.%m.%Y")
    logger.info(f"User {message.from_user.id} requested DATE")
    await message.answer(f"Текущая дата: {current_date}")

#Логика эхо
@dp.message()
async def echo_handler(message: types.Message):
    # Хендлер сработает на любое текстовое сообщение,которое не является командой /time или /date.
    if message.text:
        logger.info(f"User {message.from_user.id} sent text: {message.text}")
        await message.answer(f"Я получил сообщение {message.text}")

async def main():
    logger.info("Запуск бота...")
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка: {e}")
    finally:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning("Бот остановлен")