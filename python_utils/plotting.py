from typing import Optional


def make_axis_style(
    *,
    xlim: Optional[list] = None,
    ylim: Optional[list] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    title: Optional[str] = None,
    xticks: Optional[list] = None,
    xticklabels: Optional[list] = None,
    yticks: Optional[list] = None,
    yticklabels: Optional[list] = None,
) -> dict:

    """make style dictionary for axis.set(**style_dict)
    good cheatsheet https://qiita.com/nkay/items/d1eb91e33b9d6469ef51

    Args:
        xlim (Optional[list], optional): Defaults to None.
        ylim (Optional[list], optional): Defaults to None.
        xlabel (Optional[str], optional): Defaults to None.
        ylabel (Optional[str], optional): Defaults to None.
        title (Optional[str], optional): Defaults to None.
        xticks (Optional[list], optional): Defaults to None.
        xticklabels (Optional[list], optional): Defaults to None.
        yticks (Optional[list], optional): Defaults to None.
        yticklabels (Optional[list], optional): Defaults to None.

    Returns:
        dict: style dictionary
    """

    style_dict: dict = {}
    for key, value in [
        ["xlim", xlim],
        ["ylim", ylim],
        ["xlabel", xlabel],
        ["ylabel", ylabel],
        ["title", title],
        ["xticks", xticks],
        ["yticks", yticks],
        ["xticklabels", xticklabels],
        ["yticklabels", yticklabels],
    ]:
        if not value is None:
            style_dict[key] = value
    return style_dict
