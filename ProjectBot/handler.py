from aiogram import  Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hbold
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import ContentType
import pickle
from sklearn.ensemble import RandomForestRegressor
import numpy as np

router = Router()

with open('RFR_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)


with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)



class Req(StatesGroup):
    matrix = State()
    density = State()
    mod_upr = State()
    amount_hard = State()
    epoxy = State()
    flash_point = State()
    surf_density = State()
    tens_mod = State()
    resin_cons = State()
    patch_angle = State()
    parch_pitch = State()
    parch_density = State()


# Функция для предсказания на основе данных
def predict_from_model(data):
    prediction = loaded_model.predict([data])[0]
    return prediction


@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!")
    await message.answer('Я бот, который может предсказать-Прочность при растяжении, МПа')


@router.message(Command('help'))
async def command_help(message: Message):
    await message.answer("Команда help")


@router.message(Command('req'))
async def req_one(massage: Message, state: FSMContext):
    await state.set_state(Req.matrix)
    await massage.answer('Введите:\n'
                         '-Соотношение матрица-наполнитель\n'
                         '-Плотность, кг/м3\n'
                         '-Модуль упругости, ГПа\n'
                         '-Количество отвердителя, м.%\n'
                         '-Содержание эпоксидных групп,%_2\n'
                         '-Температура вспышки, С^2\n'
                         '-Поверхностная плотность, г/м2\n'
                         '-Модуль упругости при растяжении\n'
                         '-Потребление смолы, г/м2\n'
                         '-Угол нашивки, град\n'
                         '-Шаг нашивки\n'
                         '-Плотность нашивки')
    await massage.answer('Ведите Данные через запятую!!!!')

#
# @router.message(Req.matrix)
# async def req_two(massage: Message, state: FSMContext):
#     await state.update_data(matrix=massage.text)
#     await state.set_state(Req.density)
#     await massage.answer('Введите Плотность, кг/м3')
#
#
# @router.message(Req.density)
# async def req_three(massage: Message, state: FSMContext):
#     await state.update_data(density=massage.text)
#     await state.set_state(Req.mod_upr)
#     await massage.answer('Введите Модуль упругости, ГПа')
#
#
# @router.message(Req.mod_upr)
# async def req_three(massage: Message, state: FSMContext):
#     await state.update_data(mod_upr=massage.text)
#     await state.set_state(Req.amount_hard)
#     await massage.answer('Количество отвердителя, м.%')
#
#
# @router.message(Req.amount_hard)
# async def req_three(massage: Message, state: FSMContext):
#     await state.update_data(amount_hard=massage.text)
#     await state.set_state(Req.epoxy)
#     await massage.answer('Содержание эпоксидных групп,%_2')
#
#
# @router.message(Req.epoxy)
# async def req_three(massage: Message, state: FSMContext):
#     await state.update_data(epoxy=massage.text)
#     await state.set_state(Req.flash_point)
#     await massage.answer('Температура вспышки, С^2')
#
#
# @router.message(Req.flash_point)
# async def req_three(massage: Message, state: FSMContext):
#     await state.update_data(flash_point=massage.text)
#     await state.set_state(Req.surf_density)
#     await massage.answer('Поверхностная плотность, г/м2')
#
#
# @router.message(Req.surf_density)
# async def req_three(massage: Message, state: FSMContext):
#     await state.update_data(surf_density=massage.text)
#     await state.set_state(Req.tens_mod)
#     await massage.answer('Модуль упругости при растяжении, ГПа')
#
#
# @router.message(Req.tens_mod)
# async def req_three(massage: Message, state: FSMContext):
#     await state.update_data(tens_mod=massage.text)
#     await state.set_state(Req.resin_cons)
#     await massage.answer('Потребление смолы, г/м2')
#
#
# @router.message(Req.resin_cons)
# async def req_three(massage: Message, state: FSMContext):
#     await state.update_data(resin_cons=massage.text)
#     await state.set_state(Req.patch_angle)
#     await massage.answer('Угол нашивки, град.')
#
#
# @router.message(Req.patch_angle)
# async def req_three(massage: Message, state: FSMContext):
#     await state.update_data(patch_angle=massage.text)
#     await state.set_state(Req.parch_pitch)
#     await massage.answer('Шаг нашивки')
#
#
# @router.message(Req.parch_pitch)
# async def req_three(massage: Message, state: FSMContext):
#     await state.update_data(parch_pitch=massage.text)
#     await state.set_state(Req.parch_density)
#     await massage.answer('Плотность нашивки')
#
#
# @router.message(Req.parch_density)
# async def req_three(massage: Message, state: FSMContext):
#     await state.update_data(parch_density=massage.text)
#     data = await state.get_data()
#     Bot_handler = 1427.915063555448
#     data = await state.get_data()
#     #numbers = [float(num) for num in data["matrix"].split(',')]
#     #print(numbers, "numbers", type(numbers))
#     prediction = predict_from_model(data)
#     await massage.answer(f"Предсказание модели: {Bot_handler / prediction}")
#     await massage.answer(f'Спасибо, вы ввели:\n {data["matrix"]}\n {data["density"]}\n {data["mod_upr"]}\n {data["amount_hard"]}\n'
#                          f' {data["epoxy"]}\n {data["flash_point"]}\n {data["surf_density"]}\n {data["tens_mod"]}\n'
#                          f' {data["resin_cons"]}\n {data["patch_angle"]}\n {data["parch_pitch"]}\n {data["parch_density"]}')
#
#     await state.clear()

@router.message(Req.matrix)
async def req_three(massage: Message, state: FSMContext):
    await state.update_data(matrix=massage.text)
    Bot_handler = 1427.915063555448
    data = await state.get_data()
    numbers = [float(num) for num in data["matrix"].split(',')]
    print(numbers, "numbers", type(numbers))
    prediction = predict_from_model(numbers)
    await massage.answer(f"Предсказание модели: {Bot_handler/prediction}")
    await massage.answer(
        f'Спасибо, вы ввели:\n Соотношение матрица-наполнитель:{numbers[0]}\n Плотность, кг/м3:{numbers[1]}\n Модуль упругости, ГПа:{numbers[2]}\n Количество отвердителя, м.%:{numbers[3]}\n'
                              f'Содержание эпоксидных групп,%_2:{numbers[4]}\n Температура вспышки, С^2:{numbers[5]}\n Поверхностная плотность, г/м2:{numbers[6]}\n Модуль упругости при растяжении:{numbers[7]}\n'
                              f' Потребление смолы, г/м2:{numbers[8]}\n Угол нашивки, град:{numbers[9]}\n Шаг нашивки:{numbers[10]}\n Плотность нашивки:{numbers[11]}')
    await state.clear()
