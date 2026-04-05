import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def makeMultiPlot(data, post_types, plot_dir, plot_name, title, x_label, y_label, x_lim, y_lim, colors):
    fig, ax = plt.subplots(figsize=(12, 6))

    # data.plot()

    for post_type in post_types:
        ax.plot(data[post_type], linestyle='-', label=post_type, color=colors[post_type])

    # Format x-axis to show ticks based on time interval
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    plt.title(title,    fontsize=20)
    plt.xlabel(x_label, fontsize=16)
    plt.ylabel(y_label, fontsize=16)
    if x_lim:
        plt.xlim(x_lim)
    if y_lim:
        plt.ylim(y_lim)
    ax.legend()
    plt.grid(True)
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()

    savePlot(plot_dir, plot_name)

    # close all windows to avoid combining plots
    plt.close('all')


# save plot to png and pdf
def savePlot(plot_dir, plot_name):
    output_png = "{0}/{1}.png".format(plot_dir, plot_name)
    output_pdf = "{0}/{1}.pdf".format(plot_dir, plot_name)
    plt.savefig(output_png, bbox_inches='tight')
    plt.savefig(output_pdf, bbox_inches='tight')
