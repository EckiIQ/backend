from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession


from app.api.schemas.shipment import ShipmentCreate
from app.database.models import Shipment, ShipmentStatus


class ShipmentService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, id: int) -> Shipment:
        return await self.sesssion.get(Shipment, id) # type: ignore

    async def add(self, shipment_create: ShipmentCreate) -> Shipment: # type: ignore
        new_shipment = Shipment(
            **shipment_create.model_dump(),
            status=ShipmentStatus.placed,
            estimated_delivery=datetime.now() + timedelta(days=3)  # Example estimated delivery
        )
        self.session.add(new_shipment) # type: ignore
        await self.session.commit() # type: ignore
        await self.session.refresh(new_shipment) # type: ignore

        return new_shipment

    async def update(self, id: int, shipment_update: Shipment) -> Shipment: # type: ignore
        shipment = await self.get(id)
        shipment.sqlmodel_update(shipment_update) # type: ignore
        
        self.session.add(shipment) # type: ignore
        await self.session.commit() # type: ignore
        await self.session.refresh(shipment) # type: ignore

        return shipment # type: ignore
    
    async def delete(self, id: int) -> None: # type: ignore
        await self.session.delete(await self.get(id))
        await self.session.commit() # type: ignore

