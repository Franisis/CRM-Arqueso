from django.shortcuts import render
from django.http import JsonResponse
import random
# Create your views here.

def verificar_cliente(request):
    if request.method == 'GET':
        # Simulación de verificación de cliente
        # Aquí puedes implementar una lógica de simulación, por ejemplo, generar un mensaje aleatorio
        
        mensajes = ["Se registró con éxito la información", "Usuario ya existente"]
        mensaje = random.choice(mensajes)

        return JsonResponse({'mensaje': mensaje})

    return JsonResponse({'mensaje': 'Método no permitido'})


