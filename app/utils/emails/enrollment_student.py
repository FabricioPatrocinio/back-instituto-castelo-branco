import boto3
from botocore.exceptions import ClientError
from schemas.enrollment_student import EnrollmentStudentResponseSchema
from settings import settings
from utils.logger import logger
from utils.parses import format_cpf, format_phone, format_rg


def send_email_with_html_template(data: dict):
    parse_date = EnrollmentStudentResponseSchema(**data)

    aws_region = "us-east-1"
    ses_client = boto3.client("ses", region_name=aws_region)

    html_template = f"""
        <!DOCTYPE html>
        <html lang="pt-br">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Formulário de Matrícula</title>
        </head>

        <body>
            <main style="margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f4f4f4;">
                <div style="max-width: 600px; background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); margin-top: 20px;">

                    <h2 style="margin-bottom: 20px;">DADOS DO MATRICULADO</h2>

                    <table style="width: 100%; border-collapse: collapse; margin-top: 20px; border: 1px solid #ddd;">
                        <tr style="border: 1px solid #ddd;">
                            <th style="border: 1px solid #ddd; padding: 10px; color: #fff; background-color: rgba(24, 20, 20, 0.692)">
                                Campo</th>
                            <th style="border: 1px solid #ddd; padding: 10px; color: #fff; background-color: rgba(24, 20, 20, 0.692)">
                                Dados do Aluno</th>
                        </tr>
                        <tr style="border: 1px solid #ddd;">
                            <td style="border: 1px solid #ddd; padding: 10px;"><strong>Nome:</strong></td>
                            <td style="border: 1px solid #ddd; padding: 10px;">{parse_date.name}</td>
                        </tr>
                        <tr style="border: 1px solid #ddd;">
                            <td style="border: 1px solid #ddd; padding: 10px;"><strong>Email:</strong></td>
                            <td style="border: 1px solid #ddd; padding: 10px;">{parse_date.email}</td>
                        </tr>
                        <tr style="border: 1px solid #ddd;">
                            <td style="border: 1px solid #ddd; padding: 10px;"><strong>Endereço:</strong></td>
                            <td style="border: 1px solid #ddd; padding: 10px;">{parse_date.address}</td>
                        </tr>
                        <tr style="border: 1px solid #ddd;">
                            <td style="border: 1px solid #ddd; padding: 10px;"><strong>Telefone:</strong></td>
                            <td style="border: 1px solid #ddd; padding: 10px;">{format_phone(parse_date.phone)}</td>
                        </tr>
                        <tr style="border: 1px solid #ddd;">
                            <td style="border: 1px solid #ddd; padding: 10px;"><strong>CPF:</strong></td>
                            <td style="border: 1px solid #ddd; padding: 10px;">{format_cpf(parse_date.student_cpf)}</td>
                        </tr>
                        <tr style="border: 1px solid #ddd;">
                            <td style="border: 1px solid #ddd; padding: 10px;"><strong>RG:</strong></td>
                            <td style="border: 1px solid #ddd; padding: 10px;">{format_rg(parse_date.student_rg)}</td>
                        </tr>
                        <tr style="border: 1px solid #ddd;">
                            <td style="border: 1px solid #ddd; padding: 10px;"><strong>Data nascimento:</strong></td>
                            <td style="border: 1px solid #ddd; padding: 10px;">{parse_date.birth_date.strftime("%d/%m/%Y")}</td>
                        </tr>
                        <tr style="border: 1px solid #ddd;">
                            <td style="border: 1px solid #ddd; padding: 10px;"><strong>Nome da escola:</strong></td>
                            <td style="border: 1px solid #ddd; padding: 10px;">{parse_date.school_name}</td>
                        </tr>
                        <tr style="border: 1px solid #ddd;">
                            <td style="border: 1px solid #ddd; padding: 10px;"><strong>Escolaridade:</strong></td>
                            <td style="border: 1px solid #ddd; padding: 10px;">{parse_date.status_student}</td>
                        </tr>

                        <tr style="border: 1px solid #ddd;">
                            <th style="border: 1px solid #ddd; padding: 10px; color: #fff; background-color: rgba(24, 20, 20, 0.692)">
                                Campo</th>
                            <th style="border: 1px solid #ddd; padding: 10px; color: #fff; background-color: rgba(24, 20, 20, 0.692)">
                                Dados do Responsável</th>
                        </tr>
                        <tr style="border: 1px solid #ddd;">
                            <td style="border: 1px solid #ddd; padding: 10px;"><strong>Nome responsável financeiro:</strong></td>
                            <td style="border: 1px solid #ddd; padding: 10px;"> {parse_date.financial_responsible_name or 'N/A'}</td>
                        </tr>
                        <tr style="border: 1px solid #ddd;">
                            <td style="border: 1px solid #ddd; padding: 10px;"><strong>CPF do Responsável:</strong></td>
                            <td style="border: 1px solid #ddd; padding: 10px;"> {format_cpf(parse_date.financial_responsible_cpf) if parse_date.financial_responsible_cpf else 'N/A'}</td>
                        </tr>
                    </table>
                </div>
            </main>
        </body>
        </html>
    """  # nosec

    sender_email = "fabricioschiffer@gmail.com"
    subject = f"Confirmação de inscrição ({parse_date.type_enrollment}) - Inscrito {parse_date.name}"
    recipient_email = settings.RECIPIENT_EMAILS.split(",")

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
    except Exception as e:
        logger.error(f"Error sending email: {e.response['Error']['Message']}")
        raise e
