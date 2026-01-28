from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/lista") # Rota para listar todos os pedidos
async def pedidos():
    """
    Rota de pedidos: Todas as rotas de pedidos precisam de autenticação
    """
    return {"mensagem": "Rota de pedidos: Todas as rotas de pedidos precisam de autenticação", "status": False}