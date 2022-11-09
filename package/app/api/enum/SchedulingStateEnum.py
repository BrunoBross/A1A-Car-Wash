from enum import Enum


class SchedulingStateEnum(Enum):
    PENDENTE = 1
    FINALIZADO = 2
    CLIENTE_AUSENTE = 3
    EQUIPAMENTO_COM_DEFEITO = 4
