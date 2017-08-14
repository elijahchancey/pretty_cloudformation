#!/usr/bin/env python3

# This program takes a Cloudformation template and makes it pretty by using the PyYaml library.
# The output is printed to STDOUT
# Usage: ./pretty_cloudformation.py example.yml

# Many thanks to Anthon for this StackOverflow answer: https://stackoverflow.com/a/43768117/3101224

import sys
import yaml
import argparse

parser = argparse.ArgumentParser(
    description='Make a Cloudformation YAML template pretty.')

parser.add_argument('filename', help='name of yaml file')

args = parser.parse_args()


class GenericScalar:
    def __init__(self, value, tag, style=None):
        self._value = value
        self._tag = tag
        self._style = style

    @staticmethod
    def to_yaml(dumper, data):
        # data is a GenericScalar
        return dumper.represent_scalar(
            data._tag, data._value, style=data._style)


def default_constructor(loader, tag_suffix, node):
    if isinstance(node, yaml.ScalarNode):
        return GenericScalar(node.value, tag_suffix, style=node.style)
    else:
        raise NotImplementedError('Node: ' + str(type(node)))


yaml.add_multi_constructor('', default_constructor, Loader=yaml.SafeLoader)

yaml.add_representer(
    GenericScalar, GenericScalar.to_yaml, Dumper=yaml.SafeDumper)

with open(args.filename, 'r') as myfile:
    data = myfile.read()

data = yaml.safe_load(data)

yaml.safe_dump(
    data,
    sys.stdout,
    default_flow_style=False,
    allow_unicode=True,
    indent=2,
    width=200)
