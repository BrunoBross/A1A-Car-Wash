from package.app.api.modules.service.serviceController import ServiceController
from package.app.client.state.ComponentState import ComponentState
from package.app.meta.Singleton import Singleton
from package.app.client.utils.form import getEntryBuffer
from package.app.api.modules.service.dto.serviceDto import ServiceDto


class ServiceRegistrationComponent(metaclass=Singleton):
    def __init__(self):
        self.__serviceRegistrationController = ServiceController()
        self.__state = ComponentState()

    def getText(self) -> str:
        return self.__serviceRegistrationController.getExampleInfo()

    def serviceRegistration(self):
        """ service_name = getEntryBuffer(self.__state.getReferenceById("service_name"))
        price = getEntryBuffer(self.__state.getReferenceById("price")) """

        dto = ServiceDto(
            description=getEntryBuffer(self.__state.getReferenceById("service_name")),
            cost_value=getEntryBuffer(self.__state.getReferenceById("price"))
        )

        if dto.description == '' or dto.cost_value == '':
            return print('Preencha todos os campos!')
        if not dto.cost_value.isnumeric():
            return print('O campo preço deve conter um valor numérico!')
        try:
            self.__serviceRegistrationController.serviceRegistrastion(dto.description, dto.cost_value)
            print(f'Serviço {dto.description} cadastrado com sucesso')
        except Exception as error:
            print(error)

    def getState(self) -> ComponentState:
        return self.__state