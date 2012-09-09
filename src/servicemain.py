from service.service import Service
from protorpc.wsgi import service

app = service.service_mappings([('/api', Service)])