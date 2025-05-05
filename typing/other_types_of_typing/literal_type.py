#Literal Type (only specific values)

from typing import Literal

def move(direction: Literal["left", "right", "up", "down"]) -> None:
    print(f"Moving {direction}")

move("up")     # ✅
# move("jump") # ❌ (Error in static check)