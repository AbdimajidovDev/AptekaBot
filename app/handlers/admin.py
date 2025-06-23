from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.models.product import Product
from app.database import AsyncSessionLocal
from app.config import ADMIN_ID

admin_router = Router()

@admin_router.message(Command("add_product"))
async def start_add_product(message: Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("Sizning huquqingiz yo'q!")
    await message.answer("Dori nomini kiriting:")
    await state.set_state(ProductForm.name)


class ProductForm(StatesGroup):
    name = State()
    description = State()
    price = State()
    quantity = State()


@admin_router.message(ProductForm.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Description: ")
    await state.set_state(ProductForm.description)

@admin_router.message(ProductForm.description)
async def get_description(message: Message, state: FSMContext):
    await state.update_data(desciption=message.text)
    await message.answer("Narxini kiriting: ")
    await state.set_state(ProductForm.price)

@admin_router.message(ProductForm.price)
async def get_price(message: Message, state: FSMContext):
    try:
        await state.update_data(price=message.text)
        await message.answer("Miqdorini kiriting: ")
        await state.set_state(ProductForm.quantity)
    except ValueError:
        await message.answer("Narx noto'g'ri: ", parse_mode="Markdown")

@admin_router.message(ProductForm.quantity)
async def get_quantity(message: Message, state: FSMContext):
    try:
        quantity = int(message.text)
        data = await state.get_data()

        product = Product(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=quantity
        )

        async with AsyncSessionLocal() as session:
            session.add(product)
            await session.commit()

        await message.answer("Mahsulot muvafaqiyatli qo'shildi!")
        await state.clear()
    except ValueError:
        await message.answer("Miqdor noto'g'ri. Butun son kiriting!")

# from aiogram import Router, F
# from aiogram.types import Message
# from aiogram.filters import Command
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext
#
# from app.models.product import Product
# from app.database import AsyncSessionLocal
# from app.config import ADMIN_ID
#
# admin_router = Router()
#
#
# class ProductForm(StatesGroup):
#     name = State()
#     description = State()
#     price = State()
#     quantity = State()
#
#
# @admin_router.message(Command("add_product"))
# async def start_add_product(message: Message, state: FSMContext):
#     if message.from_user.id != ADMIN_ID:
#         return await message.answer("❌ Sizda bu amalni bajarish huquqi yo‘q.")
#     await message.answer("📝 Dori nomini kiriting:")
#     await state.set_state(ProductForm.name)
#
#
# @admin_router.message(ProductForm.name)
# async def get_name(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await message.answer("💬 Tavsifini kiriting:")
#     await state.set_state(ProductForm.description)
#
#
# @admin_router.message(ProductForm.description)
# async def get_description(message: Message, state: FSMContext):
#     await state.update_data(description=message.text)
#     await message.answer("💰 Narxini kiriting (so‘mda):")
#     await state.set_state(ProductForm.price)
#
#
# @admin_router.message(ProductForm.price)
# async def get_price(message: Message, state: FSMContext):
#     try:
#         price = float(message.text)
#         await state.update_data(price=price)
#         await message.answer("📦 Miqdorini kiriting:")
#         await state.set_state(ProductForm.quantity)
#     except ValueError:
#         await message.answer("❌ Narx noto‘g‘ri. Raqam kiriting.")
#
#
# @admin_router.message(ProductForm.quantity)
# async def get_quantity(message: Message, state: FSMContext):
#     try:
#         quantity = int(message.text)
#         data = await state.get_data()
#
#         product = Product(
#             name=data["name"],
#             description=data["description"],
#             price=data["price"],
#             quantity=quantity
#         )
#
#         async with AsyncSessionLocal() as session:
#             session.add(product)
#             await session.commit()
#
#         await message.answer("✅ Mahsulot muvaffaqiyatli qo‘shildi!")
#         await state.clear()
#     except ValueError:
#         await message.answer("❌ Miqdor noto‘g‘ri. Butun son kiriting.")
