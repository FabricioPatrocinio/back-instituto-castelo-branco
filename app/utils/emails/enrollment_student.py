import boto3
from botocore.exceptions import ClientError
from schemas.enrollment import EnrollmentStudentResponseSchema
from utils.logger import logger


def send_email_with_html_template(email_data: EnrollmentStudentResponseSchema):
    aws_region = "us-east-1"
    ses_client = boto3.client("ses", region_name=aws_region)

    html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Seu Título</title>
        </head>
        <body>
            <p>Olá {email_data.name},</p>
            <p>Informações importantes:</p>
            <ul>
                <li>Endereço: {email_data.address}</li>
                <li>Email: {email_data.email}</li>
                <li>CPF do Estudante: {email_data.student_cpf}</li>
                <li>RG do Estudante: {email_data.student_rg}</li>
                <li>Nota: {email_data.grade}</li>
                <li>Nome da Escola: {email_data.school_name}</li>
                <li>Responsável Financeiro: {email_data.financial_responsible_name or 'N/A'}</li>
                <li>CPF do Responsável Financeiro: {email_data.financial_responsible_cpf or 'N/A'}</li>
            </ul>
            <p>Obrigado!</p>
        </body>
        </html>
    """  # nosec

    sender_email = "fabricioschiffer@gmail.com"
    subject = "Assunto do Email"
    recipient_email = email_data.email

    try:
        response = ses_client.send_email(
            Destination={
                "ToAddresses": [recipient_email],
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": "UTF-8",
                        "Data": html_template,
                    },
                },
                "Subject": {
                    "Charset": "UTF-8",
                    "Data": subject,
                },
            },
            Source=sender_email,
        )

        logger.info(f"Email sent! Message ID: {response['MessageId']}")

    except ClientError as e:
        logger.error(f"Error sending email: {e.response['Error']['Message']}")
        raise e
