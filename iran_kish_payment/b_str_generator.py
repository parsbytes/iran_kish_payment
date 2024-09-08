def generate_b_str(terminal_id: str, password: str, amount: int):
    return f"{terminal_id}{password}" + str(amount).zfill(12) + "00"
