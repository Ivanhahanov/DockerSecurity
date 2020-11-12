import docker
from pprint import pprint
from images import CheckImage
from check import CheckContainer
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--image',
                    help='Enter Image Name')
parser.add_argument('-c', '--container',
                    help='Enter Container name')

args = parser.parse_args()
client = docker.APIClient(base_url='unix://var/run/docker.sock')


def print_result(**kwargs):
    for key, value in kwargs.items():
        print(f'[{key}]:  \t{value}')


if args.image is None and args.container is None:
    parser.print_help()

if args.image is not None:
    # Docker Images
    images_list = client.images()
    image_names_with_id = {field['RepoTags'][0].split(':')[0]: field['Id'].split(':')[-1] for field in images_list}
    if args.image in image_names_with_id.keys():
        image_id = image_names_with_id[args.image]
        inspected_images = [client.inspect_image(image_id) for field in images_list]
        check_image = CheckImage(inspected_images[1])
        print('Docker Image Warnings:')
        print_result(**check_image.check_image())

if args.container is not None:
    # Docker Containers
    containers_list = client.containers()
    container_names_with_id = {container['Names'][0][1:]: container['Id'] for container in containers_list}
    if args.container in container_names_with_id.keys():
        container_id = container_names_with_id[args.container]
        check_container = CheckContainer(client.inspect_container(container_id))
        print()
        print('Docker Container Info:')
        print_result(**check_container.check_container())
