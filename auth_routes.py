from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
    Rota de autenticação
    """
    return {"mensagem": "Rota de autenticação", "status": False}