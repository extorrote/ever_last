
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import  force_str

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            force_str(user.pk) + force_str(timestamp) +
            force_str(user.is_active)
        )

account_activation_token = AccountActivationTokenGenerator()




