import argparse
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


def save_image(image, name, directory='./'):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    image.save(directory / name)


def main(args):
    np.random.seed(args.seed)

    for i in range(args.num_images):
        img_arr = np.random.rand(args.height, args.width, 3) * 255
        img = Image.fromarray(img_arr.astype('uint8')).convert('RGB')

        if not args.dry_run:
            save_image(img, 'image_{}.jpg'.format(i),
                       directory=args.output_dir)


if __name__ == '__main__':
    args = parse_args()
    print('Command line arguments: {}'.format(args))

    main(args)
