from dataclasses import dataclass

import numpy.matrixlib
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


@router.get('/matrices')
def matrices() -> dict:
    matrix_a = numpy.random.randint(-10, 10, (10, 10)).tolist()
    matrix_b = numpy.random.randint(-10, 10, (10, 10)).tolist()
    product = (numpy.dot(matrix_a, matrix_b)).tolist()

    return {
        "matrix_a": matrix_a,
        "matrix_b": matrix_b,
        "product": product,
    }
