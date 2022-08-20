from flask import Flask

from clean_arch_python.main.adapters.flask_adapter import FlaskAdapter
from clean_arch_python.main.factories.client_factory import ClientFactory

app = Flask(__name__)

app.add_url_rule(
    "/api/clients",
    "find_all_clients",
    methods=["GET"],
    view_func=FlaskAdapter.adapt(ClientFactory.get_find_all_clients_controller()),
)
app.add_url_rule(
    "/api/clients",
    "create_client",
    methods=["POST"],
    view_func=FlaskAdapter.adapt(ClientFactory.get_create_client_controller()),
)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
