"""
DemoHandler
"""


class DemoHandler:
    """DemoHandler"""

    def __init__(self):
        self.message = "Hello World"

    async def get(self):
        """
        get
        :return:
        """
        return {
            "message": self.message
        }
