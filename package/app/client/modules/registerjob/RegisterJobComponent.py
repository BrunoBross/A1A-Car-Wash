from package.app.api.modules.job.JobController import JobController
from package.app.client.dialog.DialogService import DialogService
from package.app.client.dialog.InfoBox import InfoBoxProps
from package.app.client.gui.box.Box import Box
from package.app.client.modules.registerjob.RegisterJobValidator import (
    RegisterJobValidator,
)
from package.app.client.dialog.Modal import ModalProps
from package.app.client.state.ComponentState import ComponentState
from package.app.meta.Singleton import Singleton
from package.app.client.utils.form import getEntryBuffer
from package.app.api.modules.job.dto.JobDto import JobDto
from package.app.client.gui.imports import Gtk
from package.app.validation.IValidator import IValidator
from package.app.exception.DatabaseIntegrityException import DatabaseIntegrityException


class RegisterJobComponent(metaclass=Singleton):
    def __init__(self):
        self.__state = ComponentState()
        self.__validator: IValidator = RegisterJobValidator()
        self.__controller = JobController()
        self.__dialogService = DialogService()

    def requestRegister(self):
        description = getEntryBuffer(self.__state.getReferenceById("jobName"))
        cost_value = getEntryBuffer(self.__state.getReferenceById("jobValue"))

        try:
            dto = JobDto(
                description=description.upper(),
                cost_value=float(cost_value),
            )

        except ValueError:
            if cost_value == "":
                dto = JobDto(
                    description=description.upper(),
                    cost_value=0,
                )
            else:
                dto = JobDto(
                    description=description.upper(),
                    cost_value="invalid_cost",
                )

        if self.__validator.execute(dto, False):
            entity = self.__controller.registerJob(dto)
            if entity:
                self.__displaySuccessMessage("Serviço cadastrado com sucesso", "Cadastro bem sucedido")

    def requestEdit(self, job: list):
        if job is None:
            self.__displaySuccessMessage("Nenhum serviço selecionado", "Erro")
            return

        job_id = job[0]

        description = getEntryBuffer(self.__state.getReferenceById("jobName"))
        cost_value = getEntryBuffer(self.__state.getReferenceById("jobValue"))

        try:
            dto = JobDto(
                description=description.upper(),
                cost_value=float(cost_value),
            )
            
        except ValueError:
            if cost_value == "":
                dto = JobDto(
                    description=description.upper(),
                    cost_value=0,
                )
            else:
                dto = JobDto(
                    description=description.upper(),
                    cost_value="invalid_cost",
                )

        if self.__validator.execute(dto, True):
            if self.__displayConfirmBox(job, "editar"):
                try:
                    self.__controller.editJob(jobDto=dto, jobId=job_id)
                    return self.__displaySuccessMessage("Serviço editado com sucesso", "Edição bem sucedida")
                except DatabaseIntegrityException as e:
                    print(e)
                    return self.__displaySuccessMessage("Erro na edição, tente novamente", "Erro")
            else:
                return

    def requestDelete(self, job: list):
        job_id = job[0]
        if self.__displayConfirmBox(job, "deletar"):
            try:
                if self.__controller.deleteJob(job_id):
                    return self.__displaySuccessMessage("Serviço deletado com sucesso", "Deleção bem sucedida")
                return self.__displaySuccessMessage("O serviço possui agendamentos cadastrados", "Erro")
            except DatabaseIntegrityException as e:
                print(e)
                return self.__displaySuccessMessage("Erro na deleção, tente novamente", "Erro")
        else:
            return

    def getState(self) -> ComponentState:
        return self.__state

    def getJobList(self):
        jobs = self.__controller.getJobs()
        jobList = []
        for job in jobs:
            jobList.append([job.id, job.description, f'R${job.cost_value}'])
        return jobList

    def __displaySuccessMessage(self, message: str, title_message: str):
        content = Box()
        content.pack_default(Gtk.Label(message))
        self.__dialogService.displayInfoBox(
            InfoBoxProps(title=title_message, content=content)
        )

    def __displayConfirmBox(self, job: list, label: str):
        content = Box()
        content.pack_default(Gtk.Label(f"Tem certeza que você deseja {label} o serviço {job[1]}?"))
        return self.__dialogService.displayModal(
            ModalProps(title="Confirmação", content=content, cancelLabel="Cancelar", okLabel="Confirmar")
        )
