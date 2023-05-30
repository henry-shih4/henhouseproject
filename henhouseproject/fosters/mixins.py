from django.contrib.auth.mixins import AccessMixin, UserPassesTestMixin
from django.shortcuts import redirect

class FosterAndLoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_foster:
            return redirect("pet-list")
        return super().dispatch(request, *args, **kwargs)


class SuperUserRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser