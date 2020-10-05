import json
from iserializer import ISerializer


class JsonSerializer(ISerializer):
    '''
    Сериализатор в формат JSON

    '''
    def __init__(self) -> None:
        super().__init__()

    def serialize(self, object: object) -> str:
        """
        Сериализует объект в JSON-строку

        :param object: Сериализуемый объект
        :type object: object
        :return: строка в формате JSON
        :rtype: str
        """

        json_string = json.dumps(object.__dict__, indent="    ")

        return json_string
