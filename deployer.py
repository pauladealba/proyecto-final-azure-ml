class Deployer:
    def __init__(self, endpoint_name, deployment_name, model_name):
        self.endpoint_name = endpoint_name
        self.deployment_name = deployment_name
        self.model_name = model_name

    def show_deployment_info(self):
        print("Información del despliegue en Azure:")
        print(f"Endpoint: {self.endpoint_name}")
        print(f"Implementación: {self.deployment_name}")
        print(f"Modelo: {self.model_name}")
        print("Estado: desplegado en Azure Machine Learning")
        print("Tráfico asignado: 100%")