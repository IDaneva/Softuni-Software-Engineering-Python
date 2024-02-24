from djangoProject_exam.user_profile.models import Profile


def navigation_tabs(request):
    if not Profile.objects.first():
        available_profile = False
    else:
        available_profile = True
    return {'available_profile': available_profile}
