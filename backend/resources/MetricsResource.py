from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
import psutil

REQUEST_COUNT = Counter('http_requests_total', 'Total number of HTTP requests', ['method', 'endpoint'])
REQUEST_DURATION = Histogram('http_request_duration_seconds', 'HTTP request duration in seconds', ['method', 'endpoint'])
CPU_UTILIZATION = Gauge('cpu_utilization_percent', 'CPU utilization percentage')

class MetricsResource:
    def on_get(self, req, resp):
        # Collect CPU utilization
        cpu_percent = psutil.cpu_percent()
        CPU_UTILIZATION.set(cpu_percent)

        # Set response content type and body
        resp.content_type = CONTENT_TYPE_LATEST
        resp.body = generate_latest()

        # Increment request count
        REQUEST_COUNT.labels(method=req.method, endpoint=req.path).inc()