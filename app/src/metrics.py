# Métricas

from prometheus_client import Counter

REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total de requisições da aplicação'
)