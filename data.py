

from torchvision import transforms, datasets

_CIFAR_DATASET_DIR = './datasets/CIFAR'
_IMAGENET_DATASET_DIR = './datasets/IMAGENET/ILSVRC2012'
_PLACES205_DATASET_DIR = './datasets/Places205'

trans = transforms.Compose(transforms_list)
split = 'train'
split = split.lower()
split_data_dir = _IMAGENET_DATASET_DIR + '/' + split
train_set = datasets.ImageFolder(root="./data", train=True, download=True, transform=trans)
test_set = datasets.ImageFolder(root="./data", train=False, download=True, transform=trans)