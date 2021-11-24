"""
collection of function for pokelol
"""
import json
from io import BufferedReader
from typing import Union

from transparentpath import Path


def txt_openner(file_path) -> list[bytes]:
    """
    function used to open txt file, using read bytes mod ("rb") for decoding purposes

    Parameters
    ----------
    file_path : Union[str, Path]
        path to the txt file

    Returns
    -------
    list[bytes]
        list of bytes, hetch bytes correspond to a list
    """
    with open(file_path, 'rb') as f:
        data = f.readlines()
    return data


def txt_parser(bytes_list: list[bytes]) -> dict:
    """
    cast bytes to string and transform into dict, consider that text in encoded in uft8
    (casting cols name in lowered string)

    Parameters
    ----------
    bytes_list

    Returns
    -------
    dict:
        {col1_index1 : {col2_index0: value,...coln_index0: value}, ...}
    """
    ret = {}
    items = bytes_list[0].decode("ascii").replace("\n", "").replace("\r", " ").split("\t")[1:]
    for i in bytes_list[1:]:
        try:
            data = i.decode("utf-8").replace("\n", "").replace("\r", " ").split("\t")
        except Exception as e:
            print(f"Warning: txt is encoded in something weird, problematic char is : \\{str(e).split(' ')[5]}")
            data = i.replace(b"\xe7", b"c").replace(b"\xe9", b"e").replace(b"\xe0", b"a").decode("utf-8").replace(
                "\n", "").replace("\r", " ").split("\t")
        ret[str(data[0]).lower()] = {str(j).lower(): str(k) for j, k in zip(items, data[1:])}
    return ret


def save_to_json(data: dict, path: Union[str, Path]):
    """
    save data (dict) to a json file at path.
    
    Parameters
    ----------
    data : dict
        data as dict (serializable)
    path: Union[str, Path]
        path were to save the file
    
    Returns
    -------
    None
    """
    json.dump(data, path)


def load_config(path: Union[str, Path]):
    """
    load data for json file

    Parameters
    ----------
    path: Union[str, Path]
        path to the json file

    Returns
    -------

    """
    return json.load(path)
