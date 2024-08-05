from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Ola mundo, Voce esta no index de enquetes. ")

def detalhes(request, pergunta_id):
    return HttpResponse(f"Voce esta vendo os resultado da questao{pergunta_id}")

def resultado(request, pergunta_id):
    return HttpResponse(f"Voces esta vendo os resultados da pergunta{pergunta_id}")

def votos(request, pergunta_id):
    pergunta = get_object_or_404(pergunta, pk=pergunta_id)
    try:
        escolha_selecionada = pergunta.escolha_set.get(pk=request.POST("escolha"))
        
