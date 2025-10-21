# from rest_framework.throttling import SimpleRateThrottle
# from rest_framework.exceptions import Throttled

# class PostPerDayThrottle(SimpleRateThrottle):
#     scope = 'post_per_day'

#     def get_cache_key(self, request, view):
#         ip_addr = self.get_ident(request)
#         return self.cache_format % {'scope': self.scope, 'ident': ip_addr}

#     def throttle_failure(self):
#         """
#         Override to raise a custom message instead of DRF's default one.
#         """
#         raise Throttled(detail="Siz bugun 5 martadan ortiq so‘rov yubordingiz. Iltimos, ertangi kungacha kuting.")



# throttles.py
from rest_framework.throttling import SimpleRateThrottle
from rest_framework.exceptions import Throttled

class PostPerDayThrottle(SimpleRateThrottle):
    scope = "post_per_day"

    def get_cache_key(self, request, view):
        # Throttle only POST requests
        if request.method != "POST":
            return None

        # Identify by user or IP
        if request.user.is_authenticated:
            ident = f"user_{request.user.pk}"
        else:
            ident = f"ip_{self.get_ident(request)}"

        # 👇 include the view (endpoint) name in the cache key
        view_name = view.__class__.__name__.lower()
        return self.cache_format % {
            "scope": f"{self.scope}_{view_name}",
            "ident": ident,
        }

    def throttle_failure(self):
        raise Throttled(
            detail="Siz bu API uchun bugun 5 martadan ortiq POST so‘rov yubordingiz. Iltimos, ertangi kungacha kuting."
        )
