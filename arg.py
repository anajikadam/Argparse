import argparse

# def humanDetector(args):
#     image_path = args["image"]
#     video_path = args['video']
#     if str(args["camera"]) == 'true' : camera = True 
#     else : camera = False
#     print(image_path)
#     print(video_path)
#     print(camera)

class Cal:
    def __init__(self, args) -> None:
        self.num1 = args["num1"]
        self.num2 = args["num2"]

    def add(self):
        a = self.num1
        b = self.num2
        print("Adddition : ", a+b)

    def Sub(self):
        a = self.num1
        b = self.num2
        print("Subtraction : ", a-b)

    def Mul(self):
        a = self.num1
        b = self.num2
        if a==0 or b==0:
            print("Any one Given number is Zero So Multiplication is Zero")
        else:
            print("Multiplication : ", a*b)

    def Div(self):
        a = self.num1
        b = self.num2
        if a==0 or b==0:
            print("Any one Given number is Zero So Division is Not Possible")
        else:
            print("Division : ", a/b)

def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-a", "--num1", default=0, type=int, help="Number 1 ")
    arg_parse.add_argument("-b", "--num2", default=0, type=int, help="Number 2 ")
    arg_parse.add_argument("-c", "--Cal", default="All", type=str, help="All: All Operation, Add, Sub, Mul, Div")
    # arg_parse.add_argument("-v", "--video", default=None, help="path to Video File ")
    # arg_parse.add_argument("-i", "--image", default=None, help="path to Image File ")
    # arg_parse.add_argument("-c", "--camera", default=False, help="Set true if you want to use the camera.")
    # arg_parse.add_argument("-o", "--output", type=str, help="path to optional output video file")
    args = vars(arg_parse.parse_args())
    return args

if __name__ == "__main__":

    args = argsParser()
    print(args)
    c = Cal(args)
    if args["Cal"]=="All":
        c.add()
        c.Sub()
        c.Mul()
        c.Div()
    elif args["Cal"]=="Add":
        c.add()
    elif args["Cal"]=="Sub":
        c.Sub()
    elif args["Cal"]=="Mul":
        c.Mul()
    elif args["Cal"]=="Div":
        c.Div()
    # humanDetector(args)



# E: && cd E:\Python
# python arg.py -a 12 -b 32 -c "All"