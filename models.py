from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType


# cria a conexão do banco de dados
db = create_engine("sqlite:///banco.db")

# cria a base para os modelos
Base = declarative_base()

#cria as classes dos modelos
# Usuario
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column("id",Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, unique=True, index=True, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome: str, email: str, senha: str, ativo: bool = True, admin: bool = False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

# Pedido
class Pedido(Base):
    __tablename__ = "pedidos"

    #STATUS_PEDIDOS = (
    #    ("PENDENTE", "PENDENTE"),
    #    ("CANCELADO", "CANCELADO"),
    #    ("FINALIZADO", "FINALIZADO"),
    #)

    id = Column("id", Integer, primary_key=True, autoincrement=True, index=True)
    usuario = Column("usuario", Integer, ForeignKey("usuarios.id"), nullable=False)
    preco = Column("preco", Float, nullable=False)
    status = Column("status", String, nullable=False, default="PENDENTE") #pendente/cancelado/finalizado

    def __init__(self, usuario: int, preco: float = 0, status: str = "PENDENTE"):
        self.usuario = usuario
        self.preco = preco 
        self.status = status

# ItemPedido
class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True, index=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", Integer, ForeignKey("pedidos.id"))

    def __init__(self, quantidade: int, sabor: str, tamanho: str, preco_unitario: float, pedido: int):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido
# executa a criação dos metadados do seu banco(cria efetivamente o banco de dados)
