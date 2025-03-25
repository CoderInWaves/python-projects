import time

class Custom_cellular:
    @staticmethod
    def pattern():
        cells = [0, 0, 1, 0]
        
        while True:
            time.sleep(4)
            new_cells = []
            for i, j in zip(cells, cells[1:]):
                if i + j == 0:
                    new_cells.append(0)
                elif i + j == 1:
                    new_cells.append(1)
                elif i + j == 2:
                    new_cells.append(0)
            cells = (cells + new_cells)[-4:]  # Keep only the last 4 elements
            print(cells)

Custom_cellular.pattern()