import boto3
import os

def lambda_handler(event, context):
    sns_topic_arn = os.environ['SNS_TOPIC_ARN']  
   
    sns_client = boto3.client('sns')
    message = "O alarme de preço foi acionado! Verifique seus custos na AWS."
    subject = "Alerta de Preço AWS"
    
    try:
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=message,
            Subject=subject
        )
        print("Notificação por e-mail enviada com sucesso:", response)
    except Exception as e:
        print("Erro ao enviar notificação por e-mail:", e)