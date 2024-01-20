from aws_lambda_powertools import Metrics


metrics = Metrics(service="nomeDoServico", namespace="Powertools")
metrics.set_default_dimensions(environment="Dev")
