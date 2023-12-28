from fastapi import APIRouter , Path , Query
from converter import sync_converter, async_converter
from asyncio import gather

router = APIRouter(prefix="/converter")

@router.get('/sync/{from_currency}')
def converter(from_currency: str = Path(regex='^[A-Z]{3}$'),
              to_currenies: str = Query(regex='^[A-Z]{3}(,[A-Z]{3})*$'),
              price: float = Query(gt=0)
):
    to_currenies = to_currenies.split(',')
    result =  []

    for courrency in to_currenies:
        response = sync_converter(
            from_currency=from_currency,
            to_currency=courrency, 
            price=price)

        result.append(response)

    return result


@router.get('/async/{from_currency}')
async def async_converter_router(from_currency: str = Path(regex='^[A-Z]{3}$'),
              to_currenies: str = Query(regex='^[A-Z]{3}(,[A-Z]{3})*$'),
              price: float = Query(gt=0)
):
    to_currenies = to_currenies.split(',')
    courotines =  []

    for courotine in to_currenies:
        coro = async_converter(
            from_currency=from_currency,
            to_currency=courotine,
              price=price)

        courotines.append(coro)
    result = await gather(*courotines)
    return result


    return result