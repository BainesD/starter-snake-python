import typing

class Snake:
      my_head = None
      my_neck = None
      my_body = None
      def __init__(self, game_state: typing.Dict):
        self.my_head = game_state["you"]["body"][0]
        self.my_neck = game_state["you"]["body"][1]
        self.my_body = game_state["you"]["body"]
      
      def debug(self):
          print(f"BODY {self.my_body}")
          
    