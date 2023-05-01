from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Gauge

app = Flask(__name__)
metrics = PrometheusMetrics(app)

topic_lag = Gauge('topic_lag', 'Kafka topic lag',  ['group_id', 'topic_name'])

@app.route('/set_topic_lag')
def set_topic_lag():
    value = request.args.get('value', type=float)
    if value is not None:
        topic_lag.labels("our_example_service", "example-topic").set(value)
        return f"Topic lag set to {value}"
    else:
        return "Invalid value", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
