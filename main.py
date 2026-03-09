from build import bild_pipline

class Frame:
    def __init__(self, data:str):
        self.data = data
        self.meta = {}
def main():
    frame = Frame(" hello world ")
    pipline = bild_pipline()
    result = pipline.run(frame)
    print(result.data)
    print(result.meta)

if __name__ == "__main__":
    main()
