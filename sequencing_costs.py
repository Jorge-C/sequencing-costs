from __future__ import print_function

from datetime import date

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import requests


def get_file(url):
    """Downloads file using requests."""
    r = requests.get(url, stream=True)
    if r.ok:
        return r.raw
    else:
        raise RuntimeError(
            "Downloading file in url: {url} failed. If trying to open said"
            " url in a browser doesn't work either, the data file may have"
            " been updated: please create an issue in"
            " https://github.com/Jorge-C/sequencing-costs".format(url=url))


def parse_file(f):
    """Use pandas to extract the data."""
    xd = pd.ExcelFile(f)
    sheet = xd.parse('Data Table')
    dates = sheet['Date']
    costs = sheet['Cost per Mb']
    return dates, costs


def create_moore_law_data(dates, initial_y_value):
    """Data that decreases following Moore's law.

    Moore's law says computing power doubles every two years, so we
    halve sequencing cost every two years."""
    diff = dates - dates[0]
    ns_to_year = 1e9 * 3600 * 24 * 365
    diff = np.asarray(diff.values, dtype=np.int64) / ns_to_year
    doubles_every = 2  # years
    return initial_y_value * np.power(0.5, diff / doubles_every)


def plot_costs(dates, sequencing_costs, moore_law):
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(11, 6))

        # It seems matplotlib doesn't like numpy's datetime64 very much
        ax.semilogy(dates.astype(date), moore_law, 'k--', dashes=(30, 20))
        ax.semilogy(dates.astype(date), sequencing_costs, 'k')

        # annotations on the plot
        plt.annotate('Cost per Raw Megabase\n   of DNA Sequence  ',
                     xy=(date(2002, 1, 1), 1),
                     xytext=(date(2003, 1, 1), 0.4e3),
                     rotation=-11)
        plt.annotate("Moore's Law (\"Computing power doubles every 2 years\")",
                     xy=(date(2003, 1, 1), 1), xytext=(date(2003, 1, 1), 7e3),
                     rotation=-9)
        plt.annotate(
            '   Transition from\nSanger to "next-gen"\n      sequencing',
            xy=(date(2007, 11, 1), 350), arrowprops=dict(arrowstyle='->'),
            xytext=(date(2004, 1, 1), 1))

        plt.annotate('  QIIME published\nin Nature Methods',
                     xy=(date(2010, 5, 1), 0.5),
                     arrowprops=dict(arrowstyle='->'),
                     xytext=(date(2010, 6, 1), 10))

        ax.set_ylabel('Cost/$')
        ax.set_xlabel('Date')
        fig.suptitle('Sequencing cost', fontsize=20)

        # remove the ticks that show up on the top and right side
        ax.yaxis.tick_left()
        ax.xaxis.tick_bottom()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        # and also minor ticks in the log scale (they look off in xkcd mode)
        ax.tick_params(axis='y', which='minor', left='off')

        return fig

if __name__ == '__main__':
    # Data available in: http://www.genome.gov/sequencingcosts/
    # Update url to new file if this fails or a new version is available.
    # Last updated on March 2014.
    DATA_URL = 'http://www.genome.gov/pages/der/sequencing_costs.xlsx'

    print("Fetching data...")
    excel = get_file(DATA_URL)

    print("Extracting data...")
    dates, costs = parse_file(excel)

    print("Moore's law...")
    # initial y value could also be costs[0], but I like how it looks like this
    moore = create_moore_law_data(dates, 0.7e4)

    print("Creating figure...")
    fig = plot_costs(dates, costs, moore)

    print("Saving file...")
    plt.savefig('sequencing_cost.pdf', bbox_inches='tight', pad_inches=0.05)

    print("OK, done")
