import argparse
import json
import numpy as np

from PIL import Image
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description='Generate random images with given parameters.')

    parser.add_argument('--seed', '-s', type=int, default=0,
                        help='Randomization seed.')
    parser.add_argument('--num-images', '-n', type=int, default=1,
                        help='Number of images to generate.')
    parser.add_argument('--width', '-wd', type=int, default='512',
                        help='Width of the images to generate.')
    parser.add_argument('--height', '-ht', type=int, default='512',
                        help='Height of the images to generate.')
    parser.add_argument('--output-dir', '-o', type=str, default='./',
                        help='Directory in which to output generated images.')
    parser.add_argument('--dry-run', default=False, action='store_true',
                        help='Dry run tool without generating images.')

    return parser.parse_args()


def to_path(filename, directory='./'):
    dir_ = Path(directory).resolve()
    dir_.mkdir(parents=True, exist_ok=True)

    return str(dir_ / filename)


def main(args):
    np.random.seed(args.seed)

    height = args.height
    width = args.width

    metadata = {'images': []}
    for i in range(args.num_images):
        print('Generating image {}...'.format(i))

        img_arr = np.random.rand(height, width, 3) * 255
        img = Image.fromarray(img_arr.astype('uint8')).convert('RGB')

        if args.dry_run:
            continue

        img_filepath = to_path('image_{}.jpg'.format(i),
                               directory=args.output_dir)
        img.save(img_filepath)

        metadata['images'].append(
            {'file_name': img_filepath, 'height': height, 'width': width, 'image_id': i})

    if args.dry_run:
        return

    with open(to_path('metadata.json', directory=args.output_dir), 'w') as metadata_file:
        json.dump(metadata, metadata_file, indent=4)


if __name__ == '__main__':
    args = parse_args()
    print('Command line arguments: {}'.format(args))

    main(args)
