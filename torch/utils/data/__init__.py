# TODO(VitalyFedyunin): Rearranging this imports leads to crash,
# need to cleanup dependencies and fix it
from torch.utils.data.sampler import (
    BatchSampler,
    RandomSampler,
    Sampler,
    SequentialSampler,
    SubsetRandomSampler,
    WeightedRandomSampler,
)
from torch.utils.data.dataset import (
    ChainDataset,
    ConcatDataset,
    Dataset,
    Dataset as MapDataPipe,
    DataChunk,
    IterableDataset,
    IterableDataset as IterDataPipe,
    Subset,
    TensorDataset,
    random_split,
)
from torch.utils.data.dataloader import (
    DataLoader,
    _DatasetKind,
    get_worker_info,
)
from torch.utils.data.distributed import DistributedSampler
from torch.utils.data._decorator import (
    argument_validation,
    functional_datapipe,
    guaranteed_datapipes_determinism,
    non_deterministic,
    runtime_validation,
    runtime_validation_disabled,
)

__all__ = ['BatchSampler',
           'ChainDataset',
           'ConcatDataset',
           'DataLoader',
           'Dataset',
           'DistributedSampler',
           'IterDataPipe',
           'IterableDataset',
           'MapDataPipe',
           'RandomSampler',
           'Sampler',
           'SequentialSampler',
           'Subset',
           'SubsetRandomSampler',
           'TensorDataset',
           'WeightedRandomSampler',
           '_DatasetKind',
           'argument_validation',
           'functional_datapipe',
           'get_worker_info',
           'guaranteed_datapipes_determinism',
           'non_deterministic',
           'random_split',
           'runtime_validation',
           'runtime_validation_disabled']

# Please keep this list sorted
assert __all__ == sorted(__all__)


################################################################################
# import subpackage
################################################################################
from torch.utils.data import datapipes
