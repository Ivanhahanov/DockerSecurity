import docker
from source.images import CheckImage
from source.check import CheckContainer
from source.info import show_info
import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--image',
                    help='Image Name')
parser.add_argument('-c', '--container',
                    help='Container name')
parser.add_argument('-r', '--reverse',
                    help='Reverse image to Dockerfile')
parser.add_argument('--info', action="store_true",
                    help='Show info about output result')

args = parser.parse_args()
client = docker.APIClient(base_url='unix://var/run/docker.sock')
container_result = image_result = None


def print_result(**kwargs):
    for key, value in kwargs.items():
        print(f'[{key}]:  \t{value}')


def reverse_docker_image_to_dockerfile(image_name):
    history = client.history(image_name)
    for line in reversed(history):
        line = line['CreatedBy']
        line = ' '.join(line.split())
        line = line.replace('/bin/sh -c #(nop)', '')
        line = line.replace('/bin/sh -c', ' RUN')
        line = line.replace('&&', "\n\t&&")
        print(line)


if args.reverse:
    reverse_docker_image_to_dockerfile(args.reverse)

if args.image:
    # Docker Images
    images_list = client.images()
    image_names_with_id = {field['RepoTags'][0].split(':')[0]: field['Id'].split(':')[-1] for field in images_list}
    if args.image in image_names_with_id.keys():
        image_id = image_names_with_id[args.image]
        # pprint(client.inspect_image(image_id))
        check_image = CheckImage(client.inspect_image(image_id))
        print('Docker Image Warnings:')
        image_result = check_image.check_image()
        print_result(**image_result)

if args.container:
    # Docker Containers
    containers_list = client.containers()
    container_names_with_id = {container['Names'][0][1:]: container['Id'] for container in containers_list}
    if args.container in container_names_with_id.keys():
        container_id = container_names_with_id[args.container]
        check_container = CheckContainer(client.inspect_container(container_id))
        pprint(client.inspect_container(container_id))
        print('Docker Container Info:')
        container_result = check_container.check_container()
        print_result(**container_result)

if args.info:
    print()
    if args.image:
        show_info(**image_result)
    if args.container:
        show_info(**container_result)
