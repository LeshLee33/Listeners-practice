from operations import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

api = FastAPI(title="Listeners")
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
api.include_router(router=router)


def main():
    uvicorn.run("main:api", reload=True)


if __name__ == "__main__":
    main()
