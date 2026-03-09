from pipeline import Pipeline
from steps import NormalizeSpaceStep, TagStep, LenMetaStep

def bild_pipline() -> Pipeline:
    return Pipeline([
        TagStep("raw"),
        NormalizeSpaceStep(),
        LenMetaStep(),
        TagStep("preprocess"),
    ])