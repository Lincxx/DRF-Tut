from django.http import JsonResponse


# function based view
def api_home(request, *args, **kwargs):
    return JsonResponse({'message': 'Hi there this is your api reponse'})


