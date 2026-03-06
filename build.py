from pipeline import Pipeline
from steps import NormalizeSpaceStep, TagStep, LenMetaStep\

def bild_pipline() -> Pipeline:
    return Pipeline([
        TagStep(),
        NormalizeSpaceStep(),
        LenMetaStep(),
        TagStep(),
    ])