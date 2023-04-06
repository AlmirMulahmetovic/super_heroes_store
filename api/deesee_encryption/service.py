from config.app_config import app_config


class DeeSeeEncryptionService:
    @staticmethod
    def _encrypt_character(character: str) -> str:
        return chr(
            new_char_ascii
            if (new_char_ascii := ord(character) + app_config.ENCRYPTION_KEY) <= ord("z")
            else new_char_ascii - ord("z") + ord("a") - 1
        )

    @staticmethod
    def encrypt_string(string: str) -> str:
        if not string:
            return string

        return "".join(
            [
                char if char == " " else DeeSeeEncryptionService._encrypt_character(char)
                for char in string
            ]
        )
