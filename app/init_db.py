import asyncio
from app.database import engine, AsyncSessionLocal
from app.models.product import Base, Product


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as session:
        aspirin = Product(
            name="Aspirin",
            description="Og‘riq qoldiruvchi",
            price=4500,
            quantity=50
        )
        session.add(aspirin)
        await session.commit()

if __name__ == '__main__':
    asyncio.run(init_models())
