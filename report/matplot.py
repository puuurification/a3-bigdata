# data from https://allisonhorst.github.io/palmerpenguins/

import matplotlib.pyplot as plt
import numpy as np
import pylatex as pl

def main(fname, width, *args, **kwargs):
    geometry_options = {"right": "2cm", "left": "2cm"}
    doc = pl.Document(fname, geometry_options=geometry_options)

    doc.append('Introduction.')

    with doc.create(pl.Section('I am a section')):
        doc.append('Take a look at this beautiful plot:')

        with doc.create(pl.Figure(position='htbp')) as plot:
            plot.add_plot(width=pl.NoEscape(width), *args, **kwargs)
            plot.add_caption('I am a caption.')

        doc.append('Created using matplotlib.')

    doc.append('Conclusion.')

    doc.generate_tex('report/tex/matplot')
    # doc.generate_pdf(clean_tex=False)


if __name__ == '__main__':

    species = ("Adelie", "Chinstrap", "Gentoo", "Gentoo")
    penguin_means = {
        'Both Sexes': (18.35, 18.43, 14.98),
        'Males': (38.79, 48.83, 47.50),
        'Females': (189.95, 195.82, 217.19),
        'Indexs': (189.95, 195.82, 217.19),
    }

    x = np.arange(len(species))  # the label locations
    width = 0.10  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1 

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Length (mm)')
    ax.set_title('Penguin attributes by species')
    ax.set_xticks(x + width, species)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 250)

    # plt.show()
    plt.savefig('report/img/foo.png')

    # main('matplotlib_ex-dpi', r'1\textwidth', dpi=300)
    # main('matplotlib_ex-facecolor', r'0.5\textwidth', facecolor='b')
