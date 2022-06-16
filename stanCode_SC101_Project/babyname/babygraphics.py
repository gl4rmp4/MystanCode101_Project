"""
File: babygraphics.py
Name: Ernest_Huang
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    pass


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # base line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH, fill='black')  # top line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')  # bottom line
    line_space = ((CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) / len(YEARS))
    for i in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE + line_space * i, 0, GRAPH_MARGIN_SIZE + line_space * i,
                           CANVAS_HEIGHT, width=LINE_WIDTH, fill='black')
        canvas.create_text(GRAPH_MARGIN_SIZE + line_space * i, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW, fill='black', )


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #

    line_space = ((CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) / len(YEARS))  # every line space
    rank_space = ((CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK)   # every rank space
    color_count = -1  # choose the color
    # start position
    start_x = 0
    start_y = 0
    # next year position
    end_x = 0
    end_y = 0
    for name in lookup_names:
        color_count += 1
        year_for_rank_text_list = []  # every loop will reform the list
        name_data_year = name_data[name]  # Storage the name_data's year
        for i in range(len(YEARS)):
            '''
            Determine if the name_data have the YEARS list year  
            if YEARS have name_data's year value give the correct rank
            else give * 
            '''
            if str(YEARS[i]) in name_data_year:
                year_for_rank_text_list.append(name_data[name][str(YEARS[i])])
            else:
                year_for_rank_text_list.append('*')
        # 處理點位
        for j in range(len(year_for_rank_text_list) - 1):
            start_x = GRAPH_MARGIN_SIZE + line_space * j
            if year_for_rank_text_list[j] is not '*':
                start_y = GRAPH_MARGIN_SIZE + int(name_data[name][str(YEARS[j])]) * rank_space
            else:
                start_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            end_x = GRAPH_MARGIN_SIZE + line_space * (j + 1)
            if year_for_rank_text_list[j + 1] is not '*':
                end_y = GRAPH_MARGIN_SIZE + int(name_data[name][str(YEARS[j + 1])]) * rank_space
            else:
                end_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            canvas.create_line(start_x, start_y, end_x, end_y, width=LINE_WIDTH, fill=COLORS[color_count])
            canvas.create_text(start_x, start_y, text=str(name) + str(year_for_rank_text_list[j]), anchor=tkinter.SW,
                               fill=COLORS[color_count])
        # final point fix OBOB
        final_x = GRAPH_MARGIN_SIZE + line_space * (len(year_for_rank_text_list) - 1)

        if year_for_rank_text_list[-1] is not '*':
            final_y = GRAPH_MARGIN_SIZE + int(name_data[name][str(YEARS[-1])]) * rank_space
        else:
            final_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
        canvas.create_text(final_x,final_y,text=str(name)+str(year_for_rank_text_list[-1]),anchor=tkinter.SW
                           ,fill=COLORS[color_count])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
