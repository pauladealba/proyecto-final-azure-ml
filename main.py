from database import Database
from model import ChurnModel
from deployer import Deployer

if __name__ == "__main__":
    print("Iniciando proyecto de predicción de churn...")

    db = Database("Customer-Churn-Records.csv")
    data = db.load_data()

    churn_model = ChurnModel()
    accuracy = churn_model.train(data)

    deployer = Deployer(
        endpoint_name="apifinal8",
        deployment_name="modelo-1",
        model_name="modelo"
    )

    deployer.show_deployment_info()

    print("Proyecto ejecutado correctamente.")
    print(f"Accuracy del modelo: {accuracy}")