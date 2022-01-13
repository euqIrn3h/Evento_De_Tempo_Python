import time
import asyncio

async def event_second() -> bool:
    segundoanterior = time.strftime("%X")[6:]
    while True:
        if segundoanterior != time.strftime("%X")[6:]:
            segundoanterior = time.strftime("%X")[6:]
            return True
        
        await asyncio.sleep(0.1)

async def event_minute() -> bool:
    while True:
        if time.strftime("%X")[6:] == '00':
            return True
        await asyncio.sleep(1)

async def event_hour() -> bool:
    while True:
        if time.strftime("%X")[3:5] == '00':
            return True
        await asyncio.sleep(1)
    

#para utilizar o módulo é necessário colocá-lo em um loop infinito
#While True:
# asyncio.run( FUNCAO )



