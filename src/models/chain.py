from pydantic import BaseModel


class SingleChain(BaseModel):
    name: str
    id: int


class AllChains(BaseModel):
    chains: list[SingleChain]
