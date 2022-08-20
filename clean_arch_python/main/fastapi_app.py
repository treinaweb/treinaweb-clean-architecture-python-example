from fastapi import FastAPI, Request

from clean_arch_python.main.factories.client_factory import ClientFactory
from clean_arch_python.main.adapters.fastapi_adapter import FastAPIAdapter

app = FastAPI()

app.add_api_route(
    "/api/clients",
    FastAPIAdapter.adapt(ClientFactory.get_find_all_clients_controller()),
    methods=["GET"],
)
app.add_api_route(
    "/api/clients",
    FastAPIAdapter.adapt(ClientFactory.get_create_client_controller()),
    methods=["POST"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=3001, debug=True)
