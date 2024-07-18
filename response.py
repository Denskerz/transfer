from fastapi import FastAPI
import asyncio

app = FastAPI()

# Определяем глобальные переменные, которые будут использоваться в приложении
global_variable1 = None
global_variable2 = None

@app.on_event("startup")
async def startup_event():
    # Инициализируем глобальные переменные в фоновой задаче
    await initialize_global_variables()

async def initialize_global_variables():
    global global_variable1, global_variable2

    # Здесь вы можете выполнить любую необходимую логику для инициализации переменных
    global_variable1 = "Значение 1"
    global_variable2 = "Значение 2"

    print("Глобальные переменные инициализированы")

# Теперь вы можете использовать global_variable1 и global_variable2 в ваших маршрутах
@app.get("/")
def root():
    return {
        "global_variable1": global_variable1,
        "global_variable2": global_variable2
    }
