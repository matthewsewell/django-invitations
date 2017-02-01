from django.conf import settings


class AppSettings(object):

    def __init__(self, prefix):
        self.prefix = prefix

    def _setting(self, name, dflt):
        from django.conf import settings
        return getattr(settings, self.prefix + name, dflt)

    @property
    def INVITATION_EXPIRY(self):
        """ How long before the invitation expires """
        return self._setting('INVITATION_EXPIRY', 3)

    @property
    def INVITATION_ONLY(self):
        """ Signup is invite only """
        return self._setting('INVITATION_ONLY', False)

    @property
    def CONFIRM_INVITE_ON_GET(self):
        """ Simple get request confirms invite """
        return self._setting('CONFIRM_INVITE_ON_GET', True)

    @property
    def ACCEPT_INVITE_AFTER_SIGNUP(self):
        """ Accept the invitation after the user finished signup. """
        return self._setting('ACCEPT_INVITE_AFTER_SIGNUP', False)

    @property
    def GONE_ON_ACCEPT_ERROR(self):
        """
        If an invalid/expired/previously accepted key is provided, return a
        HTTP 410 GONE response.
        """
        return self._setting('GONE_ON_ACCEPT_ERROR', True)

    @property
    def ALLOW_JSON_INVITES(self):
        """ Exposes json endpoint for mass invite creation """
        return self._setting('ALLOW_JSON_INVITES', False)

    @property
    def SIGNUP_REDIRECT(self):
        """ Where to redirect on email confirm of invite """
        return self._setting('SIGNUP_REDIRECT', 'account_signup')

    @property
    def LOGIN_REDIRECT(self):
        """ Where to redirect on an expired or already accepted invite """
        return self._setting('LOGIN_REDIRECT', settings.LOGIN_URL)
        
    @property
    def AFTER_LOGIN_REDIRECT(self):
        """ 
        Where to redirect on an already accepted invite if 
        ACCEPT_INVITE_AFTER_LOGIN is True
        """
        return (
            self._setting('AFTER_LOGIN_REDIRECT', 
            getattr(settings, 'LOGIN_REDIRECT_URL', None)))

    @property
    def ADAPTER(self):
        """ The adapter, setting ACCOUNT_ADAPTER overrides this default """
        return self._setting(
            'ADAPTER', 'invitations.adapters.BaseInvitationsAdapter')

    @property
    def EMAIL_MAX_LENGTH(self):
        """
        Adjust max_length of e-mail addresses
        """
        return self._setting("EMAIL_MAX_LENGTH", 254)

    @property
    def EMAIL_SUBJECT_PREFIX(self):
        """
        Subject-line prefix to use for email messages sent
        """
        return self._setting("EMAIL_SUBJECT_PREFIX", None)

    @property
    def CUSTOM_INVITER_MODEL(self):
        """
        Model used to link with the invitation
        """
        return self._setting("CUSTOM_INVITER_MODEL", settings.AUTH_USER_MODEL)
        
    @property
    def ALLOW_DUPLICATE_EMAILS(self):
        """
        Allows more than one invite for the same email. After changing
        this, you need to make and run a migation.
        """
        return self._setting("ALLOW_DUPLICATE_EMAILS", False)
        
    @property
    def ACCEPT_INVITE_AFTER_LOGIN(self):
        """
        Makes it possible to log in with an existing account or sign
        up with social media and then be redirected afterward to accept
        the invitation.
        """
        return self._setting("ACCEPT_INVITE_AFTER_LOGIN", False)

app_settings = AppSettings('INVITATIONS_')
