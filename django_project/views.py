from django.http import HttpResponseRedirect

def angular_router(request, path):
    idx = request.path.find(path)
    return HttpResponseRedirect(request.path[0:idx] + '#/' + path)
