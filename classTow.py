class Two:
    def __init__(self, last_name, first_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"Full Name : {self.first_name} {self.last_name}"


two = Two("rahman","atik")
print(two)