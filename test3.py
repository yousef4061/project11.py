class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.fix()

    def fix(self):

        if self.second >= 60:
            extra_minutes = self.second // 60
            self.second = self.second % 60
            self.minute += extra_minutes
        elif self.second < 0:
            self.minute -= 1
            self.second += 60

        if self.minute >= 60:
            extra_hours = self.minute // 60
            self.minute = self.minute % 60
            self.hour += extra_hours
        elif self.minute < 0:
            self.hour -= 1
            self.minute += 60

        if self.hour >= 24:
            self.hour = self.hour % 24
        elif self.hour < 0:
            self.hour += 24

    def show(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
    

if __name__ == "__main__":
    t1 = Time(5, 75, 127)
    print(t1.show())

    t2 = Time(4, -10, -50)
    print(t2.show())
