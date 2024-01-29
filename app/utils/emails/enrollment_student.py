import boto3
from botocore.exceptions import ClientError
from schemas.enrollment import EnrollmentStudentResponseSchema
from utils.logger import logger


def send_email_with_html_template(data: dict):
    parse_date = EnrollmentStudentResponseSchema(**data)

    aws_region = "us-east-1"
    ses_client = boto3.client("ses", region_name=aws_region)

    html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Seu Título</title>
        </head>
        <body>
            <p>Olá {parse_date.name},</p>
            <p>Informações importantes:</p>
            <ul>
                <li>Endereço: {parse_date.address}</li>
                <li>Email: {parse_date.email}</li>
                <li>CPF do Estudante: {parse_date.student_cpf}</li>
                <li>RG do Estudante: {parse_date.student_rg}</li>
                <li>Nota: {parse_date.grade}</li>
                <li>Nome da Escola: {parse_date.school_name}</li>
                <li>Responsável Financeiro: {parse_date.financial_responsible_name or 'N/A'}</li>
                <li>CPF do Responsável Financeiro: {parse_date.financial_responsible_cpf or 'N/A'}</li>
            </ul>
            <p>Obrigado!</p>
        </body>
        </html>
    """  # nosec

    sender_email = "fabricioschiffer@gmail.com"  # TODO: Perdir email do instituto castelo branco
    subject = "Assunto do Email"
    recipient_email = [parse_date.email]

    try:
        response = ses_client.send_email(
            Destination={
                "ToAddresses": recipient_email,
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
