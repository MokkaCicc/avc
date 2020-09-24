import avc


def main():
    c = avc.Choregraphy()
    c.load_choregraphy('.\\routines', '.\\choregraphies\\template.json')
    print(c)

if __name__ == "__main__":
    main()