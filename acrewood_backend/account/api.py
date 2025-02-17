from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import SignupForm
import json

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    print("Received Data:", json.dumps(request.data, indent=2))  # Log received data

    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email', ''),
        'name': data.get('name', ''),
        'password1': data.get('password1', ''),
        'password2': data.get('password2', ''),
    })

    if form.is_valid():
        form.save()
    else:
        message = 'error'
        print("Form Errors:", form.errors)  # Log form validation errors

    return JsonResponse({'message': message})



@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })
