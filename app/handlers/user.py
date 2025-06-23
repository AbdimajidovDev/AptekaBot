from aiogram import Router, types
from aiogram.types import Message
from sqlalchemy import select

from app.database import AsyncSessionLocal
from app.models.product import Product

user_router = Router()


@user_router.message()
async def search_product(message: Message):
    query = message.text.strip()

    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Product).where(Product.name.ilike(f"%{query}%"))
        )
        product = result.scalars().first() # all()

        if product:
            await message.answer(
                f"🔎 <b>{product.name}</b> mavjud!\n"
                f"💬 {product.description}\n"
                f"💰 Narxi: {product.price} so‘m\n"
                f"📦 Omborda: {product.quantity} dona"
            )
        else:
            await message.answer("Kechirasiz! Bunday dori mavjud emas.")