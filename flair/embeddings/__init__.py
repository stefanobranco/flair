# Expose base classses
from flair.embeddings.transformer import (
    TransformerEmbeddings,
    TransformerJitDocumentEmbeddings,
    TransformerJitWordEmbeddings,
    TransformerOnnxDocumentEmbeddings,
    TransformerOnnxWordEmbeddings,
)

from .base import Embeddings, ScalarMix

# Expose document embedding classes
from .document import (
    DocumentCNNEmbeddings,
    DocumentEmbeddings,
    DocumentLMEmbeddings,
    DocumentPoolEmbeddings,
    DocumentRNNEmbeddings,
    DocumentStaticEmbeddings,
    DocumentTFIDFEmbeddings,
    SentenceTransformerDocumentEmbeddings,
    TransformerDocumentEmbeddings,
)

# Expose image embedding classes
from .image import (
    ConvTransformNetworkImageEmbeddings,
    IdentityImageEmbeddings,
    ImageEmbeddings,
    NetworkImageEmbeddings,
    PrecomputedImageEmbeddings,
)

# Expose legacy embedding classes
from .legacy import (
    BertEmbeddings,
    CamembertEmbeddings,
    CharLMEmbeddings,
    DocumentLSTMEmbeddings,
    DocumentMeanEmbeddings,
    ELMoEmbeddings,
    ELMoTransformerEmbeddings,
    OpenAIGPT2Embeddings,
    OpenAIGPTEmbeddings,
    RoBERTaEmbeddings,
    XLMEmbeddings,
    XLMRobertaEmbeddings,
    XLNetEmbeddings,
)

# Expose token embedding classes
from .token import (
    BPEmbSerializable,
    BytePairEmbeddings,
    CharacterEmbeddings,
    FastTextEmbeddings,
    FlairEmbeddings,
    HashEmbeddings,
    MuseCrosslingualEmbeddings,
    NILCEmbeddings,
    OneHotEmbeddings,
    PooledFlairEmbeddings,
    StackedEmbeddings,
    TokenEmbeddings,
    TransformerWordEmbeddings,
    WordEmbeddings,
)

__all__ = [
    "Embeddings",
    "ScalarMix",
    "DocumentCNNEmbeddings",
    "DocumentEmbeddings",
    "DocumentLMEmbeddings",
    "DocumentPoolEmbeddings",
    "DocumentStaticEmbeddings",
    "DocumentRNNEmbeddings",
    "DocumentTFIDFEmbeddings",
    "SentenceTransformerDocumentEmbeddings",
    "TransformerDocumentEmbeddings",
    "ConvTransformNetworkImageEmbeddings",
    "IdentityImageEmbeddings",
    "ImageEmbeddings",
    "NetworkImageEmbeddings",
    "PrecomputedImageEmbeddings",
    "BertEmbeddings",
    "CamembertEmbeddings",
    "CharLMEmbeddings",
    "DocumentLSTMEmbeddings",
    "DocumentMeanEmbeddings",
    "ELMoTransformerEmbeddings",
    "OpenAIGPT2Embeddings",
    "OpenAIGPTEmbeddings",
    "RoBERTaEmbeddings",
    "XLMEmbeddings",
    "XLMRobertaEmbeddings",
    "XLNetEmbeddings",
    "BPEmbSerializable",
    "BytePairEmbeddings",
    "CharacterEmbeddings",
    "ELMoEmbeddings",
    "FastTextEmbeddings",
    "FlairEmbeddings",
    "HashEmbeddings",
    "MuseCrosslingualEmbeddings",
    "NILCEmbeddings",
    "OneHotEmbeddings",
    "PooledFlairEmbeddings",
    "StackedEmbeddings",
    "TokenEmbeddings",
    "TransformerWordEmbeddings",
    "WordEmbeddings",
    "TransformerEmbeddings",
    "TransformerOnnxWordEmbeddings",
    "TransformerOnnxDocumentEmbeddings",
    "TransformerJitWordEmbeddings",
    "TransformerJitDocumentEmbeddings",
]
