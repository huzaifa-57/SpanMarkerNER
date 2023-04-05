import pytest
from datasets import DatasetDict, load_dataset

from span_marker.modeling import SpanMarkerModel
from tests.constants import CONLL_LABELS, FEWNERD_COARSE_LABELS


@pytest.fixture()
def fresh_conll_span_marker_model() -> SpanMarkerModel:
    return SpanMarkerModel.from_pretrained("prajjwal1/bert-tiny", labels=CONLL_LABELS)


@pytest.fixture()
def finetuned_conll_span_marker_model() -> SpanMarkerModel:
    return SpanMarkerModel.from_pretrained("tomaarsen/span-marker-bert-tiny-conll03")


@pytest.fixture()
def fresh_fewnerd_span_marker_model() -> SpanMarkerModel:
    return SpanMarkerModel.from_pretrained("prajjwal1/bert-tiny", labels=FEWNERD_COARSE_LABELS)


@pytest.fixture()
def finetuned_fewnerd_span_marker_model() -> SpanMarkerModel:
    return SpanMarkerModel.from_pretrained("tomaarsen/span-marker-bert-tiny-fewnerd-coarse-super")


@pytest.fixture(scope="session")
def conll_dataset_dict() -> DatasetDict:
    return DatasetDict.load_from_disk("tests/data/tiny_conll2003")


@pytest.fixture(scope="session")
def fewnwerd_coarse_dataset_dict() -> DatasetDict:
    return DatasetDict.load_from_disk("tests/data/tiny_fewnerd_super").remove_columns("fine_ner_tags")
