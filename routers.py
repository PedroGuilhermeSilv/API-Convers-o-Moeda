from fastapi import APIRouter , Path , Query 
from converter import sync_converter, async_converter
from asyncio import gather
from schemas import ConverterInput, ConverterOutput

router = APIRouter(prefix="/converter")

@router.get('/sync/{from_currency}')
def converter(body: ConverterInput,from_currency: str = Path(regex='^[A-Z]{3}$')
):
    to_currenies = body.to_currenies
    price = body.price
    result =  []

    for courrency in to_currenies:
        response = sync_converter(
            from_currency=from_currency,
            to_currency=courrency, 
            price=price)

        result.append(response)

    return result


@router.get('/async/{from_currency}', response_model=ConverterOutput)
async def async_converter_router(body: ConverterInput,from_currency: str = Path(regex='^[A-Z]{3}$')
):
    to_currenies = body.to_currenies
    price = body.price
    courotines =  []

    for courotine in to_currenies:
        coro = async_converter(
            from_currency=from_currency,
            to_currency=courotine,
              price=price)

        courotines.append(coro)
    result = await gather(*courotines)
    return ConverterOutput(
        message="Sucessse",
        data=result
    )

