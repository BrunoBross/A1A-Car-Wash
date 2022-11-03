from package.app.api.modules.job.JobController import JobController
from package.app.client.dialog.DialogService import DialogService
from package.app.client.dialog.InfoBox import InfoBoxProps
from package.app.client.gui.box.Box import Box
from package.app.client.modules.registerjob.RegisterJobValidator import (
    RegisterJobValidator,
)
from package.app.client.state.ComponentState import ComponentState
from package.app.meta.Singleton import Singleton
from package.app.client.utils.form import getEntryBuffer
from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.client.gui.imports import Gtk
from package.app.validation.IValidator import IValidator


class RegisterJobComponent(metaclass=Singleton):
    def __init__(self):
        self.__state = ComponentState()
        self.__validator: IValidator = RegisterJobValidator()
        self.__controller = JobController()
        self.__dialogService = DialogService()

    def requestRegistration(self):

        description = getEntryBuffer(self.__state.getReferenceById("jobName"))
        cost_value = getEntryBuffer(self.__state.getReferenceById("jobValue"))

        dto = JobDto(
            description=description.upper(),
            cost_value=float((cost_value) if bool(cost_value) else 0),
        )

        if self.__validator.execute(dto):
            entity = self.__controller.registerJob(dto)
            if entity:
                self.__displaySuccessMessage()

    def getState(self) -> ComponentState:
        return self.__state

    def __displaySuccessMessage(self):
        content = Box()
        content.pack_default(Gtk.Label("Serviço cadastrado com sucesso"))
        self.__dialogService.displayInfoBox(
            InfoBoxProps(title="Cadastro bem sucedido", content=content)
        )
