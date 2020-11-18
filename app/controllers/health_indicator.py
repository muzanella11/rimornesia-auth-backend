from app.core.controllers import BaseControllers

class HealthIndicator(BaseControllers):
    def run(self):
        data = {
            'code': 200,
            'message': 'Success'
        }

        return self.create_response(data)