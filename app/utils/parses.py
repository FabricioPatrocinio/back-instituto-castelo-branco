def format_phone(number: str) -> str:
    number = "".join(filter(str.isdigit, number))

    if len(number) == 11:
        number_format = f"{number[:2]} {number[2]} {number[3:7]}-{number[7:]}"
        return number_format

    return number


def format_cpf(cpf) -> str:
    cpf = "".join(filter(str.isdigit, cpf))

    if len(cpf) == 11:
        cpf_format = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        return cpf_format

    return cpf


def format_rg(rg):
    rg = "".join(filter(str.isdigit, rg))

    if len(rg) == 7:
        rg_format = f"{rg[:1]}.{rg[1:4]}.{rg[4:7]}"
        return rg_format

    return rg
