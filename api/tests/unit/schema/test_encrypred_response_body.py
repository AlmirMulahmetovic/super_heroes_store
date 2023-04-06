from unittest.mock import MagicMock, patch

from super_hero.schema import EncryptedHeroResponseBody


class TestCreateHeroRequestBody:
    @patch("deesee_encryption.service.DeeSeeEncryptionService.encrypt_string")
    def test_superpowers_validation_valid_values(self, deesee_encrypt_string_mock):
        identity_mock = MagicMock()
        assert (
            EncryptedHeroResponseBody.encrypt_identity(identity_mock)
            == deesee_encrypt_string_mock.return_value
        )
        deesee_encrypt_string_mock.assert_called_once_with(identity_mock)
