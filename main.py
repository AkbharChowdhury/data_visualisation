from diagram import Diagram
def main():
    hist = Diagram.hist_demo
    popular_lang = Diagram.most_popular_programming_lang
    free_time = Diagram.free_time
    # my_diagram = free_time()
    my_diagram = hist()
    # my_diagram = Diagram.most_popular_programming_lang(top=15)
    Diagram.show(my_diagram)

if __name__ == '__main__':
    main()
