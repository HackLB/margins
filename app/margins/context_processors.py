from django.conf import settings


def apikeys(request):
    added_context = {
        'hello': 'world',
    }

    return added_context