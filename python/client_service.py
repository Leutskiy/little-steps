from pathlib import Path
from iserializer import ISerializer


class ClientService:
    '''
    Класс, который является клиентом стратегии
    '''
    def __init__(self, serializer: ISerializer) -> None:
        self.__serializer = serializer

    def process(self, file_path: Path, object: object) -> None:
        """
        Метод, который обрабатывает даннные переданного файла

        :param file_path: Полное наименование файла
        :type Path: pathlib.Path, обязательный

        """

        with open(str(file_path), 'w') as file_writer:
            serialized_data = self.__serializer.serialize(object=object)
            file_writer.write(serialized_data)
