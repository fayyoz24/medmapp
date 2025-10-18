from rest_framework.throttling import SimpleRateThrottle
from rest_framework.exceptions import Throttled

class PostPerDayThrottle(SimpleRateThrottle):
    scope = 'post_per_day'

    def get_cache_key(self, request, view):
        ip_addr = self.get_ident(request)
        return self.cache_format % {'scope': self.scope, 'ident': ip_addr}

    def throttle_failure(self):
        """
        Override to raise a custom message instead of DRF's default one.
        """
        raise Throttled(detail="Siz bugun 5 martadan ortiq so‘rov yubordingiz. Iltimos, ertangi kungacha kuting.")
