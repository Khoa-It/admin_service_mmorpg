from responses.api_response import create_response


class AdminController:
    def __init__(self, repository):
        self.repository = repository

    def login(self, email, password):
        result = self.repository.getByAccount(email, password)
        return create_response(
            "Get account success",
            "Error when get account" ,
            result,
        )