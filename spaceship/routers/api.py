from dataclasses import dataclass

from fastapi import APIRouter

router = APIRouter()


@dataclass
class EchoDto:
    text: str


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.post('')
def echo(dto: EchoDto) -> dict:
    return {'msg': dto.text}
