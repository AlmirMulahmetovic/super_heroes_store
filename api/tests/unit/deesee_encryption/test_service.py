from deesee_encryption.service import DeeSeeEncryptionService


class TestDeeSeeEncryptionService:
    def test_encrypt_string(self):
        assert DeeSeeEncryptionService.encrypt_string("clark kent") == "hqfwp pjsy"
