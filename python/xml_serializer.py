from dict2xml import dict2xml
from iserializer import ISerializer


class Xmlserializer(ISerializer):
    '''
    Сериализатор объектов в формат xml
    '''
    def serialize(self, object: object) -> str:
        """
        Сериализует объект в формате xml

        :param object: Сериализуемый объект
        :type object: object
        :return: строка в формате xml
        :rtype: object
        """

        xml_string = dict2xml(object.__dict__, wrap="all", indent="    ")

        return xml_string
