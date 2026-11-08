"""
Tests for OCA types and enums.
"""
import pytest
from aes70.types.enum import Enum


class TestEnum:
    """Test the Enum factory function."""

    def test_enum_creation(self):
        """Test basic enum creation."""
        TestEnum = Enum({
            'Value1': 1,
            'Value2': 2,
            'Value3': 3,
        })
        assert TestEnum is not None
        # isEnum is an instance property, test on an instance
        assert TestEnum.Value1.isEnum is True

    def test_enum_value_access(self):
        """Test accessing enum values."""
        StatusEnum = Enum({
            'Off': 0,
            'On': 1,
        })
        off_value = StatusEnum.Off
        on_value = StatusEnum.On
        assert off_value.value == 0
        assert on_value.value == 1

    def test_enum_name_property(self):
        """Test enum name property."""
        ColorEnum = Enum({
            'Red': 1,
            'Green': 2,
            'Blue': 3,
        })
        red = ColorEnum.Red
        assert red.name == 'Red'
        assert str(red) == 'Red'

    def test_enum_from_string(self):
        """Test creating enum from string name."""
        DirectionEnum = Enum({
            'North': 1,
            'South': 2,
        })
        north = DirectionEnum('North')
        assert north.value == 1
        assert north.name == 'North'

    def test_enum_invalid_string_raises(self):
        """Test that invalid enum name raises exception."""
        TestEnum = Enum({'Valid': 1})
        with pytest.raises(Exception):
            TestEnum('Invalid')

    def test_enum_getName(self):
        """Test static getName method."""
        TestEnum = Enum({
            'Alpha': 1,
            'Beta': 2,
        })
        assert TestEnum.getName(1) == 'Alpha'
        assert TestEnum.getName(2) == 'Beta'

    def test_enum_getName_invalid_raises(self):
        """Test that getName with invalid value raises exception."""
        TestEnum = Enum({'Valid': 1})
        with pytest.raises(Exception):
            TestEnum.getName(999)

    def test_enum_getValue(self):
        """Test static getValue method."""
        TestEnum = Enum({
            'First': 10,
            'Second': 20,
        })
        assert TestEnum.getValue('First') == 10
        assert TestEnum.getValue('Second') == 20

    def test_enum_getValue_invalid_raises(self):
        """Test that getValue with invalid name raises exception."""
        TestEnum = Enum({'Valid': 1})
        with pytest.raises(Exception):
            TestEnum.getValue('Invalid')

    def test_enum_values(self):
        """Test values() method returns original dict."""
        original = {'A': 1, 'B': 2}
        TestEnum = Enum(original)
        assert TestEnum.values() == original

    def test_enum_singleton_behavior(self):
        """Test that same value returns same instance."""
        TestEnum = Enum({'Same': 1})
        instance1 = TestEnum(1)
        instance2 = TestEnum(1)
        assert instance1 is instance2

    def test_enum_instance_equality(self):
        """Test enum instance equality."""
        TestEnum = Enum({'Value': 42})
        val1 = TestEnum(42)
        val2 = TestEnum(42)
        assert val1.value == val2.value
        assert val1.name == val2.name


class TestOcaTypesImport:
    """Test that OCA type modules can be imported."""

    def test_import_mute_state(self):
        """Test OcaMuteState type imports."""
        from aes70.types.ocamutestate import OcaMuteState
        assert OcaMuteState is not None
        assert OcaMuteState.Muted.value == 1
        assert OcaMuteState.Unmuted.value == 2

    def test_import_class_identification(self):
        """Test OcaClassIdentification type imports."""
        from aes70.types.ocaclassidentification import OcaClassIdentification
        assert OcaClassIdentification is not None

    def test_import_model_description(self):
        """Test OcaModelDescription type imports."""
        from aes70.types.ocamodeldescription import OcaModelDescription
        assert OcaModelDescription is not None

    def test_import_property_id(self):
        """Test OcaPropertyID type imports."""
        from aes70.types.ocapropertyid import OcaPropertyID
        assert OcaPropertyID is not None


class TestOcaStructs:
    """Test OCA struct types."""

    def test_class_identification_instantiation(self):
        """Test OcaClassIdentification can be created."""
        from aes70.types.ocaclassidentification import OcaClassIdentification

        class_id = [1, 2, 3]
        ident = OcaClassIdentification(class_id, 1)
        assert ident is not None
        assert ident.ClassID == class_id
        assert ident.ClassVersion == 1

    def test_model_description_instantiation(self):
        """Test OcaModelDescription can be created."""
        from aes70.types.ocamodeldescription import OcaModelDescription

        desc = OcaModelDescription(
            Manufacturer="Test Manufacturer",
            Name="Test Device",
            Version="1.0.0"
        )
        assert desc is not None
        assert desc.Manufacturer == "Test Manufacturer"
        assert desc.Name == "Test Device"
        assert desc.Version == "1.0.0"
