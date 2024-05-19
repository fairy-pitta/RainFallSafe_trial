
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

from django.shortcuts import render
import requests

def show_map(request):
    # APIからデータを取得してマップに渡す
    response = requests.get('https://api.data.gov.sg/v1/environment/rainfall')
    data = response.json()
    stations = data['metadata']['stations']
    readings = data['items'][0]['readings']
    timestamp = data['items'][0]['timestamp']

    context = {
        'stations': stations,
        'readings': readings,
        'timestamp': timestamp
    }
    return render(request, 'rainmap/index.html', context)
