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


def get_map(request):
    if request.method == 'GET':
        tileMap = TileMap(8, 8)
        tileMap.printM()

        tileMap.set_init_point([7, 0])
        tileMap.set_pack_point([0, 4])
        tileMap.set_end_point([7, 5])

        shortest_path = tileMap.find_shortest_path()
        print(shortest_path)

        chess_table = tileMap.get_chess_table()

        response = JsonResponse({'table': chess_table})
        # Permite acesso de todos os domínios
        response['Access-Control-Allow-Origin'] = '*'

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
