import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dronezonia.models import Path
from rest_framework import viewsets

from .map.tile_map import TileMap
from .serializer import PathSerializer


class PathViewSet(viewsets.ModelViewSet):
    """Exibe os caminhos já percorridos"""
    queryset = Path.objects.all()
    serializer_class = PathSerializer


@csrf_exempt
def get_map(request):
    response = JsonResponse({})

    tileMap = TileMap(8, 8)

    if request.method == 'POST':
        print("Recebemos os valores")
        data = json.loads(request.body)
        print(data)

        tileMap.set_init_point([data[0]['row'], data[0]['col']])
        tileMap.set_pack_point([data[1]['row'], data[1]['col']])
        tileMap.set_end_point([data[2]['row'], data[2]['col']])

        shortest_path = tileMap.find_shortest_path()

        print(shortest_path)

        response = JsonResponse({'path': shortest_path})

    if request.method == 'GET':

        tileMap.set_init_point([7, 0])
        tileMap.set_pack_point([0, 4])
        tileMap.set_end_point([7, 5])

        shortest_path = tileMap.find_shortest_path()
        print(shortest_path)

        chess_table = tileMap.get_chess_table()

        response = JsonResponse({'table': chess_table})

    return response


@csrf_exempt
def get_shortest(request):
    # coleta o json enviado pelo request
    data = json.loads(request.body)

    tile_map = TileMap(8, 8)
    tile_map.fill_with_data(data)

    return JsonResponse({'GET': "Short"})


def path(request):
    if request.method == 'GET':
        return JsonResponse({'status': 'okasdasd'})


def pega_aluno(request):
    # Lógica para lidar com o método GET para a rota '/aluno'
    return JsonResponse({'GET': "GET"})


def post_aluno(request):
    # Lógica para lidar com o método POST para a rota '/aluno'
    return JsonResponse({'POST': "POST"})
