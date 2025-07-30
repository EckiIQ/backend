from datetime import datetime
from enum import Enum
from sqlmodel import SQLModel, Field

class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"

class Shipment(SQLModel, table=True):
    __tablename__ = "shipment" # type: ignore

    id: int = Field(default=None, primary_key=True)
    content: str
    weight: float = Field(le=25)
    status: ShipmentStatus
    destination: int
    estimated_delivery: datetime
