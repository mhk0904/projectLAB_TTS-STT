class Rectangle:
    count = 0  # 클래스 변수

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    # 인스턴스 메서드
    def calcArea(self):
        area = self.width * self.height
        return area


class Woman:
    def __init__(self,iq,wegiht):
        self.iq = iq
        self.wegiht = wegiht

    def chat(self):
        self.iq += 1

    def yoga(self):
        self.wegiht -= 1

    def show_state(self):
        print(self.iq)
        print(self.wegiht)

# km = Woman(70,1)
# km.show_state()
# km.yoga()
# km.show_state()


class Man:
    def __init__(self, iq, wegiht):
        self.iq = iq
        self.wegiht = wegiht

    def eat(self):
        self.wegiht += 10

    def game(self):
        self.iq += 10

    def show(self):
        print(self.iq)
        print(self.wegiht)

ka = Man(200,65)
ka.show()



    # # 정적 메서드
    # @staticmethod
    # def isSquare(rectWidth, rectHeight):
    #     return rectWidth == rectHeight   

    # # 클래스 메서드
    # @classmethod
    # def printCount(cls):
    #     print(cls.count)   


# 테스트
# square = Rectangle.isSquare(5, 5)        
# print(square)   # True        

rect1 = Rectangle(5, 5)
rect2 = Rectangle(2, 5)
#rect1.printCount()  # 2 
#print(rect1.height)
#print(rect2.height)

