

def manager_context(request):

    context = {
        'title': 'MongoManager'
    }
    if request.path == '/':
        context.update({'page':'My Dashboard'})
    return context