from client_service import ClientService
from json_serializer import JsonSerializer
from xml_serializer import Xmlserializer
from test_class import TestClass
from not_supported_exception import NotSupportedException

format_type = 'xml'
path_to_data = "c:\\my_test.txt"

if __name__ == "__main__":
    serializer = None
    if format_type == 'json':
        serializer = JsonSerializer()
    elif format_type == 'xml':
        serializer = Xmlserializer()
    else:
        raise NotSupportedException(
            f'The {format_type} format type is not supported')

    test_instance = TestClass(prop1="property 1", prop2="property 2")
    client_service = ClientService(serializer=serializer)
    client_service.process(file_path=path_to_data, object=test_instance)
