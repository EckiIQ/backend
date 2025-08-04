from fastapi import APIRouter, HTTPException, status

from app.api.dependencies import ServiceDep
from app.api.schemas.shipment import ShipmentCreate, ShipmentUpdate
from app.database.models import Shipment


router = APIRouter()


###  a shipment by id
@router.get("/shipment", response_model=Shipment)
async def get_shipment(id: int, service: ServiceDep):
    # Check for shipment with given id
    shipment = await service.get(id)  

    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!",
        )

    return shipment


### Create a new shipment with content and weight
@router.post("/shipment")
async def submit_shipment(shipment: ShipmentCreate, service: ServiceDep) -> Shipment:
    return await service.add(shipment)


### Update fields of a shipment
@router.patch("/shipment", response_model=Shipment)
async def update_shipment(id: int, shipment_update: ShipmentUpdate, service: ServiceDep):
    # Update data with given fields
    update = shipment_update.model_dump(exclude_none=True)

    if not update:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields to update provided.",
        )
    
    shipment = await service.update(id, shipment_update)  # type: ignore
    return shipment


### Delete a shipment by id
@router.delete("/shipment")
async def delete_shipment(id: int, service: ServiceDep) -> dict[str, str]:
    await service.delete(id)

    return {"detail": f"Shipment with id #{id} is deleted!"}
