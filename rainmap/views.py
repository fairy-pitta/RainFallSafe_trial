
from django.shortcuts import render
import requests

# def get_rainfall_data(request):
#     url = 'https://api.data.gov.sg/v1/environment/rainfall'
#     response = requests.get(url)
#     data = response.json()
#     stations = data['metadata']['stations']
#     readings = data['items'][0]['readings']
#     timestamp = data['items'][0]['timestamp']  # タイムスタンプのデータを取得
#     return stations, readings, timestamp

from django.http import JsonResponse

def get_rainfall_data(request):
    url = 'https://api.data.gov.sg/v1/environment/rainfall'
    response = requests.get(url)
    data = response.json()
    # Since you're directly using this in the frontend, consider returning JsonResponse
    return JsonResponse(data)

def show_map(request):
    return render(request, 'rainmap/index.html')