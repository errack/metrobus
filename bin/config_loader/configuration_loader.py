from ruamel.yaml import YAML

yaml = YAML(typ='safe')

class ConfigurationLoader:
    @staticmethod
    def load_config(config_file_path):
        with open(config_file_path, 'r') as stream:
            return yaml.load(stream)