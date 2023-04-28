import pympi 
from format_elan.utils import milliseconds_to_sec
def get_tsv(file_path_to_elan):
    elan_object = pympi.Elan.Eaf(file_path_to_elan)
    txt = ""
    for tier in elan_object.get_tier_names():
        for annotation in elan_object.get_annotation_data_for_tier(tier):
            txt += f"{tier}\t{milliseconds_to_sec(annotation[0])}\t{milliseconds_to_sec(annotation[1])}\t{milliseconds_to_sec(annotation[1]-annotation[0])}\t{annotation[2]}\n"
    return txt