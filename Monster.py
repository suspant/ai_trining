#creating instances
class Monster:
    hitpoint =1
    color = "yellow"
    weapon = "sword"

    def battlecry(self):
        return self.weapon.upper()
