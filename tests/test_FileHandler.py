import pytest

from src.file_handler.FileHandler import FileHandler

class TestFileHandler:

    @pytest.fixture
    def input_file_path(self):
        return 'data/mesquite_characters_list_example.txt'

    @pytest.fixture
    def output_file_path(self):
        return None

    @pytest.fixture
    def input_data_treated(self):
        input_data_treated = ['1. Frons, median carina', '0 absent', '1 present', '2. Frons, sublateral carinae', '0 absent', '1 present', '3. Frons, median ocelli', '0 present', '1 absent', '4. Frons, lateral ocelli', '0 absent', '1 present', '5. Vertex, median carina', '0 present', '1 absent', '6. Clypeus, median carina', '0 absent', '1 present', '7. Clypeus, lateral carinae', '0 present', '1 absent', '8. Pronotum, median carina', '0 present', '1 absent', '9. Pronotum, lateral carinae', '0 present', '1 absent', '10. Pronotum, lateral carinae, extension related to hind margin', '0 reach', '1 do not reach', '11. Mesonotum, median carina', '0 absent', '1 present', '12. Mesonotum, lateral carinae', '0 present', '1 absent', '13. Forewing, venation, granule', '0 present', '1 absent', '14. Forewing, venation, granule, setae', '0 present', '1 absent', '15. Leg III, tibia, basal spine', '0 present', '1 absent', '16. Leg III, tibia, lateral spine', '0 absent', '1 present', '17. Leg III, tibia, lateral spine, number', '0 more than one', '1 one', '18. Leg III, tibia, apical spines, quantity', '0 five (regular)', '1 five (3+2)', '2 seven (5+2)', '19. Leg III, tibia, apical movable spur (calcar)', '0 absent', '1 present', '20. Leg III, tibia, calcar, shape', '0 spine-like', '1 flattened', '2 tectiform', '21. Leg III, tibia, calcar, hind margin, teeth', '0 present', '1 absent', '22. Leg III, tibia, calcar, apical teeth', '0 present', '1 absent', '23. Pygofer, dorsolateral processes', '0 absent', '1 present', '24. Pygofer, caudal margin, middle portion, extended caudally', '0 absent', '1 present', '25. Pygofer, midlateral processes', '0 absent', '1 present', '26. Pygofer, caudal margin, ventral portion, strongly extended caudally', '0 absent', '1 present', '27. Pygofer, lateroventral processes', '0 absent', '1 present', '28. Pygofer, midventral process', '0 absent', '1 present', '29. Pygofer, midventral process, type', '0 unique', '1 bifid', '30. Gonostylus, caudal apex, shape', '0 hammer-like', '1 finger-like', '2 bifid', '31. Anal tube, ventral process', '0 present', '1 absent', '32. Anal tube, ventral process', '0 bifid', '1 single']
        return input_data_treated

    def test_open_input_file(input_file_path, input_data_treated):
        input_data = FileHandler.open_input_file(input_file_path)
        assert input_data == input_data_treated
    
    def test_save_output_file(self):
        ...